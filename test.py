import RSI
import Bull_Market_Data
import Bear_Market_Data

trades = []
Bull_Data = Bull_Market_Data.set_2()
Bear_Data = Bear_Market_Data.set_1()
data = Bull_Data

#indicators
ma_out = data["price"].rolling(10).mean()
rsi_out = RSI.rsi(data, 10, True)

#strategy for rsi
trade_running = False #so you dont double trade
for x in range(len(rsi_out)): #go through rsi to find below 30
    print(str(rsi_out[x]) + " " + str(data["price"][x]))
    strategy = {"open_trade": 0, "close_trade": 0, "stop_loss": 1000, "take_profit": 3000}
    if(rsi_out[x]>30):
        trade_running = False
    if(rsi_out[x]<=30 and trade_running == False):
        strategy["open_trade"] = data["price"][x]
        trade_running = True
        for y in range(x, len(data["price"])): #go through prices from index when rsi below 30 to find close trade
            if(data["price"][y] <= strategy["open_trade"]-strategy["stop_loss"] or data["price"][y] >= strategy["open_trade"]+strategy["take_profit"] ):
                strategy["close_trade"] = data["price"][y]
                trades.append(strategy)
                break

#summary of trades
total = 0
efficiency = 0
print("\n")
for trade in trades:
    if(trade["close_trade"] - trade["open_trade"] > 0):
        efficiency += 1
    total += (trade["close_trade"] - trade["open_trade"])/trade["open_trade"]
    print(str(trade["close_trade"]) + " - " + str(trade["open_trade"]) +" = "+str((trade["close_trade"] - trade["open_trade"])/trade["open_trade"])+"%")
print("\nTotal: "+str(total)+"%")


if(len(trades) == 0):
    print("Efficiency: 0%")
else:
    print("Efficiency: " + str((efficiency*100)/len(trades)) +"%")



