class Node:
    def __init__(self):
        self.children = defaultdict(Node)
        self.content = ""


class FileSystem:

    def __init__(self):
        self.root = Node()

    def find(self, path):
        if path == "/":
            return self.root
        parts = path.split("/")[1:]
        cur = self.root
        for part in parts:
            cur = cur.children[part]
        return cur

    def ls(self, path: str) -> List[str]:
        cur = self.find(path)
        ans = []
        if cur.children:
            for child in cur.children:
                ans.append(child)
            return ans
        else:
            return [path.split("/")[-1]]

    def mkdir(self, path: str) -> None:
        self.find(path)

    def addContentToFile(self, filePath: str, content: str) -> None:
        self.find(filePath).content += content

    def readContentFromFile(self, filePath: str) -> str:
        return self.find(filePath).content
