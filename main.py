# plank Puzzle Solver


import csv

# a list of lists of the plank space
class plankProblem:
    def __init__(self):
        self.elements = []

    def addElement(self, list):
        self.elements.extend(list)

    def displayPlankProblem(self):
        print(self.elements)

    def getElement(self,x,y):
        return self.elements[x][y]

    def getLength(self):
        return len(self.elements)

    def getElements(self):
        return self.elements
# a Node is a combination of a node and state
class node:
    def __init__(self, currentPos, holdingPlankSize, plankPosList):
        self.currentPos = currentPos
        self.holdingPlankSize = holdingPlankSize
        self.plankPosList = plankPosList

    def isHoldingPlank(self):
        if self.holdingPlankSize == '0':
            return False
        else:
            return True

    def getPlankPos(self,index):
        return self.plankPosList[index]

    def getPlankPosList(self):
        return self.plankPosList

    def getCurrentPos(self):
        return self.currentPos

    def getHoldingPlankSize(self):
        return self.holdingPlankSize

    def updatePlankPosList(self,index, value):
        self.plankPosList[index] = value

    def setHoldingPlankSize(self, value):
        self.holdingPlankSize = value

    def __repr__(self):

        return "Node currentPos: " + self.currentPos + " holdingPlankSize: " +  self.holdingPlankSize + " PlankPosList: " + ' '.join(self.plankPosList)





# possible movements include : moveTo, pickUp, putDown
class action:
    def __init__(self, target, movement):
        self.target = target
        self.movement = movement

    def getTarget(self):
        return self.target

    def getMovement(self):
        return self.movement

    def __repr__(self):
        return "action: " + self.movement + " " +  self.target



def actions(node, plankProblem):

    list =[]
    for x in range(plankProblem.getLength()):
        if node.getCurrentPos() == plankProblem.getElement(x,0) and node.getPlankPos(x) == 'T':
            list.append(action(plankProblem.getElement(x,1), 'moveTo'))
        if node.getCurrentPos() == plankProblem.getElement(x,0) and node.getPlankPos(x) == 'T' and not node.isHoldingPlank():
            list.append(action(plankProblem.getElement(x,1), 'pickUp'))
        if node.getCurrentPos() == plankProblem.getElement(x,0) and node.getHoldingPlankSize() == plankProblem.getElement(x,2) and node.getPlankPos(x) == 'F':
            list.append(action(plankProblem.getElement(x,1), 'putDown'))

        # check reverse direction for possible moves
        if node.getCurrentPos() == plankProblem.getElement(x,1) and node.getPlankPos(x) == 'T':
            list.append(action(plankProblem.getElement(x,0), 'moveTo'))
        if node.getCurrentPos() == plankProblem.getElement(x,1) and node.getPlankPos(x) == 'T' and not node.isHoldingPlank():
            list.append(action(plankProblem.getElement(x,0), 'pickUp'))
        if node.getCurrentPos() == plankProblem.getElement(x,1) and node.getHoldingPlankSize() == plankProblem.getElement(x,2) and node.getPlankPos(x) == 'F':
            list.append(action(plankProblem.getElement(x,0), 'putDown'))
    return list

def result(plankProblem, Node, action):

    newNode = node(Node.getCurrentPos(),Node.getHoldingPlankSize(),Node.getPlankPosList())
    print(newNode)




    if action.getMovement() == 'moveTo':
        newNode.currentPos = action.getTarget()

    elif action.getMovement() == 'pickUp':
        for l in plankProblem.getElements():
            if l[0] == newNode.currentPos and l[1] == action.getTarget():
                index = plankProblem.getElements().index(l)
                newNode.updatePlankPosList(index, 'F')
                newNode.setHoldingPlankSize(l[2])

            # check reverse direction
            elif l[1] == newNode.currentPos and l[0] == action.getTarget():
                index = plankProblem.getElements().index(l)
                newNode.updatePlankPosList(index, 'F')
                newNode.setHoldingPlankSize(l[2])

    elif action.getMovement() == 'putDown':
        for l in plankProblem.getElements():
            if l[0] == newNode.currentPos and l[1] == action.getTarget():
                index = plankProblem.getElements().index(l)
                newNode.updatePlankPosList(index, 'T')
                newNode.setHoldingPlankSize('0')

            # check reverse direction
            elif l[1] == newNode.currentPos and l[0] == action.getTarget():
                index = plankProblem.getElements().index(l)
                newNode.updatePlankPosList(index, 'T')
                newNode.setHoldingPlankSize('0')

    print(newNode)


    return newNode



def expand(plankProblem, n):
    final = []
    lis = actions(n, plankProblem)
    for x in lis:

        temp = result(plankProblem,n,x)
        final.append(temp)
        print(final)


    return final






def main():
    p = plankProblem()
    n = node('START','0',['T','F','F','F','F','T','F','T','F','T'])
    a = action('F', 'moveTo')
    with open("plankproblem.txt") as f:
        reader = csv.reader(f, delimiter='\t')
        d = list(reader)
        p.addElement(d)

#    p.displayPlankProblem()
#    print(p.getLength())
#    print(actions(n,p))
#    print(result(p,n,a))
    expand(p,n)









if __name__ == "__main__": main()
