class Pagination:
    def __init__(self, data: list, page_size: int):
        self._data_ = []
        self._page_size_ = page_size
        self._cur_page_ = 0

        j = 0
        for i in range(len(data) // page_size + 1):
            cur_page = data[j:page_size * (i + 1)]
            if cur_page:
                self._data_.append(cur_page)
            j += page_size

    @property
    def total_pages(self):
        return len(self._data_)

    @property
    def current_page(self):
        return self._cur_page_ + 1

    def get_visible_items(self):
        return self._data_[self._cur_page_]

    def next_page(self):
        if not self._cur_page_ == len(self._data_) - 1:
            self._cur_page_ += 1
        return self

    def prev_page(self):
        if self._cur_page_ != 0:
            self._cur_page_ -= 1
        return self

    def last_page(self):
        self._cur_page_ = len(self._data_) - 1

    def first_page(self):
        self._cur_page_ = 0

    def go_to_page(self, page_num: int):
        if page_num - 1 < 0:
            self.first_page()
        elif page_num > len(self._data_):
            self.last_page()
        else:
            self._cur_page_ = page_num - 1


# более умное решение, верно:
#
#
# class Pagination:
#     def __init__(self, data, size):
#         self.pages = [data[i: i + size] for i in range(0, len(data), size)]
#         self.total_pages = len(self.pages)
#         self.current_page = 1
#
#     def prev_page(self):
#         self.current_page = max(1, self.current_page - 1)
#         return self
#
#     def next_page(self):
#         self.current_page = min(self.total_pages, self.current_page + 1)
#         return self
#
#     def first_page(self):
#         self.current_page = 1
#
#     def last_page(self):
#         self.current_page = self.total_pages
#
#     def go_to_page(self, page):
#         self.current_page = max(1, min(page, self.total_pages))
#
#     def get_visible_items(self):
#         return self.pages[self.current_page - 1]
