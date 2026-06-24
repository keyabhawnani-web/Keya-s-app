import plotly.graph_objects as go

# Moving Averages
data["MA50"] = data["Close"].rolling(window=50).mean()
data["MA200"] = data["Close"].rolling(window=200).mean()

st.subheader("📊 Interactive Stock Analysis")

fig = go.Figure()

# Candlestick Chart
fig.add_trace(
    go.Candlestick(
        x=data.index,
        open=data["Open"],
        high=data["High"],
        low=data["Low"],
        close=data["Close"],
        name="Price"
    )
)

# 50-Day MA
fig.add_trace(
    go.Scatter(
        x=data.index,
        y=data["MA50"],
        mode="lines",
        name="50-Day MA"
    )
)

# 200-Day MA
fig.add_trace(
    go.Scatter(
        x=data.index,
        y=data["MA200"],
        mode="lines",
        name="200-Day MA"
    )
)

fig.update_layout(
    title="Stock Price with Moving Averages",
    xaxis_title="Date",
    yaxis_title="Price",
    xaxis_rangeslider_visible=False,
    height=700
)

st.plotly_chart(fig, use_container_width=True)
