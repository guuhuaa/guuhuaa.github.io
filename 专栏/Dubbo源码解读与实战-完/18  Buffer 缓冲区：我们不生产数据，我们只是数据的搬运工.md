<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>18  Buffer 缓冲区：我们不生产数据，我们只是数据的搬运工.md</title>
        <!-- Spectre.css framework -->
        <link rel="stylesheet" href="../../static/index.css">
        <!-- theme css & js -->
        <meta name="generator" content="Hexo 4.2.0">
    </head>

<body>

<div class="book-container">
    <div class="book-sidebar">
        <div class="book-brand">
            <a href="../../index.html">
                <img src="../../static/favicon.png">
                <span>技术文章摘抄</span>
            </a>
        </div>
        <div class="book-menu uncollapsible">
            <ul class="uncollapsible">
                <li><a href="../../index.html" class="current-tab">首页</a></li>
            </ul>

            <ul class="uncollapsible">
                <li><a href="../index.html">上一级</a></li>
            </ul>

            <ul class="uncollapsible">
                <li>

                    
                    <a href="00&#32;开篇词&#32;&#32;深入掌握&#32;Dubbo&#32;原理与实现，提升你的职场竞争力.md">00 开篇词  深入掌握 Dubbo 原理与实现，提升你的职场竞争力.md</a>

                </li>
                <li>

                    
                    <a href="01&#32;&#32;Dubbo&#32;源码环境搭建：千里之行，始于足下.md">01  Dubbo 源码环境搭建：千里之行，始于足下.md</a>

                </li>
                <li>

                    
                    <a href="02&#32;Dubbo&#32;的配置总线：抓住&#32;URL，就理解了半个&#32;Dubbo.md">02 Dubbo 的配置总线：抓住 URL，就理解了半个 Dubbo.md</a>

                </li>
                <li>

                    
                    <a href="03&#32;&#32;Dubbo&#32;SPI&#32;精析，接口实现两极反转（上）.md">03  Dubbo SPI 精析，接口实现两极反转（上）.md</a>

                </li>
                <li>

                    
                    <a href="04&#32;&#32;Dubbo&#32;SPI&#32;精析，接口实现两极反转（下）.md">04  Dubbo SPI 精析，接口实现两极反转（下）.md</a>

                </li>
                <li>

                    
                    <a href="05&#32;&#32;海量定时任务，一个时间轮搞定.md">05  海量定时任务，一个时间轮搞定.md</a>

                </li>
                <li>

                    
                    <a href="06&#32;&#32;ZooKeeper&#32;与&#32;Curator，求你别用&#32;ZkClient&#32;了（上）.md">06  ZooKeeper 与 Curator，求你别用 ZkClient 了（上）.md</a>

                </li>
                <li>

                    
                    <a href="07&#32;&#32;ZooKeeper&#32;与&#32;Curator，求你别用&#32;ZkClient&#32;了（下）.md">07  ZooKeeper 与 Curator，求你别用 ZkClient 了（下）.md</a>

                </li>
                <li>

                    
                    <a href="08&#32;&#32;代理模式与常见实现.md">08  代理模式与常见实现.md</a>

                </li>
                <li>

                    
                    <a href="09&#32;&#32;Netty&#32;入门，用它做网络编程都说好（上）.md">09  Netty 入门，用它做网络编程都说好（上）.md</a>

                </li>
                <li>

                    
                    <a href="10&#32;&#32;Netty&#32;入门，用它做网络编程都说好（下）.md">10  Netty 入门，用它做网络编程都说好（下）.md</a>

                </li>
                <li>

                    
                    <a href="11&#32;&#32;简易版&#32;RPC&#32;框架实现（上）.md">11  简易版 RPC 框架实现（上）.md</a>

                </li>
                <li>

                    
                    <a href="12&#32;&#32;简易版&#32;RPC&#32;框架实现（下）.md">12  简易版 RPC 框架实现（下）.md</a>

                </li>
                <li>

                    
                    <a href="13&#32;&#32;本地缓存：降低&#32;ZooKeeper&#32;压力的一个常用手段.md">13  本地缓存：降低 ZooKeeper 压力的一个常用手段.md</a>

                </li>
                <li>

                    
                    <a href="14&#32;&#32;重试机制是网络操作的基本保证.md">14  重试机制是网络操作的基本保证.md</a>

                </li>
                <li>

                    
                    <a href="15&#32;&#32;ZooKeeper&#32;注册中心实现，官方推荐注册中心实践.md">15  ZooKeeper 注册中心实现，官方推荐注册中心实践.md</a>

                </li>
                <li>

                    
                    <a href="16&#32;&#32;Dubbo&#32;Serialize&#32;层：多种序列化算法，总有一款适合你.md">16  Dubbo Serialize 层：多种序列化算法，总有一款适合你.md</a>

                </li>
                <li>

                    
                    <a href="17&#32;&#32;Dubbo&#32;Remoting&#32;层核心接口分析：这居然是一套兼容所有&#32;NIO&#32;框架的设计？.md">17  Dubbo Remoting 层核心接口分析：这居然是一套兼容所有 NIO 框架的设计？.md</a>

                </li>
                <li>

                    <a class="current-tab" href="18&#32;&#32;Buffer&#32;缓冲区：我们不生产数据，我们只是数据的搬运工.md">18  Buffer 缓冲区：我们不生产数据，我们只是数据的搬运工.md</a>
                    

                </li>
                <li>

                    
                    <a href="19&#32;&#32;Transporter&#32;层核心实现：编解码与线程模型一文打尽（上）.md">19  Transporter 层核心实现：编解码与线程模型一文打尽（上）.md</a>

                </li>
                <li>

                    
                    <a href="20&#32;&#32;Transporter&#32;层核心实现：编解码与线程模型一文打尽（下）.md">20  Transporter 层核心实现：编解码与线程模型一文打尽（下）.md</a>

                </li>
                <li>

                    
                    <a href="21&#32;&#32;Exchange&#32;层剖析：彻底搞懂&#32;Request-Response&#32;模型（上）.md">21  Exchange 层剖析：彻底搞懂 Request-Response 模型（上）.md</a>

                </li>
                <li>

                    
                    <a href="22&#32;&#32;Exchange&#32;层剖析：彻底搞懂&#32;Request-Response&#32;模型（下）.md">22  Exchange 层剖析：彻底搞懂 Request-Response 模型（下）.md</a>

                </li>
                <li>

                    
                    <a href="23&#32;&#32;核心接口介绍，RPC&#32;层骨架梳理.md">23  核心接口介绍，RPC 层骨架梳理.md</a>

                </li>
                <li>

                    
                    <a href="24&#32;&#32;从&#32;Protocol&#32;起手，看服务暴露和服务引用的全流程（上）.md">24  从 Protocol 起手，看服务暴露和服务引用的全流程（上）.md</a>

                </li>
                <li>

                    
                    <a href="25&#32;&#32;从&#32;Protocol&#32;起手，看服务暴露和服务引用的全流程（下）.md">25  从 Protocol 起手，看服务暴露和服务引用的全流程（下）.md</a>

                </li>
                <li>

                    
                    <a href="26&#32;&#32;加餐：直击&#32;Dubbo&#32;“心脏”，带你一起探秘&#32;Invoker（上）.md">26  加餐：直击 Dubbo “心脏”，带你一起探秘 Invoker（上）.md</a>

                </li>
                <li>

                    
                    <a href="27&#32;&#32;加餐：直击&#32;Dubbo&#32;“心脏”，带你一起探秘&#32;Invoker（下）.md">27  加餐：直击 Dubbo “心脏”，带你一起探秘 Invoker（下）.md</a>

                </li>
                <li>

                    
                    <a href="28&#32;&#32;复杂问题简单化，代理帮你隐藏了多少底层细节？.md">28  复杂问题简单化，代理帮你隐藏了多少底层细节？.md</a>

                </li>
                <li>

                    
                    <a href="https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/Dubbo%E6%BA%90%E7%A0%81%E8%A7%A3%E8%AF%BB%E4%B8%8E%E5%AE%9E%E6%88%98-%E5%AE%8C/29%20%20%E5%8A%A0%E9%A4%90%EF%BC%9AHTTP%20%E5%8D%8F%E8%AE%AE%20+%20JSON-RPC%EF%BC%8CDubbo%20%E8%B7%A8%E8%AF%AD%E8%A8%80%E5%B0%B1%E6%98%AF%E5%A6%82%E6%AD%A4%E7%AE%80%E5%8D%95.md">29  加餐：HTTP 协议 + JSON-RPC，Dubbo 跨语言就是如此简单.md</a>

                </li>
                <li>

                    
                    <a href="30&#32;&#32;Filter&#32;接口，扩展&#32;Dubbo&#32;框架的常用手段指北.md">30  Filter 接口，扩展 Dubbo 框架的常用手段指北.md</a>

                </li>
                <li>

                    
                    <a href="31&#32;&#32;加餐：深潜&#32;Directory&#32;实现，探秘服务目录玄机.md">31  加餐：深潜 Directory 实现，探秘服务目录玄机.md</a>

                </li>
                <li>

                    
                    <a href="32&#32;&#32;路由机制：请求到底怎么走，它说了算（上）.md">32  路由机制：请求到底怎么走，它说了算（上）.md</a>

                </li>
                <li>

                    
                    <a href="33&#32;&#32;路由机制：请求到底怎么走，它说了算（下）.md">33  路由机制：请求到底怎么走，它说了算（下）.md</a>

                </li>
                <li>

                    
                    <a href="34&#32;&#32;加餐：初探&#32;Dubbo&#32;动态配置的那些事儿.md">34  加餐：初探 Dubbo 动态配置的那些事儿.md</a>

                </li>
                <li>

                    
                    <a href="35&#32;&#32;负载均衡：公平公正物尽其用的负载均衡策略，这里都有（上）.md">35  负载均衡：公平公正物尽其用的负载均衡策略，这里都有（上）.md</a>

                </li>
                <li>

                    
                    <a href="36&#32;&#32;负载均衡：公平公正物尽其用的负载均衡策略，这里都有（下）.md">36  负载均衡：公平公正物尽其用的负载均衡策略，这里都有（下）.md</a>

                </li>
                <li>

                    
                    <a href="37&#32;&#32;集群容错：一个好汉三个帮（上）.md">37  集群容错：一个好汉三个帮（上）.md</a>

                </li>
                <li>

                    
                    <a href="38&#32;&#32;集群容错：一个好汉三个帮（下）.md">38  集群容错：一个好汉三个帮（下）.md</a>

                </li>
                <li>

                    
                    <a href="39&#32;&#32;加餐：多个返回值不用怕，Merger&#32;合并器来帮忙.md">39  加餐：多个返回值不用怕，Merger 合并器来帮忙.md</a>

                </li>
                <li>

                    
                    <a href="40&#32;&#32;加餐：模拟远程调用，Mock&#32;机制帮你搞定.md">40  加餐：模拟远程调用，Mock 机制帮你搞定.md</a>

                </li>
                <li>

                    
                    <a href="41&#32;&#32;加餐：一键通关服务发布全流程.md">41  加餐：一键通关服务发布全流程.md</a>

                </li>
                <li>

                    
                    <a href="42&#32;&#32;加餐：服务引用流程全解析.md">42  加餐：服务引用流程全解析.md</a>

                </li>
                <li>

                    
                    <a href="43&#32;&#32;服务自省设计方案：新版本新方案.md">43  服务自省设计方案：新版本新方案.md</a>

                </li>
                <li>

                    
                    <a href="44&#32;&#32;元数据方案深度剖析，如何避免注册中心数据量膨胀？.md">44  元数据方案深度剖析，如何避免注册中心数据量膨胀？.md</a>

                </li>
                <li>

                    
                    <a href="45&#32;&#32;加餐：深入服务自省方案中的服务发布订阅（上）.md">45  加餐：深入服务自省方案中的服务发布订阅（上）.md</a>

                </li>
                <li>

                    
                    <a href="46&#32;&#32;加餐：深入服务自省方案中的服务发布订阅（下）.md">46  加餐：深入服务自省方案中的服务发布订阅（下）.md</a>

                </li>
                <li>

                    
                    <a href="47&#32;&#32;配置中心设计与实现：集中化配置&#32;and&#32;本地化配置，我都要（上）.md">47  配置中心设计与实现：集中化配置 and 本地化配置，我都要（上）.md</a>

                </li>
                <li>

                    
                    <a href="48&#32;&#32;配置中心设计与实现：集中化配置&#32;and&#32;本地化配置，我都要（下）.md">48  配置中心设计与实现：集中化配置 and 本地化配置，我都要（下）.md</a>

                </li>
                <li>

                    
                    <a href="49&#32;结束语&#32;&#32;认真学习，缩小差距.md">49 结束语  认真学习，缩小差距.md</a>

                </li>
            </ul>

        </div>
    </div>

    <div class="sidebar-toggle" onclick="sidebar_toggle()" onmouseover="add_inner()" onmouseleave="remove_inner()">
        <div class="sidebar-toggle-inner"></div>
    </div>

    <script>
        function add_inner() {
            let inner = document.querySelector('.sidebar-toggle-inner')
            inner.classList.add('show')
        }

        function remove_inner() {
            let inner = document.querySelector('.sidebar-toggle-inner')
            inner.classList.remove('show')
        }

        function sidebar_toggle() {
            let sidebar_toggle = document.querySelector('.sidebar-toggle')
            let sidebar = document.querySelector('.book-sidebar')
            let content = document.querySelector('.off-canvas-content')
            if (sidebar_toggle.classList.contains('extend')) { // show
                sidebar_toggle.classList.remove('extend')
                sidebar.classList.remove('hide')
                content.classList.remove('extend')
            } else { // hide
                sidebar_toggle.classList.add('extend')
                sidebar.classList.add('hide')
                content.classList.add('extend')
            }
        }
    </script>

    <div class="off-canvas-content">
        <div class="columns">
            <div class="column col-12 col-lg-12">
                <div class="book-navbar">
                    <!-- For Responsive Layout -->
                    <header class="navbar">
                        <section class="navbar-section">
                            <a onclick="open_sidebar()">
                                <i class="icon icon-menu"></i>
                            </a>
                        </section>
                    </header>
                </div>
                <div class="book-content" style="max-width: 960px; margin: 0 auto;
    overflow-x: auto;
    overflow-y: hidden;">
                    <div class="book-post">
                        <p id="tip" align="center"></p>
                        <div><h1>18  Buffer 缓冲区：我们不生产数据，我们只是数据的搬运工</h1>
