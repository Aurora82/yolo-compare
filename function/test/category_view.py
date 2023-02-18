from classes.res import Result, CategoryView

if __name__ == "__main__":
    view = CategoryView()
    view.a_category = 10
    # view.a_category = '1234125412'

    res = Result()
    res.category_view.append(view)
    for item in res.category_view:
        print(item.a_category)
