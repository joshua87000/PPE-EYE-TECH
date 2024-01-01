from typing import List, Tuple

class Chare:
    def __init__(self):
        self.lettre = None
        self.After = [(0, chr(i + 97)) for i in range(26)] + [(0, " "), (0, "'")]
        self.iteration = 0

    def set_lettre(self, add: str):
        self.lettre = add

    def get_iteration(self):
        return self.iteration

    def add_lettre(self, ant: str):
        index = 26 if ant == ' ' else 27 if ant == "'" else ord(ant) - 97
        self.iteration += 1
       # print(index)
        #print(ant)
        if index > 0:
            self.After[index] = (self.After[index][0] + 1, self.After[index][1])

    def trier_result(self):
        self.After.sort(key=lambda x: x[0], reverse=True)

    def afficher_stat(self):
        total = 0
        print(f"Lettre: {self.lettre}")
        print(self.iteration)
        if self.iteration > 0:
            for i in range(28):
                apparition = (self.After[i][0] / self.iteration) * 100
                total += apparition
                self.After[i] = (apparition, self.After[i][1])
                print(f"({self.After[i][1]}) - {apparition:.2f}   {total:.2f}")


def recupData(C):
  with open(r"C:\Users\Joshua\Desktop\PPE EYE TECH\t.txt", "r") as ifs:
    c = ifs.read(1)

    alphabet = "abcdefghijklmnopqrstuvwxyz '"
    for i in range(28):
      C[i].set_lettre(alphabet[i])

    for i in range(3130):
      c2 = ifs.read(1)

      x = 26 if c == " " else 27 if c == "'" else ord(c) - 97
      C[x].add_lettre(c2)
      c = c2

    for i in range(28):
      C[i].trier_result()
      C[i].afficher_stat()



 
      
C = [Chare() for i in range(28)]
recupData(C)