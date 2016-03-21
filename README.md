# adidas-original-price-monitor

## how to use
- config the settings, fill with your sender email, code, receive email, then it's ok to go.
- s15220, s15228 are the article number, support unlimited nums, thanks to [click](http://click.pocoo.org/6/).
- default expected price is ¥800,
- when the price of the article number that you just input, is undering expected price, you will got email notification.

## Example:
``` 
(envpython3)➜  adidas price monitor  python3 adidas_orginal_price_monitor.py s15220 s15228
expected_price [800]:900
630.0
(envpython3)➜  adidas price monitor
```
