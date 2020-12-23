from datetime import datetime
import numpy as np
import talib
import alpaca_trade_api as tradeapi

apiKey = "AK0NH0Q7BUUANZ2E2GKL"
secretKey = "v1pokxWFX12BRujjOomxmownZnWE0e6eIcxtndfR"
realEndpoint = "https://api.alpaca.markets"

paperEndpoint = "https://paper-api.alpaca.markets"
paperKey = "PKW2JHY75SLSKA1VUX74"
paperSecret = "mS59yaHEGv5CyBFmaGqrmziRRkF14ioEWS8ENmGG"

api = tradeapi.REST(key_id=paperKey,secret_key=paperSecret, base_url=paperEndpoint, api_version='v2')

barTimeframe = "15Min" # 1Min, 5Min, 15Min, 1H, 1D
assetsToTrade = ["SPY","MSFT","AAPL","NFLX"]
positionSizing = 0.25

# Tracks position in list of symbols to download
iteratorPos = 0 
assetListLen = len(assetsToTrade)

returned = api.submit_order("SPY",100,"buy","market","gtc") # Market order to open position
print(returned)

# while iteratorPos < assetListLen:
# 	symbol = assetsToTrade[iteratorPos]
	
# 	returned_data = api.get_barset(symbol,barTimeframe,1)
# 	print(returned_data)
# 	timeList = []
# 	openList = []
# 	highList = []
# 	lowList = []
# 	closeList = []
# 	volumeList = []

# 	# Reads, formats and stores the new bars
# 	for bar in returned_data[assetsToTrade[iteratorPos]]:
# 		print(bar)
# 		#timeList.append(datetime.strptime(bar[1].t,'%Y-%m-%dT%H:%M:%SZ'))
# 		openList.append(bar.o)
# 		highList.append(bar.h)
# 		lowList.append(bar.l)
# 		closeList.append(bar.c)
# 		volumeList.append(bar.v)
	
# 	# Processes all data into numpy arrays for use by talib
# 	timeList = np.array(timeList)
# 	openList = np.array(openList,dtype=np.float64)
# 	highList = np.array(highList,dtype=np.float64)
# 	lowList = np.array(lowList,dtype=np.float64)
# 	closeList = np.array(closeList,dtype=np.float64)
# 	volumeList = np.array(volumeList,dtype=np.float64)

# 	# Calculated trading indicators
# 	SMA20 = talib.SMA(closeList,20)[-1]
# 	SMA50 = talib.SMA(closeList,50)[-1]

# 	openPosition = None
	
# 	# Calculates the trading signals
# 	if SMA20 > SMA50:
# 		openPosition = api.get_position(symbol)
		
# 		# Opens new position if one does not exist
# 		if openPosition == 0:
# 			cashBalance = api.get_account().cash
		
# 			targetPositionSize = cashBalance / (price / positionSizing) # Calculates required position size
			
# 			returned = api.submit_order(symbol,targetPositionSize,"buy","market","gtc") # Market order to open position
# 			print(returned)
		
# 	else:
# 		# Closes position if SMA20 is below SMA50
# 		if openPosition != None:
# 			openPosition = api.get_position(symbol)
			
# 			returned = api.submit_order(symbol,openPosition,"sell","market","gtc") # Market order to fully close position
# 			print(returned)
	
# 	iteratorPos += 1