<p>Buffer 是一种字节容器，在 Netty 等 NIO 框架中都有类似的设计，例如，Java NIO 中的ByteBuffer、Netty4 中的 ByteBuf。Dubbo 抽象出了 ChannelBuffer 接口对底层 NIO 框架中的 Buffer 设计进行统一，其子类如下图所示：</p>
<p><img src="assets/CgqCHl9pudyACkPPAABei6G8kSc033.png" alt="Drawing 0.png" /></p>
<p>ChannelBuffer 继承关系图</p>
<p>下面我们就按照 ChannelBuffer 的继承结构，从顶层的 ChannelBuffer 接口开始，逐个向下介绍，直至最底层的各个实现类。</p>
<h3>ChannelBuffer 接口</h3>
<p><strong>ChannelBuffer 接口</strong>的设计与 Netty4 中 ByteBuf 抽象类的设计基本一致，也有 readerIndex 和 writerIndex 指针的概念，如下所示，它们的核心方法也是如出一辙。</p>
<ul>
<li>getBytes()、setBytes() 方法：从参数指定的位置读、写当前 ChannelBuffer，不会修改 readerIndex 和 writerIndex 指针的位置。</li>
<li>readBytes() 、writeBytes() 方法：也是读、写当前 ChannelBuffer，但是 readBytes() 方法会从 readerIndex 指针开始读取数据，并移动 readerIndex 指针；writeBytes() 方法会从 writerIndex 指针位置开始写入数据，并移动 writerIndex 指针。</li>
<li>markReaderIndex()、markWriterIndex() 方法：记录当前 readerIndex 指针和 writerIndex 指针的位置，一般会和 resetReaderIndex()、resetWriterIndex() 方法配套使用。resetReaderIndex() 方法会将 readerIndex 指针重置到 markReaderIndex() 方法标记的位置，resetwriterIndex() 方法同理。</li>
<li>capacity()、clear()、copy() 等辅助方法用来获取 ChannelBuffer 容量以及实现清理、拷贝数据的功能，这里不再赘述。</li>
<li>factory() 方法：该方法返回创建 ChannelBuffer 的工厂对象，ChannelBufferFactory 中定义了多个 getBuffer() 方法重载来创建 ChannelBuffer，如下图所示，这些 ChannelBufferFactory的实现都是单例的。</li>
</ul>
<p><img src="assets/Ciqc1F9pugWAMFoIAABVU01bqiI007.png" alt="Drawing 1.png" /></p>
<p>ChannelBufferFactory 继承关系图</p>
<p><strong>AbstractChannelBuffer 抽象类</strong>实现了 ChannelBuffer 接口的大部分方法，其核心是维护了以下四个索引。</p>
<ul>
<li>readerIndex、writerIndex（int 类型）：通过 readBytes() 方法及其重载读取数据时，会后移 readerIndex 索引；通过 writeBytes() 方法及其重载写入数据的时候，会后移 writerIndex 索引。</li>
<li>markedReaderIndex、markedWriterIndex（int 类型）：实现记录 readerIndex（writerIndex）以及回滚 readerIndex（writerIndex）的功能，前面我们已经介绍过markReaderIndex() 方法、resetReaderIndex() 方法以及 markWriterIndex() 方法、resetWriterIndex() 方法，你可以对比学习。</li>
</ul>
<p>AbstractChannelBuffer 中 readBytes() 和 writeBytes() 方法的各个重载最终会通过 getBytes() 方法和 setBytes() 方法实现数据的读写，这些方法在 AbstractChannelBuffer 子类中实现。下面以读写一个 byte 数组为例，进行介绍：</p>
<pre><code>public void readBytes(byte[] dst, int dstIndex, int length) {

    // 检测可读字节数是否足够

    checkReadableBytes(length);

    // 将readerIndex之后的length个字节数读取到dst数组中dstIndex~

    // dstIndex+length的位置

    getBytes(readerIndex, dst, dstIndex, length);

    // 将readerIndex后移length个字节

    readerIndex += length;

}

