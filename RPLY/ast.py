from symboltable import IdentSymbol, FuncSymbol, SymbolTable

#Special/specific nodes

class Number():
    def __init__(self, value):
        self.value = value
    def eval(self, st):
        return int(self.value)

class ArgList():
    #Recebe NAMES
    def __init__(self, firstborn):
        self.childs = [firstborn]
    def addChild(self, child):
        self.childs.append(child)
    def getArgs(self):
        return self.childs

class Program(): 
    def __init__(self, firstborn):
        self.childs = [firstborn]

    def addChild(self, child):
        self.childs.append(child)
    def eval(self, st):
        for child in self.childs:
            if type(child) == ReturnNode:
                raise Exception("Return fora de uma func")
            child.eval(st)

class Block(): 
    def __init__(self, firstborn):
        self.childs = [firstborn]

    def addChild(self, child):
        self.childs.append(child)
    def eval(self, st):
        for child in self.childs:
            if type(child) == ReturnNode:
                return child
            result = child.eval(st)
            if(type(result) == ReturnNode):
                return result

class Ident():
    def __init__(self, name):
        self.name = name
    def eval(self, st):
        return st.getSymbol(self.name).value



class FuncDef():
    def __init__(self, name, argList, block):
        self.name = name
        self.argList = argList
        self.block = block
    def eval(self, st):
        func = FuncSymbol(self.name, self.argList, self.block)
        st.setSymbol(func)

class FuncCall():
    def __init__(self, name, argList):
        self.name = name
        self.argList = argList
    def eval(self, st):
        func = st.getSymbol(self.name) #get function definition
        if(len(self.argList) != len(func.argList)): #check if has same arglen
            raise Exception(f"{self.name} receives {len(self.argList)} arguments but {func.argList} were given")
        
        funcSt = SymbolTable(self.name, st) #create local scope

        for i in range(len(func.argList)):  #copy args for local scope
            #                   Arg name       , arg value
            symb = IdentSymbol(func.argList[i],self.argList[i].eval(st))
            funcSt.setSymbol(symb)
        
        result = func.block.eval(funcSt) #run funcblock with local scope
        
        if(not result is None): 
            return result.eval(funcSt)



class WhileNode():
    def __init__(self, condition, block):
        self.condition = condition
        self.block = block
    def eval(self,st):
        result = None
        while(self.condition.eval(st)):
            result = self.block.eval(st)
            if type(result) == ReturnNode:
                return result

class IfNode():
    def __init__(self, condition, block_true, block_false = None):
        self.condition = condition
        self.block_true = block_true
        self.block_false = block_false
    def eval(self,st):
        result = None
        if(self.condition.eval(st)):
            result = self.block_true.eval(st)
        elif(not (self.block_false) is None):
            result = self.block_false.eval(st)
        if type(result) == ReturnNode:
            return result
        

#Base nodes
class UnOp():
    def __init__(self, child):
        self.child = child

class BinOp():
    def __init__(self, left, right):
        self.left = left
        self.right = right

#Binops

class Sum(BinOp):
    def eval(self,st):
        return int(self.left.eval(st) + self.right.eval(st))

class Sub(BinOp):
    def eval(self,st):
        return int(self.left.eval(st) - self.right.eval(st))

class Div(BinOp):
    def eval(self,st):
        return int(self.left.eval(st) // self.right.eval(st))

class Mult(BinOp):
    def eval(self,st):
        return int(self.left.eval(st) * self.right.eval(st))

class PowNode(BinOp):
    def eval(self,st):
        return int(self.left.eval(st) ** self.right.eval(st))

class Equal(BinOp):
    def eval(self,st):
        return int(self.left.eval(st) == self.right.eval(st))

class Greater(BinOp):
    def eval(self,st):
        return int(self.left.eval(st) > self.right.eval(st))

class Less(BinOp):
    def eval(self,st):
        return int(self.left.eval(st) < self.right.eval(st))

class Or(BinOp):
    def eval(self,st):
        return int(self.left.eval(st) or self.right.eval(st))

class And(BinOp):
    def eval(self,st):
        return int(self.left.eval(st) and self.right.eval(st))

class Assign(BinOp):
    def eval(self, st):
        symbol = IdentSymbol(self.left, self.right.eval(st))
        st.setSymbol(symbol)



#UNOP 

class Print(UnOp):
    def eval(self, st):
        print(self.child.eval(st))

class Invert(UnOp):
    def eval(self,st):
        return -int(self.child.eval(st))

class Negate(UnOp):
    def eval(self,st):
        return int(not self.child.eval(st))

class Positive(UnOp):
    def eval(self,st):
        return +int(self.child.eval(st))

class ReturnNode(UnOp):
    def eval(self,st):
        return self.child.eval(st)

class NoOp():
    def eval(self, st):
        pass