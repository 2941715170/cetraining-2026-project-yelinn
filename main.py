from library_manager import LibraryManager


def print_menu():
    """打印主菜单"""
    print("\n" + "="*40)
    print("📚  小型图书借阅管理系统  📚")
    print("="*40)
    print("1. 📖 录入图书信息")
    print("2. 🔍 查询图书（模糊搜索）")
    print("3. 📤 借阅图书")
    print("4. 📥 归还图书")
    print("5. 📋 查看所有图书及状态")
    print("0. 🚪 退出系统")
    print("="*40)


def main():
    """主程序入口"""
    manager = LibraryManager()
    print("🎉 欢迎使用图书借阅管理系统！")

    while True:
        print_menu()
        choice = input("请输入操作编号：").strip()

        if choice == "0":
            print("\n👋 感谢使用，系统已退出，再见！")
            break

        elif choice == "1":
            print("\n--- 录入图书信息 ---")
            book_id = input("请输入图书编号：").strip()
            title = input("请输入书名：").strip()
            author = input("请输入作者：").strip()
            stock = input("请输入库存数量：").strip()
            if not book_id or not title or not author or not stock:
                print("⚠️  输入有误：所有内容都不能为空")
                continue
            success, msg = manager.add_book(book_id, title, author, stock)
            print(msg)

        elif choice == "2":
            print("\n--- 图书查询 ---")
            keyword = input("请输入书名/作者关键词：").strip()
            if not keyword:
                print("⚠️  关键词不能为空")
                continue
            success, results = manager.search_book(keyword)
            if not results:
                print("😕 未找到匹配的图书")
            else:
                print(f"\n✅ 找到 {len(results)} 本匹配的图书：")
                print("-"*50)
                for idx, book in enumerate(results, 1):
                    borrower_info = "、".join(book.borrowers) if book.borrowers else "无"
                    status = "可借阅" if book.stock > 0 else "已借完"
                    print(f"{idx}. 编号：{book.book_id}")
                    print(f"   书名：《{book.title}》")
                    print(f"   作者：{book.author}")
                    print(f"   库存：{book.stock} 本 | 状态：{status}")
                    print(f"   当前借阅人：{borrower_info}")
                    print("-"*50)

        elif choice == "3":
            print("\n--- 借阅图书 ---")
            book_id = input("请输入要借阅的图书编号：").strip()
            borrower = input("请输入借阅人姓名：").strip()
            if not book_id or not borrower:
                print("⚠️  编号和姓名都不能为空")
                continue
            success, msg = manager.borrow_book(book_id, borrower)
            print(msg)

        elif choice == "4":
            print("\n--- 归还图书 ---")
            book_id = input("请输入要归还的图书编号：").strip()
            borrower = input("请输入归还人姓名：").strip()
            if not book_id or not borrower:
                print("⚠️  编号和姓名都不能为空")
                continue
            success, msg = manager.return_book(book_id, borrower)
            print(msg)

        elif choice == "5":
            print("\n--- 所有图书列表 ---")
            success, all_books = manager.get_all_books()
            if not all_books:
                print("📭 书库中暂无图书")
            else:
                print(f"共 {len(all_books)} 本图书：")
                print("-"*60)
                print(f"{'编号':<6}{'书名':<20}{'作者':<12}{'库存':<6}{'状态':<8}")
                print("-"*60)
                for book in all_books:
                    status = "可借阅" if book.stock > 0 else "已借完"
                    print(f"{book.book_id:<6}{book.title:<18}{book.author:<12}{book.stock:<6}{status:<8}")
                print("-"*60)

        else:
            print("⚠️  输入无效，请输入 0-5 之间的数字")


if __name__ == "__main__":
    main()