requiredKing = 1
requiredQueen = 1
requiredRook = 2
requiredBishop = 2
requiredKnight = 2
requiredPawn = 8

kings, queens, rooks, bishops, knights, pawns = map(int, input().split())

print(requiredKing - kings, requiredQueen - queens, requiredRook - rooks, 
      requiredBishop - bishops, requiredKnight - knights, requiredPawn - pawns)