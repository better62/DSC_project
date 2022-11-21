import numpy as np

class Graph:
    def __init__(self):
        self.matrix = []
        self.size = 0

    def insert(self, patient_id, infected_by, info):    # 새로운 데이터 삽입, 새로운 경로 삽입
        if infected_by != None: # 감염 경로가 있을 때
            if infected_by > self.size: # 아직 데이터가 없는 환자에게서 감염 되었으면
                k = infected_by - self.size # matrix 행과 열을 추가로 생성
                if self.size == 0:
                    for _ in range(k):
                        self.matrix.append([0]*k)
                        self.size += 1
                else:

                    for row in self.matrix: # 기존에 존재하는 행에 열 추가 생성
                        for _ in range(k):
                            row.insert(-2, 0)
                    self.size += infected_by
            else:
                if patient_id > self.size:
                    k = patient_id - self.size
                    for _ in range(k):  # 행 추가 생성
                        self.matrix.append([0] * self.size)
                    for row in self.matrix:  # 기존에 존재하는 행에 열 추가 생성
                        for _ in range(k):
                            row.insert(-2, 0)
                    self.size += k

            self.matrix[infected_by-1][patient_id-1] = 1    # 데이터 넣기
            self.matrix[patient_id-1].append(info)

        else:   # 감염 경로가 없을 떄
            if self.size == 0:
                self.matrix.append([0, info])
                self.size += 1
            else:
                if patient_id > self.size:
                    k = patient_id - self.size
                    for _ in range(k):  # 행 추가 생성
                        self.matrix.append([0] * self.size)
                    for row in self.matrix:  # 기존에 존재하는 행에 열 추가 생성
                        for _ in range(k):
                            row.insert(-2, 0)
                    self.size += k
                self.matrix[patient_id-1].append(info)



    def info_update(self, patient_id, info): # patient_id로 접근해서 정보나 감염 경로 수정
        print("*" * 10, "Patient information update", "*" * 10)
        if patient_id > self.size:  # 존재하지 않는 데이터를 업데이트 하려고 할 때 에러
            print("error")
            return
        else:
            print("Before:", self.matrix[patient_id-1][-1])
            self.matrix[patient_id-1][-1] = info
            print("Update Success")
            print("Updated patient info:", self.matrix[patient_id-1][-1])
            return

    def path_update(self, patient_id, infected_by):
        """어떻게 수정할 지 사용자에게 입력을 받는 게 좋을 듯
        어떤 정보를 어떻게 수정"""
        self.matrix[infected_by-1][patient_id-1] = 1
        return

    def delete(self, patient_id):
        if patient_id > self.size:  # 존재하지 않는 데이터를 지우려고 할 때 에러
            print("error")
            return
        else:   # 존재할 때
            for row in self.matrix:
                row[patient_id-1] = 0
            self.matrix[patient_id-1] = []

    def print_graph(self):  # 전체 그래프 출력
        print("*" * 10, "Printing graph", "*" * 10)
        print(self.matrix)

    def patient_info(self, patient_id): # 어떤 환자 정보 반환
        return self.matrix[patient_id-1][-1]

    def infection_route(self, patient_id):  # 어떤 환자가 누구에게서 감염되었는지, 누구를 감염시켰는지 출력
        print("*"*10, "Infection route", "*"*10)
        infected = np.array(self.matrix).T[0]   # 여기서 오류 발생
        pos = np.where(np.array(infected) == 1)[0]
        pos += 1
        print("patient", patient_id, "is infected by patient ", end="")
        print(*pos)
        infect = self.matrix[patient_id-1][:-1]
        pos = np.where(np.array(infect) == 1)[0]
        pos += 1
        print("patient", patient_id, "infects patient ", end="")
        print(*pos)
        # patient_id로 접근해서 출력
        return


if __name__ == "__main__":
    graph = Graph()
    graph.insert(1, 4, ['m', 'f'])
    graph.insert(2, None, ['m', 'f'])
    graph.insert(3, 1, ['s', 't'])
    graph.insert(4, None, ['s,', 't'])
    graph.insert(5, 1, ['s,', 't'])
    graph.print_graph()
    graph.infection_route(1)
    graph.info_update(1, ['s', 't'])
    graph.print_graph()