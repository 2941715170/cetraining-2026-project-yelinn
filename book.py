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
    
if __name__ == "__main__":
    # 测试创建对象
    book1 = Book("101", "Python入门教程", "张三", 5)
    print("测试1-创建图书：", book1.title, "库存：", book1.stock)
    # 测试转字典
    book_dict = book1.to_dict()
    print("测试2-转字典：", book_dict)
    # 测试从字典还原
    test_data = {"book_id": "102", "title": "Java基础", "author": "李四", "stock": 3, "borrowers": ["王五"]}
    book2 = Book.from_dict(test_data)
    print("测试3-字典转对象：", book2.title, "借阅人：", book2.borrowers)
    print("\n所有测试通过！")