掘金小册(微信登陆): https://juejin.im/book/6844733722936377351/section/6844733722919452686

# protobuf
传输使用一系列的键值对，如果连续的键重复了，那说明传输的值是一个列表.

## key=tag||type
tag和type都用整数来标识, 因此可以使用varint编码
    
## value
### 整数
使用 zigzag 编码, 支持负数值