public void writeBytes(byte[] src, int srcIndex, int length) {

    // 将src数组中srcIndex~srcIndex+length的数据写入当前buffer中

    // writerIndex~writerIndex+length的位置

    setBytes(writerIndex, src, srcIndex, length);

    // 将writeIndex后移length个字节

    writerIndex += length;

}
</code></pre>
<h3>Buffer 各实现类解析</h3>
<p>了解了 ChannelBuffer 接口的核心方法以及 AbstractChannelBuffer 的公共实现之后，我们再来看 ChannelBuffer 的具体实现。</p>
<p><strong>HeapChannelBuffer 是基于字节数组的 ChannelBuffer 实现</strong>，我们可以看到其中有一个 array（byte[]数组）字段，它就是 HeapChannelBuffer 存储数据的地方。HeapChannelBuffer 的 setBytes() 以及 getBytes() 方法实现是调用 System.arraycopy() 方法完成数组操作的，具体实现如下：</p>
<pre><code>public void setBytes(int index, byte[] src, int srcIndex, int length) {

    System.arraycopy(src, srcIndex, array, index, length);

}

public void getBytes(int index, byte[] dst, int dstIndex, int length) {

    System.arraycopy(array, index, dst, dstIndex, length);

}
</code></pre>
<p>HeapChannelBuffer 对应的 ChannelBufferFactory 实现是 HeapChannelBufferFactory，其 getBuffer() 方法会通过 ChannelBuffers 这个工具类创建一个指定大小 HeapChannelBuffer 对象，下面简单介绍两个 getBuffer() 方法重载：</p>
<pre><code>@Override

