import time
import winsound
from itertools import combinations_with_replacement


freqs = {"la": 220,
         "si": 247,
         "do": 261,
         "re": 293,
         "mi": 329,
         "fa": 349,
         "sol": 392,
         }


notes = ("sol,250-mi,250-mi,500-fa,250-re,250-re,500-do,250-re,"
         "250-mi,250-fa,250-sol,250-sol,250-sol,500")

notes_list = notes.split("-")
# print(type(notes_list))
# for phrase in notes_list:
#     temp = phrase.split(",")
#     note = temp[0]
#     duration = int(temp[1])
#     winsound.Beep(freqs[note], duration)


# numbers = iter(list(range(1, 101)))
# for i in numbers:
#    next(numbers)
#    next(numbers)
#    print(i)


class Note():
    def __init__(self, name, frequency):
        self._name = name
        self.frequency = frequency

    def get_name(self):
        return self._name

    def get_frequency(self):
        return self.frequency


class MusicNotes():
    def __init__(self):
        self._notes_list = [
            Note("La", [55, 110, 220, 440, 880]),
            Note("Si", [61.74, 123.48, 246.96, 493.92, 987.84]),
            Note("Do", [65.41, 130.82, 261.64, 523.28, 1046.56]),
            Note("Re", [73.42, 146.84, 293.68, 587.36, 1174.72]),
            Note("Mi", [82.41, 164.82, 329.64, 659.28, 1318.56]),
            Note("Fa", [87.31, 174.62, 349.24, 698.48, 1396.96]),
            Note("Sol", [98, 196, 392, 784, 1568])
        ]
        self._note_index = 0
        self._freq_index = 0

    def add_note(self, new_node):
        self._notes_list.append(new_node)

    def __iter__(self):
        return self

    def __next__(self):
        if self._note_index >= len(self._notes_list):
            self._note_index = 0
            self._freq_index += 1
        if self._freq_index >= len(self._notes_list[0].get_frequency()):
            raise StopIteration
        frequency =  self._notes_list[self._note_index].get_frequency()[self._freq_index]
        self._note_index += 1
        return frequency


notes_iter = iter(MusicNotes())
for freq in notes_iter:
    print(freq)