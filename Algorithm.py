class AlgorithmExercises:
    def data_processing(self):
        print("===数据处理算法 ===\n")
        numbers=[3,1,4,1,5,9,2,6,5,3,5]
        word=["apple","banana","apple","orange","banana","apple"]
        text="hello world this is a test hello world"

        #冒泡排序实战-学生成绩排序
        def bubble_sort_grades(grades):
            n=len(grades)
            for i in range(n):
                for j in range(0,n-i-1):
                    if grades[j]>grades[j+1]:
                        grades[j],grades[j+1]=grades[j+1],grades[j]
            return grades
        grades=[85,92,78,60,95,72,88]
        print(f"学成成绩排序：")
        print(f"原始成绩：{grades}")
        print(f"排序后：{bubble_sort_grades(grades.copy())}")

        def word_frequecy(text):
            words=text.split()
            freq={}
            for word in words:
                freq[word]=freq.get(word,0)+1
            return freq

        print(f"\n2. 词频统计")
        print(f"文本：'{text}'")
        print(f"词频：{word_frequecy(text)}")

        #1.3列表去重-去除重复订单
        def remove_duplicates(order_ids):
            seen=set()
            unique_orders=[]
            for order_id in order_ids:
                if order_id not in seen:
                    seen.add(order_id)
                    unique_orders.append(order_id)
            return unique_orders
        order_ids=[1001,1002,1001,1003,1002,1004]
        print(f"\n3订单去重")
        print(f"原始订单：{order_ids}")