public ChannelBuffer getBuffer(int capacity) {

    // 新建一个HeapChannelBuffer，底层的会新建一个长度为capacity的byte数组

    return ChannelBuffers.buffer(capacity); 

}

@Override

public ChannelBuffer getBuffer(byte[] array, int offset, int length) {

    // 新建一个HeapChannelBuffer，并且会拷贝array数组中offset~offset+lenght

    // 的数据到新HeapChannelBuffer中

    return ChannelBuffers.wrappedBuffer(array, offset, length);

}
</code></pre>
<p>其他 getBuffer() 方法重载这里就不再展示，你若感兴趣的话可以参考源码进行学习。
<strong>DynamicChannelBuffer 可以认为是其他 ChannelBuffer 的装饰器，它可以为其他 ChannelBuffer 添加动态扩展容量的功能</strong>。DynamicChannelBuffer 中有两个核心字段：</p>
<ul>
<li>buffer（ChannelBuffer 类型），是被修饰的 ChannelBuffer，默认为 HeapChannelBuffer。</li>
<li>factory（ChannelBufferFactory 类型），用于创建被修饰的 HeapChannelBuffer 对象的 ChannelBufferFactory 工厂，默认为 HeapChannelBufferFactory。</li>
</ul>
<p>DynamicChannelBuffer 需要关注的是 ensureWritableBytes() 方法，该方法实现了动态扩容的功能，在每次写入数据之前，都需要调用该方法确定当前可用空间是否足够，调用位置如下图所示：</p>
<p><img src="assets/CgqCHl9puiWABaDpAACaisslR0Q430.png" alt="Drawing 2.png" /></p>
<p>ensureWritableBytes() 方法如果检测到底层 ChannelBuffer 对象的空间不足，则会创建一个新的 ChannelBuffer（空间扩大为原来的两倍），然后将原来 ChannelBuffer 中的数据拷贝到新 ChannelBuffer 中，最后将 buffer 字段指向新 ChannelBuffer 对象，完成整个扩容操作。ensureWritableBytes() 方法的具体实现如下：</p>
<pre><code>public void ensureWritableBytes(int minWritableBytes) {

    if (minWritableBytes &lt;= writableBytes()) {

        return;

    }

    int newCapacity;

    if (capacity() == 0) {

        newCapacity = 1;

    } else {

        newCapacity = capacity();

    }

    int minNewCapacity = writerIndex() + minWritableBytes;

    while (newCapacity &lt; minNewCapacity) {

        newCapacity &lt;&lt;= 1;

    }

    ChannelBuffer newBuffer = factory().getBuffer(newCapacity);

    newBuffer.writeBytes(buffer, 0, writerIndex());

    buffer = newBuffer;

}
</code></pre>
<p><strong>ByteBufferBackedChannelBuffer 是基于 Java NIO 中 ByteBuffer 的 ChannelBuffer 实现</strong>，其中的方法基本都是通过组合 ByteBuffer 的 API 实现的。下面以 getBytes() 方法和 setBytes() 方法的一个重载为例，进行分析：</p>
<pre><code>public void getBytes(int index, byte[] dst, int dstIndex, int length) {

    ByteBuffer data = buffer.duplicate();

    try {

        // 移动ByteBuffer中的指针

        data.limit(index + length).position(index);

    } catch (IllegalArgumentException e) {

        throw new IndexOutOfBoundsException();

    }

    // 通过ByteBuffer的get()方法实现读取

    data.get(dst, dstIndex, length);

}

