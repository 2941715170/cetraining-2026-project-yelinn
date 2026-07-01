from book import Book


class LibraryManager:
    def __init__(self):
        """初始化图书管理器，创建空的图书列表"""
        self.books = []

    def add_book(self, book_id, title, author, stock):
        """添加新图书，校验编号重复和库存格式"""
        # 校验编号重复
        for book in self.books:
            if book.book_id == book_id:
                return False, "❌ 添加失败：图书编号已存在"
        # 校验库存格式
        try:
            stock_num = int(stock)
            if stock_num < 0:
                return False, "❌ 添加失败：库存不能为负数"
        except ValueError:
            return False, "❌ 添加失败：库存必须是数字"
        # 添加图书
        new_book = Book(book_id, title, author, stock_num)
        self.books.append(new_book)
        return True, f"✅ 添加成功：《{title}》已加入书库，库存{stock_num}本"

    def borrow_book(self, book_id, borrower_name):
        """借阅图书，校验库存"""
        for book in self.books:
            if book.book_id == book_id:
                if book.stock <= 0:
                    return False, "❌ 借阅失败：图书库存不足，已全部借出"
                book.stock -= 1
                book.borrowers.append(borrower_name)
                return True, f"✅ 借阅成功：《{book.title}》剩余库存{book.stock}本"
        return False, f"❌ 借阅失败：未找到编号为 {book_id} 的图书"

    def return_book(self, book_id, borrower_name):
        """归还图书，校验借阅记录"""
        for book in self.books:
            if book.book_id == book_id:
                if borrower_name not in book.borrowers:
                    return False, "❌ 归还失败：该用户未借阅此图书"
                book.stock += 1
                book.borrowers.remove(borrower_name)
                return True, f"✅ 归还成功：《{book.title}》当前库存{book.stock}本"
        return False, f"❌ 归还失败：未找到编号为 {book_id} 的图书"

    def search_book(self, keyword):
        """按关键词模糊查询，不区分大小写"""
        keyword_lower = keyword.lower()
        results = []
        for book in self.books:
            if keyword_lower in book.title.lower() or keyword_lower in book.author.lower():
                results.append(book)
        return True, results

    def get_all_books(self):
        """获取所有图书"""
        return True, self.books
    