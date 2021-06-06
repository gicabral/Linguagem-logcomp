
def logcomp(x){
    if (x < 2) :
        return x
    endif else :
        return logcomp(x-1) + logcomp(x-1)
    endelse
}     

a = 7
b = 0
while (b < a): 
    print(logcomp(b))
    b = b+1
endwhile