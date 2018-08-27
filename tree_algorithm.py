import os

class Node:
    '''
        Узел дерева файловой системы.
    '''
    def __init__(self, name):
        self.name = name.split("/")[-1]
        self.full_name = name
        self.children = []
        
        
    def set_children(self, item):
        '''
            функция для добавления узла в дочерние
        '''
        self.children.append(item)
        
class Tree:
    '''
        Дерево файловой системы. Корневой узел - root.
    '''
    def __init__(self, path):
        self.root = Node(path)
        self.count = 0
        self.stack = []
        self.queque = []
        
        self.search_children(self.root)
        
        
    def search_children(self, node):
        '''
            Рекурсивная функция для создания дерева путем поиска
            всех узлов.
        '''
        #определяем содежимое текущей директории, сортируем его
        child_list_ord = os.listdir(node.full_name)
        child_list_ord.sort()
        
        for f in child_list_ord:
            new_node = Node(node.full_name+'/'+f)
            node.set_children(new_node)
            if os.path.isdir(new_node.full_name):
                self.search_children(new_node)
                
    def display_tree(self, node, space):
        '''
            функция для отображения дерева
        '''
        for i in node.children:
            print("{}{}".format(space, i.name))
            if i.children:
                self.display_tree(i, "  {}".format(space))
                
    def exists(self, node, name):
        '''
            рекурсивная функция для обхода дерева и поиска
            совпадения по имени
        '''
        if node.name == name:
            return True
        for i in node.children:
            if i.name == name:
                return True
            elif i.children:
                result = self.exists(i, name)
                if result:
                    return True
        return False
    
    def search_name_by_stack(self, name):
        '''
            функция для обхода дерева, используя стек
            (обход вглубь)
        '''
        print("Обход в глубину с использованием стека")
        self.count = 0
        #добавляем в стек корневой узел
        self.stack.append(self.root)
        while self.stack:
            #извлекаем с вершины стека узел
            node = self.stack.pop()
            #проверяем на совпадение
            if node.name == name:
                return True
            #вставляем в стек дочерние элементы, 
            #таким образом на вершине всегда будет находится дочерний
            #элеммент предыдущего, пока не дойдем до листа
            for i in node.children:
                self.stack.append(i)
            self.count += 1
        return False
        
    def search_name_by_queue(self, name):
        '''
            функция для обхода дерева, используя очередь
            (обход в ширину)
        '''
        
        print("Обход в ширину с использованием череди")
        self.count = 0
        #добавляем в очередь корневой узел
        self.queque.append(self.root)
        while self.queque:
            #извлекаем из головы очереди узел, проверяем на соответствие
            node = self.queque.pop(0)
            if node.name == name:
                return True
            #дочерние узлы текущего добавляем в конец очереди,
            #таким образом мы пройдем сначала по всем дочерним узлам
            #текущего, а уже потом перейдем во "внучатые"
            for i in node.children:
                self.queque.append(i)
            self.count += 1
        return False
                
            
if __name__=="__main__":    
    path = "/path/to/directory"                
    tree = Tree(path)
    #tree.display_tree(tree.root, "")

    print(tree.exists(tree.root, "search_name"))
    print(tree.search_name_by_stack("search_name"))
    print(tree.count)
    print(tree.search_name_by_queue("search_name"))
    print(tree.count)
