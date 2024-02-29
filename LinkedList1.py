class Node:
    """Tugun (node) obyekti"""

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Linked List obyekti"""

    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def push(self, new_data):
        """List boshiga tugun qo'shish"""
        # Yangi node yaratamiz
        new_node = Node(new_data)
        # List boshini keyingi o'ringa suramiz
        new_node.next = self.head
        # Yangi nodeni list boshiga qo'yamiz
        self.head = new_node

    def insertAfter(self, prev_node, new_data):
        """Biror tugundan so'ng tugun qo'shish"""
        if prev_node is None:
            print("Tugun mavjud emas")
            return
        # Yangi tugun qo'shamiz
        new_node = Node(new_data)
        # Yangi tugunni keyingi tugunga bog'laymiz
        new_node.next = prev_node.next
        # Avvalgi tugunni yangi tugunga bog'laymiz
        prev_node.next = new_node

    def append(self, new_data):
        """List oxiriga tugun qo'shish"""
        # Yangi tugun yaratamiz
        new_node = Node(new_data)
        # List bo'sh emasligini tekshriamiz
        if self.head is None:
            # Bo'sh bo'lsa yangi tugun list boshiga tushadi
            self.head = new_node
            return
        # Aks holda List oxiriga boramiz
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node


## Linked List yaratamiz
llist = LinkedList()
print("____________________________________________________")


## Uchta node (tugun) yaratamiz
llist.head = Node('Dushanba')
tuesday = Node('Seshanba')
wednesday = Node('Chorshanba')

## Tugunlarni bog'laymiz
llist.head.next = tuesday
tuesday.next = wednesday

## Linked Listni konsolga chiqaramiz:
llist.printList()
print("____________________________________________________")

## List boshiga yangi tugun qo'shamiz
llist.push('Yakshanba')
llist.push('Dushanba')
llist.push('Seshanba')
llist.push('Chorshanba')
llist.push('Payshanba')

llist.printList()
print("____________________________________________________")

## List o'rtasiga element qo'shamiz
llist.insertAfter(llist.head.next.next, 'Seshanba Kechasi')
llist.printList()
print("____________________________________________________")
llist.insertAfter(llist.head.next.next.next, 'Dushanba Ertalab')
llist.printList()
print("____________________________________________________")
llist.insertAfter(llist.head.next.next.next.next.next, 'Dushanba Kechasi')
llist.printList()
print("____________________________________________________")
llist.insertAfter(llist.head.next.next.next.next.next.next, 'Yakshanba Ertalab')
llist.printList()
print("____________________________________________________")
llist.insertAfter(llist.head.next, 'Chorshanba Ertalab')
llist.printList()
print("____________________________________________________")

## List oxiriga tugun qo'shamiz
llist.append('Payshanba')
llist.append('Juma')
llist.append('Shanba')
llist.append('Yakshanba')
llist.append('Dushanba')
llist.printList()
print("____________________________________________________")



