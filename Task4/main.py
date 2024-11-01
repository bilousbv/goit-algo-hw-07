class Comment:
    def __init__(self, text, author):
        self.text = text
        self.author = author
        self.replies = []
        self.is_deleted = False

    def add_reply(self, reply):
        """Додає нову відповідь до коментаря."""
        self.replies.append(reply)

    def remove_reply(self):
        """Видаляє коментар, замінюючи текст на 'Цей коментар було видалено.' і встановлюючи прапорець is_deleted."""
        self.text = "Цей коментар було видалено."
        self.is_deleted = True

    def display(self, level=0):
        """Рекурсивно виводить коментар та всі його відповіді з відступами для відображення ієрархії."""
        indent = "    " * level
        if not self.is_deleted:
            print(f"{indent}{self.author}: {self.text}")
        else:
            print(f"{indent}{self.text}")

        for reply in self.replies:
            reply.display(level + 1)


# Приклад використання
root_comment = Comment("Яка чудова книга!", "Бодя")
reply1 = Comment("Книга повне розчарування :(", "Андрій")
reply2 = Comment("Що в ній чудового?", "Марина")

root_comment.add_reply(reply1)
root_comment.add_reply(reply2)

reply1_1 = Comment("Не книжка, а перевели купу паперу ні нащо...", "Сергій")
reply1.add_reply(reply1_1)

# Видаляємо коментар Андрія
reply1.remove_reply()

# Виведення ієрархії коментарів
root_comment.display()