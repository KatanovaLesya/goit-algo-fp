class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

# Додавання вузла на кінець списку
    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
# Відображення списку
    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.value, end=" -> ")
            current_node = current_node.next
        print("None")

def reverse_linked_list(ll):
    previous = None
    current = ll.head
    while current:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node
    ll.head = previous

def insert_sorted(sorted_ll, new_node):
    # Перевірка чи новий вузол не є None
    if new_node is None:
        raise ValueError("New node is None")

    # Перевірка чи відсортований список існує
    if sorted_ll is None:
        raise ValueError("Sorted linked list is None")

    # Вставка нового вузла на початок відсортованого списку
    if not sorted_ll.head or sorted_ll.head.value >= new_node.value:
        new_node.next = sorted_ll.head
        sorted_ll.head = new_node
    else:
        # Проходимо по списку і знаходимо правильне місце для вставки
        current = sorted_ll.head
        while current.next and current.next.value < new_node.value:
            current = current.next
        
        # Перевірка чи наступний вузол не є None
        if current is None:
            raise RuntimeError("Current node is None during insertion")

        # Вставка нового вузла у правильну позицію
        new_node.next = current.next
        current.next = new_node

def insertion_sort_linked_list(ll):
    sorted_ll = LinkedList()
    current = ll.head
    while current:
        next_node = current.next
        insert_sorted(sorted_ll, current)
        current = next_node
    ll.head = sorted_ll.head

def merge_sorted_linked_lists(ll1, ll2):
    dummy = Node()
    tail = dummy
    l1 = ll1.head
    l2 = ll2.head

    while l1 and l2:
        if l1.value < l2.value:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    if l1:
        tail.next = l1
    elif l2:
        tail.next = l2

    merged_ll = LinkedList()
    merged_ll.head = dummy.next
    return merged_ll

# Приклад використання з обробкою помилок
try:
    ll = LinkedList()
    ll.append(4)
    ll.append(2)
    ll.append(1)
    ll.append(3)

    print("Початковий список:")
    ll.print_list()

    # Сортуємо список вставками
    insertion_sort_linked_list(ll)
    print("Відсортований список:")
    ll.print_list()

    # Створюємо ще один відсортований список
    ll1 = LinkedList()
    ll1.append(1)
    ll1.append(3)
    ll1.append(5)

    ll2 = LinkedList()
    ll2.append(2)
    ll2.append(4)
    ll2.append(6)

    print("Перший відсортований список:")
    ll1.print_list()
    print("Другий відсортований список:")
    ll2.print_list()

    # Об'єднуємо два відсортовані списки
    merged_ll = merge_sorted_linked_lists(ll1, ll2)
    print("Об'єднаний відсортований список:")
    merged_ll.print_list()

except Exception as e:
    print(f"An error occurred: {e}")
