class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.tracks = None
        self.size = 0

    def enqueue(self, data):
        node = Node(data)
        if self.tracks is None:
            self.tracks = node
            return
        else:
            current = self.tracks
            while current.next:
                current = current.next
            current.next = node

        self.size += 1

    def dequeue(self):
        first = self.tracks.data
        self.tracks = self.tracks.next
        self.size -= 1
        return first

    def iter(self):
        current = self.tracks
        while current:
            val = current.data
            current = current.next
            yield val


class Track:
    def __init__(self, title=None):
        self.title = title


class MediaQueue(Queue):
    def __init__(self):
        super().__init__()

    def add_song(self, data):
        self.enqueue(data)

    def play(self):
        while self.size >= 1:
            current_song = self.dequeue()
            print(f'Now playing:{current_song.title}')


if __name__ == "__main__":
    player = MediaQueue()
    songs = ['Dior', 'Kondiko', 'Geri Inengi']
    for song in songs:
        track = Track(song)
        player.add_song(track)

    player.play()
