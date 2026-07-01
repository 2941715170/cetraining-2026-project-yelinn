class Book:
    def __init__(self, book_id, title, author, stock, borrowers=None):
        """
        初始化图书对象
        :param book_id: 图书唯一编号
        :param title: 书名
        :param author: 作者
        :param stock: 库存数量（非负整数）
        :param borrowers: 借阅人列表，默认空列表
        """
        self.book_id = book_id
        self.title = title
        self.author = author
        self.stock = stock
        # 避免所有实例共享同一个列表
        self.borrowers = borrowers if borrowers else []

    def to_dict(self):
        """将图书对象转为字典，用于JSON存储"""
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "stock": self.stock,
            "borrowers": self.borrowers
        }

    @classmethod
    def from_dict(cls, data):
        """从字典数据还原为Book对象"""
        return cls(
            data["book_id"],
            data["title"],
            data["author"],
            data["stock"],
            data.get("borrowers", [])
        )
    
