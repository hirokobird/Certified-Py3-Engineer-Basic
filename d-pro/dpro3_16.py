# No.16

class Sample:
    c_list = []

    def add_c_list(self, data):
        self.c_list.append(data)

print("出力結果:", end=" ")
sample1 = Sample()
sample1.add_c_list("データ1")

sample2 = Sample()
sample2.add_c_list("データ2")

for item_data in sample1.c_list:
    print(item_data, end=" ")