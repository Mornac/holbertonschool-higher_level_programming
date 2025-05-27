#!/usr/bin/env python3


class VerboseList(list):
    def append(self, item):
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, item_added):
        super().extend(item_added)

        print("Extended the list with [{}] items.".format(len(item_added)))

    def remove(self, removed_item):
        super().remove(removed_item)
        print("Removed [{}] from the list.".format(removed_item))

    def pop(self, index=-1):
        if index == -1:
            popped_item = self[-1]
        else:
            popped_item = self[index]
        super().pop(index)
        print("Popped [{}] from the list.".format(popped_item))
        return popped_item
