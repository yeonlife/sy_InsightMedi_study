import copy
def add_label(key, value):
    try:
        added_directory = result_dict[frame_number]

    except KeyError:
        new_original_dict = copy.deepcopy(original_dict)
        result_dict[frame_number] = new_original_dict
        added_directory = result_dict[frame_number]
    
    print(added_directory)
    added_directory[key].append(value)

original_dict = {'line': [], 'rectangle': []}
result_dict = {0: {'line':[], 'rectangle': [(2,3,4,5)]}}

print("현재 frame이 1인 상태")
frame_number = 1
add_label('rectangle', (1,2,3,4))

print("\n현재 frame이 2인 상태")
frame_number = 2
add_label('rectangle', (4,5,6,7))
print(result_dict)



"""     def add_label(self, key, value):    #key: label_type / value: 좌표
        #print("전체 frame별 label dictionary", self.frame_label_dict)
        try:
            ld = self.frame_label_dict[self.frame_number]
        except KeyError:
            new_label_dict_schema = self.label_dict_schema.copy()
            self.frame_label_dict[self.frame_number] = new_label_dict_schema
            ld =  self.frame_label_dict[self.frame_number]
            print("새로운 frame에 label을 그렸을 때 text파일에 들어갈 정보 틀 생성")
            print(self.label_dict_schema.copy())
            
        ld[key].append(value)
        print("확인",ld)
        print("현재 framenumber", self.frame_number) """