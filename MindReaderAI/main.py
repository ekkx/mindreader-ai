import time
import random

import g4f
import yaylib

from .db import DB


# GPTプロバイダーの設定
providers = [
    g4f.Provider.GptGo,
    g4f.Provider.You,
    g4f.Provider.GptForLove,
    g4f.Provider.GPTalk,
]


class MindReader:
    def __init__(self, db_path: str, email: str, password: str) -> None:
        self.db = DB(db_path)

        self.client = yaylib.Client()
        self.client.login(email, password)

    def run(self, root_post_id: int) -> None:
        while True:
            reposts = self.client.get_reposts(root_post_id, number=15).posts

            # 新しい(´∀｀∩)↑age↑が見つからない場合はスキップする
            if self.db.has_new(reposts) is False:
                self.client.logger.info("新しい(´∀｀∩)↑age↑を待機しています...")
                time.sleep(60)
                continue

            for repost in reposts:
                if self.db.is_queued(repost.id):
                    continue

                # ユーザーの投稿数が少ない場合はスキップする
                if self.client.get_user(repost.user.id).posts_count < 5:
                    self.client.create_post(
                        "投稿数が少ないよ！😭",
                        in_reply_to=repost.id,
                        mention_ids=[repost.user.id],
                    )
                    self.db.queue(repost.id)
                    continue

                try:
                    prompt = f"以下の文章は{repost.user.nickname}さんの「Yay!」というSNSの投稿本文一覧です。投稿本文から{repost.user.nickname}さんがどういう人物像だと推測されるか150文字程度で教えてください。\n\n---\n\n"

                    user_timeline = self.client.get_user_timeline(
                        repost.user.id, number=100
                    )

                    # テキストを含まない場合はスキップ
                    for user_post in user_timeline.posts:
                        if user_post.text:
                            prompt += f"{user_post.text}\n"

                    # 生成に成功するまで繰り返す
                    while True:
                        charactor_amount = 2500

                        try:
                            generated_answer = g4f.ChatCompletion.create(
                                model="gpt-3.5-turbo",
                                provider=random.choice(providers),
                                messages=[
                                    {
                                        "role": "user",
                                        "content": prompt[:charactor_amount],
                                    }
                                ],
                            )[:480]
                            break

                        except Exception as e:
                            self.client.logger.error(e)
                            charactor_amount -= 500

                    generated_answer += "\n\nMindReader AI より"

                    res = self.client.create_post(
                        generated_answer,
                        in_reply_to=repost.id,
                        mention_ids=[repost.user.id],
                    )

                    print(res.text)

                    self.db.queue(repost.id)

                    self.client.logger.info("15秒待機します")
                    time.sleep(15)

                except yaylib.ForbiddenError:
                    self.client.logger.info("非公開のユーザー")
                    self.client.create_post(
                        "投稿が非公開ですよ。",
                        in_reply_to=repost.id,
                        mention_ids=[repost.user.id],
                    )
                    continue

                except Exception as e:
                    self.client.logger.critical(e)
                    time.sleep(300)
