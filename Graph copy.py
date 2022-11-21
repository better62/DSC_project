
class Graph:
    def __init__(self):
        self.matrix = []
        self.size = 0
        self.column = ['info'] #column이랑 row를 따로 저장해둠
        self.row = []

    def insert(self, info): # 새 데이터 삽입, info에 id 나와 있으니까 이거로 쓰는거
        #info[0]을 확진자 id, #info[1]을 전파자 id라고 가정
        patient_id = info[0]
        infected_by = info[1]
        
        if patient_id in self.column: #column에 이미 확진자가 존재하면 그 index에 맞게 row에 추가하기 위함
            patient_idx_col = self.column.index(patient_id)
            self.row.insert(patient_idx_col, patient_id) 
        else:
            self.row.append(patient_id) #row, column 모두에 없던 확진자이므로 그냥 append
            self.column.insert(-1, patient_id)#column에도 추가
            for row in self.matrix:# 각 행에 0 하나씩 추가
                row.insert(-1,0)

        new = [0 for x in range(len(self.column)-1)] #새로 추가할 행, 아직은 전파자 id 반영 x
        new.append(info[2:])

        #new를 matrix에 삽입, 근데 column에는 이미 해당 id가 있을 수도 있으니
        #index 맞춰서 중간에 insert 혹은 column에도 없다면 append
        if self.row[-1] != patient_id:
            self.matrix.insert(patient_idx_col, new)
        else:
            self.matrix.append(new)
        
        #여기서부터 전파자(1)표시 작업 진행
        if infected_by != 0: #전파자가 알려져 있을 때
            if infected_by not in self.column:#아직 데이터 없는 환자로부터 감염
                self.column.insert(-1, infected_by) #전파자 id column에 추가
                for row in self.matrix:#전파자 열 추가를 위해 행에 0 모두 하나씩 더해준다
                    row.insert(-1,0)
            
            #전파자에 대한 열이 생겼으니 관계 표시
            inf_idx = self.column.index(infected_by) #column 선택
            if self.row[-1] != patient_id: #방금 추가한 행렬이 중간에 insert되었던 경우
                self.matrix[patient_idx_col][inf_idx] = 1
            else:
                self.matrix[len(self.row)-1][inf_idx] = 1
        return

    def update(self, info):
        #patient_id가 matrix 내에 이미 존재한다는 전제 하 진행
        patient_id = info[0]
        infected_by = info[1] 
        pat_idx = self.row.index(patient_id) #update할 row 선택

        self.matrix[pat_idx] = [0 for x in range(len(self.column)-1)] #전부 0으로 초기화
        self.matrix[pat_idx].append(info[2:]) #새로운 info 더해줌, 변경 되었는지 아닌지 확인 X

        if infected_by != 0 : #infected_by 관계 추가.
            if infected_by not in self.column:#아직 데이터 없는 환자로부터 감염
                self.column.insert(-1, infected_by) #전파자 id column에 추가
                for row in self.matrix:#전파자 열 추가를 위해 행에 0 모두 하나씩 더해준다
                    row.insert(-1,0)
            inf_idx = self.column.index(infected_by)
            self.matrix[pat_idx][inf_idx] = 1
        return
    #여기서도 데이터베이스에 없던 사람에 의해 감염되었을 수도 있으니 반영해야 함
    #재감염 여부

    def delete(self, patient_id):
        pat_idx = self.row.index(patient_id) #delete할 row 선택
        del self.matrix[pat_idx] #matrix에서 삭제하고, row 리스트에서도 삭제
        del self.row[pat_idx]
        return
    
    def print_graph(self):
        print(" ",self.column)
        for i in range(len(self.row)):
            print(self.row[i], self.matrix[i])
        return
    
    def patient_info(self, patient_id):
        pat_idx = self.row.index(patient_id)
        info = self.matrix[pat_idx][-1]

        if 1 in self.matrix[pat_idx]:
            inf_idx = self.matrix[pat_idx].index(1)
            infected_by = self.column[inf_idx]

        print("information of id",patient_id)
        print()
        print("infected by:", infected_by)
        print(info)
        return

    def infection_route(self):
        return

if __name__ == "__main__":
    graph = Graph()
    graph.insert([1,0,'m', 'f'])
    graph.print_graph()
    graph.insert([2,3,'m', 'f'])
    graph.print_graph()
    graph.insert([4,3,'s', 't'])
    graph.print_graph()
    print()
    graph.insert([3,1,'a','b'])
    graph.print_graph()
    graph.update([3,2,'a','c'])
    graph.print_graph()
    graph.delete(2)
    graph.print_graph()
    graph.insert([2,3,'m', 'f'])
    graph.print_graph()
    graph.patient_info(2)
    print()
    graph.update([2,6,'m','f'])
    graph.print_graph()
    graph.insert([5,4,'d','e'])
    graph.print_graph()