public void setBytes(int index, byte[] src, int srcIndex, int length) {

    ByteBuffer data = buffer.duplicate();

    // 移动ByteBuffer中的指针

    data.limit(index + length).position(index);

    // 将数据写入底层的ByteBuffer中

    data.put(src, srcIndex, length);

}
</code></pre>
<p>ByteBufferBackedChannelBuffer 的其他方法实现比较简单，这里就不再展示，你若感兴趣的话可以参考源码进行学习。</p>
<p><strong>NettyBackedChannelBuffer 是基于 Netty 中 ByteBuf 的 ChannelBuffer 实现</strong>，Netty 中的 ByteBuf 内部维护了 readerIndex 和 writerIndex 以及 markedReaderIndex、markedWriterIndex 这四个索引，所以 NettyBackedChannelBuffer 没有再继承 AbstractChannelBuffer 抽象类，而是直接实现了 ChannelBuffer 接口。</p>
<p>NettyBackedChannelBuffer 对 ChannelBuffer 接口的实现都是调用底层封装的 Netty ByteBuf 实现的，这里就不再展开介绍，你若感兴趣的话也可以参考相关代码进行学习。</p>
<h3>相关 Stream 以及门面类</h3>
<p>在 ChannelBuffer 基础上，Dubbo 提供了一套输入输出流，如下图所示：</p>
<p><img src="assets/Ciqc1F9puj2AXLalAALcfencKx0331.png" alt="Drawing 3.png" /></p>
<p>ChannelBufferInputStream 底层封装了一个 ChannelBuffer，其实现 InputStream 接口的 read*() 方法全部都是从 ChannelBuffer 中读取数据。ChannelBufferInputStream 中还维护了一个 startIndex 和一个endIndex 索引，作为读取数据的起止位置。ChannelBufferOutputStream 与 ChannelBufferInputStream 类似，会向底层的 ChannelBuffer 写入数据，这里就不再展开，你若感兴趣的话可以参考源码进行分析。</p>
<p>最后要介绍 ChannelBuffers 这个<strong>门面类</strong>，下图展示了 ChannelBuffers 这个门面类的所有方法：</p>
<p><img src="assets/CgqCHl9pukOAT_8kAACo0xRQ2po574.png" alt="Drawing 4.png" /></p>
<p>对这些方法进行分类，可归纳出如下这些方法。</p>
<ul>
<li>dynamicBuffer() 方法：创建 DynamicChannelBuffer 对象，初始化大小由第一个参数指定，默认为 256。</li>
<li>buffer() 方法：创建指定大小的 HeapChannelBuffer 对象。</li>
<li>wrappedBuffer() 方法：将传入的 byte[] 数字封装成 HeapChannelBuffer 对象。</li>
<li>directBuffer() 方法：创建 ByteBufferBackedChannelBuffer 对象，需要注意的是，底层的 ByteBuffer 使用的堆外内存，需要特别关注堆外内存的管理。</li>
<li>equals() 方法：用于比较两个 ChannelBuffer 是否相同，其中会逐个比较两个 ChannelBuffer 中的前 7 个可读字节，只有两者完全一致，才算两个 ChannelBuffer 相同。其核心实现如下示例代码：</li>
</ul>
<pre><code>public static boolean equals(ChannelBuffer bufferA, ChannelBuffer bufferB) {

    final int aLen = bufferA.readableBytes();

    if (aLen != bufferB.readableBytes()) { 

        return false; // 比较两个ChannelBuffer的可读字节数

    }

    final int byteCount = aLen &amp; 7; // 只比较前7个字节

    int aIndex = bufferA.readerIndex();

    int bIndex = bufferB.readerIndex();

    for (int i = byteCount; i &gt; 0; i--) {

        if (bufferA.getByte(aIndex) != bufferB.getByte(bIndex)) {

            return false; // 前7个字节发现不同，则返回false

        }

        aIndex++;

        bIndex++;

    }

    return true;

}
</code></pre>
<ul>
<li>compare() 方法：用于比较两个 ChannelBuffer 的大小，会逐个比较两个 ChannelBuffer 中的全部可读字节，具体实现与 equals() 方法类似，这里就不再重复讲述。</li>
</ul>
<h3>总结</h3>
<p>本课时重点介绍了 dubbo-remoting 模块 buffers 包中的核心实现。我们首先介绍了 ChannelBuffer 接口这一个顶层接口，了解了 ChannelBuffer 提供的核心功能和运作原理；接下来介绍了 ChannelBuffer 的多种实现，其中包括 HeapChannelBuffer、DynamicChannelBuffer、ByteBufferBackedChannelBuffer 等具体实现类，以及 AbstractChannelBuffer 这个抽象类；最后分析了 ChannelBufferFactory 使用到的 ChannelBuffers 工具类以及在 ChannelBuffer 之上封装的 InputStream 和 OutputStream 实现。</p>
<p>关于本课时，你若还有什么疑问或想法，欢迎你留言跟我分享。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="17&#32;&#32;Dubbo&#32;Remoting&#32;层核心接口分析：这居然是一套兼容所有&#32;NIO&#32;框架的设计？.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="19&#32;&#32;Transporter&#32;层核心实现：编解码与线程模型一文打尽（上）.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b433f4c9be970ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
</body>
<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-NPSEEVD756"></script>
<script>
    window.dataLayer = window.dataLayer || [];

    function gtag() {
        dataLayer.push(arguments);
    }

    gtag('js', new Date());
    gtag('config', 'G-NPSEEVD756');
    var path = window.location.pathname
    var cookie = getCookie("lastPath");
    console.log(path)
    if (path.replace("/", "") === "") {
        if (cookie.replace("/", "") !== "") {
            console.log(cookie)
            document.getElementById("tip").innerHTML = "<a href='https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/Dubbo%E6%BA%90%E7%A0%81%E8%A7%A3%E8%AF%BB%E4%B8%8E%E5%AE%9E%E6%88%98-%E5%AE%8C/&quot;&#32;+&#32;cookie&#32;+&#32;&quot;'>跳转到上次进度</a>"
        }
    } else {
        setCookie("lastPath", path)
    }

    function setCookie(cname, cvalue) {
        var d = new Date();
        d.setTime(d.getTime() + (180 * 24 * 60 * 60 * 1000));
        var expires = "expires=" + d.toGMTString();
        document.cookie = cname + "=" + cvalue + "; " + expires + ";path = /";
    }

    function getCookie(cname) {
        var name = cname + "=";
        var ca = document.cookie.split(';');
        for (var i = 0; i < ca.length; i++) {
            var c = ca[i].trim();
            if (c.indexOf(name) === 0) return c.substring(name.length, c.length);
        }
        return "";
    }
</script>

</html>
