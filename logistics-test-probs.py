

##    initial_state = 'In(C1, R1) & In(C2, D1) & In(C3, D2) & In(R1, D1) & Holding(R1)'
    
logisticsPlan('In(C1, D1)')

logisticsPlan('In(C1,D2)')

logisticsPlan('In(C1, D1) & In(R1, D2)')
logisticsPlan('In(R1, D2) & In(C1, D1)')

logisticsPlan('In(C1, D1) & In(C3, R1)')
logisticsPlan('In(C1, D1) & In(C3, R1) & In(R1, D3)')

logisticsPlan('In(C1, D1) & In(R1, D3) & In(C3, R1)')
logisticsPlan('In(C1, D1) & In(C3, D3)')

logisticsPlan('In(C1, D1) & In(R1, D2) & In(C3, R1)')

logisticsPlan('In(C1, D1) & In(C3, R1) & In(R1, D3)')

logisticsPlan('In(C1, D1) & In(C2, D3)')


logisticsPlan('In(C3, D1)')

logisticsPlan('In(C2, D3)')

logisticsPlan('In(C3, D3)')


#no plans for these below
logisticsPlan('In(C2, D3) & In(C3, D3)')

logisticsPlan('In(C3, D3) & In(C2, D3)')

logisticsPlan('In(C1, D2) & In(C3, D3)')

logisticsPlan('In(C1, D3) & In(C2, D3) & In(C3, D3)')  ## homework??

logisticsPlan('In(C1, D2) & In(C3, D3) & In(C2, D1)')


#kaboom... didn't stop?
logisticsPlan('In(C1, D2) & In(C3, D3) & In(C2, D3) & In(R1, D1)')

