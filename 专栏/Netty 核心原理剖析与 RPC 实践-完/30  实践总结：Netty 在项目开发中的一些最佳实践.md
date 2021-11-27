<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>30  实践总结：Netty 在项目开发中的一些最佳实践.md</title>
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

                    
                    <a href="00&#32;学好&#32;Netty，是你修炼&#32;Java&#32;内功的必经之路.md">00 学好 Netty，是你修炼 Java 内功的必经之路.md</a>

                </li>
                <li>

                    
                    <a href="01&#32;&#32;初识&#32;Netty：为什么&#32;Netty&#32;这么流行？.md">01  初识 Netty：为什么 Netty 这么流行？.md</a>

                </li>
                <li>

                    
                    <a href="02&#32;&#32;纵览全局：把握&#32;Netty&#32;整体架构脉络.md">02  纵览全局：把握 Netty 整体架构脉络.md</a>

                </li>
                <li>

                    
                    <a href="03&#32;&#32;引导器作用：客户端和服务端启动都要做些什么？.md">03  引导器作用：客户端和服务端启动都要做些什么？.md</a>

                </li>
                <li>

                    
                    <a href="04&#32;事件调度层：为什么&#32;EventLoop&#32;是&#32;Netty&#32;的精髓？.md">04 事件调度层：为什么 EventLoop 是 Netty 的精髓？.md</a>

                </li>
                <li>

                    
                    <a href="05&#32;&#32;服务编排层：Pipeline&#32;如何协调各类&#32;Handler&#32;？.md">05  服务编排层：Pipeline 如何协调各类 Handler ？.md</a>

                </li>
                <li>

                    
                    <a href="06&#32;&#32;粘包拆包问题：如何获取一个完整的网络包？.md">06  粘包拆包问题：如何获取一个完整的网络包？.md</a>

                </li>
                <li>

                    
                    <a href="07&#32;&#32;接头暗语：如何利用&#32;Netty&#32;实现自定义协议通信？.md">07  接头暗语：如何利用 Netty 实现自定义协议通信？.md</a>

                </li>
                <li>

                    
                    <a href="08&#32;&#32;开箱即用：Netty&#32;支持哪些常用的解码器？.md">08  开箱即用：Netty 支持哪些常用的解码器？.md</a>

                </li>
                <li>

                    
                    <a href="09&#32;&#32;数据传输：writeAndFlush&#32;处理流程剖析.md">09  数据传输：writeAndFlush 处理流程剖析.md</a>

                </li>
                <li>

                    
                    <a href="10&#32;&#32;双刃剑：合理管理&#32;Netty&#32;堆外内存.md">10  双刃剑：合理管理 Netty 堆外内存.md</a>

                </li>
                <li>

                    
                    <a href="11&#32;&#32;另起炉灶：Netty&#32;数据传输载体&#32;ByteBuf&#32;详解.md">11  另起炉灶：Netty 数据传输载体 ByteBuf 详解.md</a>

                </li>
                <li>

                    
                    <a href="12&#32;&#32;他山之石：高性能内存分配器&#32;jemalloc&#32;基本原理.md">12  他山之石：高性能内存分配器 jemalloc 基本原理.md</a>

                </li>
                <li>

                    
                    <a href="13&#32;&#32;举一反三：Netty&#32;高性能内存管理设计（上）.md">13  举一反三：Netty 高性能内存管理设计（上）.md</a>

                </li>
                <li>

                    
                    <a href="14&#32;&#32;举一反三：Netty&#32;高性能内存管理设计（下）.md">14  举一反三：Netty 高性能内存管理设计（下）.md</a>

                </li>
                <li>

                    
                    <a href="15&#32;&#32;轻量级对象回收站：Recycler&#32;对象池技术解析.md">15  轻量级对象回收站：Recycler 对象池技术解析.md</a>

                </li>
                <li>

                    
                    <a href="16&#32;&#32;IO&#32;加速：与众不同的&#32;Netty&#32;零拷贝技术.md">16  IO 加速：与众不同的 Netty 零拷贝技术.md</a>

                </li>
                <li>

                    
                    <a href="17&#32;&#32;源码篇：从&#32;Linux&#32;出发深入剖析服务端启动流程.md">17  源码篇：从 Linux 出发深入剖析服务端启动流程.md</a>

                </li>
                <li>

                    
                    <a href="18&#32;&#32;源码篇：解密&#32;Netty&#32;Reactor&#32;线程模型.md">18  源码篇：解密 Netty Reactor 线程模型.md</a>

                </li>
                <li>

                    
                    <a href="19&#32;&#32;源码篇：一个网络请求在&#32;Netty&#32;中的旅程.md">19  源码篇：一个网络请求在 Netty 中的旅程.md</a>

                </li>
                <li>

                    
                    <a href="20&#32;&#32;技巧篇：Netty&#32;的&#32;FastThreadLocal&#32;究竟比&#32;ThreadLocal&#32;快在哪儿？.md">20  技巧篇：Netty 的 FastThreadLocal 究竟比 ThreadLocal 快在哪儿？.md</a>

                </li>
                <li>

                    
                    <a href="21&#32;&#32;技巧篇：延迟任务处理神器之时间轮&#32;HashedWheelTimer.md">21  技巧篇：延迟任务处理神器之时间轮 HashedWheelTimer.md</a>

                </li>
                <li>

                    
                    <a href="22&#32;&#32;技巧篇：高性能无锁队列&#32;Mpsc&#32;Queue.md">22  技巧篇：高性能无锁队列 Mpsc Queue.md</a>

                </li>
                <li>

                    
                    <a href="23&#32;&#32;架构设计：如何实现一个高性能分布式&#32;RPC&#32;框架.md">23  架构设计：如何实现一个高性能分布式 RPC 框架.md</a>

                </li>
                <li>

                    
                    <a href="24&#32;&#32;服务发布与订阅：搭建生产者和消费者的基础框架.md">24  服务发布与订阅：搭建生产者和消费者的基础框架.md</a>

                </li>
                <li>

                    
                    <a href="25&#32;&#32;远程通信：通信协议设计以及编解码的实现.md">25  远程通信：通信协议设计以及编解码的实现.md</a>

                </li>
                <li>

                    
                    <a href="26&#32;&#32;服务治理：服务发现与负载均衡机制的实现.md">26  服务治理：服务发现与负载均衡机制的实现.md</a>

                </li>
                <li>

                    
                    <a href="27&#32;&#32;动态代理：为用户屏蔽&#32;RPC&#32;调用的底层细节.md">27  动态代理：为用户屏蔽 RPC 调用的底层细节.md</a>

                </li>
                <li>

                    
                    <a href="28&#32;&#32;实战总结：RPC&#32;实战总结与进阶延伸.md">28  实战总结：RPC 实战总结与进阶延伸.md</a>

                </li>
                <li>

                    
                    <a href="29&#32;&#32;编程思想：Netty&#32;中应用了哪些设计模式？.md">29  编程思想：Netty 中应用了哪些设计模式？.md</a>

                </li>
                <li>

                    <a class="current-tab" href="30&#32;&#32;实践总结：Netty&#32;在项目开发中的一些最佳实践.md">30  实践总结：Netty 在项目开发中的一些最佳实践.md</a>
                    

                </li>
                <li>

                    
                    <a href="31&#32;结束语&#32;&#32;技术成长之路：如何打造自己的技术体系.md">31 结束语  技术成长之路：如何打造自己的技术体系.md</a>

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
                        <div><h1>30  实践总结：Netty 在项目开发中的一些最佳实践</h1>
<p>这是专栏的最后一节课，首先恭喜你持之以恒学习到现在，你已经离成为一个 Netty 高手不远啦！本节课我会结合自身的实践经验，整理出一些 Netty 的最佳实践，帮助你回顾之前课程的知识点以及进一步提升 Netty 的进阶技巧。</p>
<p>本节课我们的内容以知识点列表的方式呈现，仅仅对 Netty 的核心要点进行提炼，更多详细的实现原理需要你课后深入研究源码。</p>
<h3>性能篇</h3>
<h4>网络参数优化</h4>
<p>Netty 提供了 ChannelOption 以便于我们优化 TCP 参数配置，为了提高网络通信的吞吐量，一些可选的网络参数我们有必要掌握。在之前的课程中我们已经介绍了一些常用的参数，我们在此基础上再做一些详细地扩展。</p>
<ul>
<li><strong>SO_SNDBUF/SO_RCVBUF</strong></li>
</ul>
<p>TCP 发送缓冲区和接收缓冲区的大小。为了能够达到最大的网络吞吐量，SO_SNDBUF 不应当小于带宽和时延的乘积。SO_RCVBUF 一直会保存数据到应用进程读取为止，如果 SO_RCVBUF 满了，接收端会通知对端 TCP 协议中的窗口关闭，保证 SO_RCVBUF 不会溢出。</p>
<p>SO_SNDBUF/SO_RCVBUF 大小的设置建议参考消息的平均大小，不要按照最大消息来进行设置，这样会造成额外的内存浪费。更灵活的方式是可以动态调整缓冲区的大小，这时候就体现出 ByteBuf 的优势，Netty 提供的 ByteBuf 是可以支持动态调整容量的，而且提供了开箱即用的工具，例如可动态调整容量的接收缓冲区分配器 AdaptiveRecvByteBufAllocator。</p>
<ul>
<li><strong>TCP_NODELAY</strong></li>
</ul>
<p>是否开启 Nagle 算法。Nagle 算法通过缓存的方式将网络数据包累积到一定量才会发送，从而避免频繁发送小的数据包。Nagle 算法 在海量流量的场景下非常有效，但是会造成一定的数据延迟。如果对数据传输延迟敏感，那么应该禁用该参数。</p>
<ul>
<li><strong>SO_BACKLOG</strong></li>
</ul>
<p>已完成三次握手的请求队列最大长度。同一时刻服务端可能会处理多个连接，在高并发海量连接的场景下，该参数应适当调大。但是 SO_BACKLOG 也不能太大，否则无法防止 SYN-Flood 攻击。</p>
<ul>
<li><strong>SO_KEEPALIVE</strong></li>
</ul>
<p>连接保活。启用了 TCP SO_KEEPALIVE 属性，TCP 会主动探测连接状态，Linux 默认设置了 2 小时的心跳频率。TCP KEEPALIVE 机制主要用于回收死亡时间交长的连接，不适合实时性高的场景。</p>
<p>在海量连接的场景下，也许你会遇到类似 &quot;too many open files&quot; 的报错，所以 Linux 操作系统最大文件句柄数基本是必须要调优参数。可以通过 vi /etc/security/limits.conf，添加如下配置：</p>
<pre><code>* soft nofile 1000000

* hard nofile 1000000
</code></pre>
<p>修改保存以后，执行 sysctl -p 命令使配置生效，然后通过 ulimit -a 命令查看参数是否生效。</p>
<h4>业务线程池的必要性</h4>
<p>Netty 是基于 Reactor 线程模型实现的，I/O 线程数量固定且资源珍贵，ChannelPipeline 负责所有事件的传播，如果其中任何一个 ChannelHandler 处理器需要执行耗时的操作，其中那么 I/O 线程就会出现阻塞，甚至整个系统都会被拖垮。所以推荐的做法是在 ChannelHandler 处理器中自定义新的业务线程池，将耗时的操作提交到业务线程池中执行。以 RPC 框架为例，在服务提供者处理 RPC 请求调用时就是将 RPC 请求提交到自定义的业务线程池中执行，如下所示：</p>
<pre><code>public class RpcRequestHandler extends SimpleChannelInboundHandler&lt;MiniRpcProtocol&lt;MiniRpcRequest&gt;&gt; {

    @Override

    protected void channelRead0(ChannelHandlerContext ctx, MiniRpcProtocol&lt;MiniRpcRequest&gt; protocol) {

        RpcRequestProcessor.submitRequest(() -&gt; {

            // 处理 RPC 请求

        });

    }

}
</code></pre>
<h4>共享 ChannelHandler</h4>
<p>我们经常使用以下 new HandlerXXX() 的方式进行 Channel 初始化，在每建立一个新连接的时候会初始化新的 HandlerA 和 HandlerB，如果系统承载了 1w 个连接，那么就会初始化 2w 个处理器，造成非常大的内存浪费。</p>
<pre><code>ServerBootstrap b = new ServerBootstrap();

            b.group(bossGroup, workerGroup)

                    .channel(NioServerSocketChannel.class)

                    .localAddress(new InetSocketAddress(port))

                    .childHandler(new ChannelInitializer&lt;SocketChannel&gt;() {

                        @Override

                        public void initChannel(SocketChannel ch) {

                            ch.pipeline()

                                    .addLast(new HandlerA())

                                    .addLast(new HandlerB());

                        }

                    });
</code></pre>
<p>为了解决上述问题，Netty 提供了 @Sharable 注解用于修饰 ChannelHandler，标识该 ChannelHandler 全局只有一个实例，而且会被多个 ChannelPipeline 共享。所以我们必须要注意的是，@Sharable 修饰的 ChannelHandler 必须都是无状态的，这样才能保证线程安全。</p>
<h4>设置高低水位线</h4>
<p>高低水位线 WRITE_BUFFER_HIGH_WATER_MARK 和 WRITE_BUFFER_LOW_WATER_MARK 是两个非常重要的流控参数。Netty 每次添加数据时都会累加数据的字节数，然后判断缓存大小是否超过所设置的高水位线，如果超过了高水位，那么 Channel 会被设置为不可写状态。直到缓存的数据大小低于低水位线以后，Channel 才恢复成可写状态。Netty 默认的高低水位线配置是 32K ~ 64K，可以根据发送端和接收端的实际情况合理设置高低水位线，如果你没有足够的测试数据作为参考依据，建议不要随意更改高低水位线。高低水位线的设置方式如下：</p>
<pre><code>// Server

ServerBootstrap bootstrap = new ServerBootstrap();

bootstrap.childOption(ChannelOption.WRITE_BUFFER_HIGH_WATER_MARK, 32 * 1024);

bootstrap.childOption(ChannelOption.WRITE_BUFFER_LOW_WATER_MARK, 8 * 1024);

// Client

Bootstrap bootstrap = new Bootstrap();

bootstrap.option(ChannelOption.WRITE_BUFFER_HIGH_WATER_MARK, 32 * 1024);

bootstrap.option(ChannelOption.WRITE_BUFFER_LOW_WATER_MARK, 8 * 1024);
</code></pre>
<p>当缓存超过了高水位，Channel 会被设置为不可写状态，调用 isWritable() 方法会返回 false。建议在 Channel 写数据之前，使用 isWritable() 方法来判断缓存水位情况，防止因为接收方处理较慢造成 OOM。推荐的使用方式如下：</p>
<pre><code>if (ctx.channel().isActive() &amp;&amp; ctx.channel().isWritable()) {

    ctx.writeAndFlush(message);

} else {

    // handle message

}
</code></pre>
<h4>GC 参数优化</h4>
<p>对不同场景下的网络应用程序进行 JVM 参数调优，可以取得很好的性能提升，以及避免 OOM 风险。因为不同业务系统的特性是不一样的，在此我只能给你分享一些重要的注意事项。</p>
<ul>
<li><strong>堆内存</strong>：-Xms 和 -Xmx 参数，-Xmx 用于控制 JVM Heap 的最大值，必须设置其大小，合理调整 -Xmx 有助于降低 GC 开销，提升系统吞吐量。-Xms 表示 JVM Heap 的初始值，对于生产环境的服务端来说 -Xms 和 -Xmx 最好设置为相同值。</li>
<li><strong>堆外内存</strong>：DirectByteBuffer 最容易造成 OOM 的情况，DirectByteBuffer 对象的回收需要依赖 Old GC 或者 Full GC 才能触发清理。如果长时间没有 Old GC 或者 Full GC 执行，那么堆外内存即使不再使用，也会一直在占用内存不释放。我们最好通过 JVM 参数 -XX:MaxDirectMemorySize 指定堆外内存的上限大小，当堆外内存的大小超过该阈值时，就会触发一次 Full GC 进行清理回收，如果在 Full GC 之后还是无法满足堆外内存的分配，那么程序将会抛出 OOM 异常。</li>
<li><strong>年轻代</strong>：-Xmn 调整新生代大小，-XX:SurvivorRatio 设置 SurvivorRatio 和 eden 区比例。我们经常遇到 YGC 频繁的情况，应该清楚程序中对象的基本分布情况，如果存在大量朝生夕灭的对象，应适当调大新生代；反之应适当调大老年代。例如在类似百万长连接、推送服务等延迟敏感的场景中，老年代的内存增长缓慢，优化年轻代的空间大小以及各区的比例可以带来更大的收益。</li>
</ul>
<h4>内存池 &amp; 对象池</h4>
<p>从内存分配的角度来看，ByteBuf 可以分为堆内存 HeapByteBuf 和堆外内存 DirectByteBuf。DirectByteBuf 相比于 HeapByteBuf，虽然分配和回收的效率较慢，但是在 Socket 读写时可以少一次内存拷贝，性能更佳。</p>
<p>为了减少堆外内存的频繁创建和销毁，Netty 提供了池化类型的 PooledDirectByteBuf。Netty 提前申请一块连续内存作为 ByteBuf 内存池，如果有堆外内存申请的需求直接从内存池里获取即可，使用完之后必须重新放回内存池，否则会造成严重的内存泄漏。Netty 中启用内存池可以在创建客户端或者服务端的时候指定，示例代码如下：</p>
<pre><code>bootstrap.option(ChannelOption.ALLOCATOR, PooledByteBufAllocator.DEFAULT);

bootstrap.childOption(ChannelOption.ALLOCATOR, PooledByteBufAllocator.DEFAULT);
</code></pre>
<p>对象池与内存池的都是为了提高 Netty 的并发处理能力，通常在项目开发中我们会将一些通用的对象缓存起来，当需要该对象时，优先从对象池中获取对象实例。通过重用对象，不仅避免频繁地创建和销毁所带来的性能损耗，而且对 JVM GC 是友好的。如果你是一个高性能的网络应用系统，不妨试下 Netty 提供的 Recycler 对象池。Recycler 对象池如何使用在之前的课程有介绍过，在此我们一起回顾下。假设我们有一个 User 类，需要实现 User 对象的复用，具体实现代码如下：</p>
<pre><code>public class UserCache {

    private static final Recycler&lt;User&gt; userRecycler = new Recycler&lt;User&gt;() {

        @Override

        protected User newObject(Handle&lt;User&gt; handle) {

            return new User(handle);

        }

    };

    static final class User {

        private String name;

        private Recycler.Handle&lt;User&gt; handle;

        public void setName(String name) {

            this.name = name;

        }

        public String getName() {

            return name;

        }

        public User(Recycler.Handle&lt;User&gt; handle) {

            this.handle = handle;

        }

        public void recycle() {

            handle.recycle(this);

        }

    }

    public static void main(String[] args) {

        User user1 = userRecycler.get(); // 1、从对象池获取 User 对象

        user1.setName(&quot;hello&quot;); // 2、设置 User 对象的属性

        user1.recycle(); // 3、回收对象到对象池

        User user2 = userRecycler.get(); // 4、从对象池获取对象

        System.out.println(user2.getName());

        System.out.println(user1 == user2);

    }

}ß
</code></pre>
<p>由此可见，Netty 内存池和 Recycler 对象池优化的核心目标都是为了减少资源分配的开销，避免大量朝生夕灭的对象造成严重的内存消耗和 GC 压力。关于内存池和对象池的原理可以复习下之前课程《举一反三：Netty 高性能内存管理设计》《轻量级对象回收站：Recycler 对象池技术解析》，值得我们反复消化理解。</p>
<h4>Native 支持</h4>
<p>从 4.0.16 版本起，Netty 提供了用 C++ 编写 JNI 调用的 Socket Transport，相比 JDK NIO 具备更高的性能和更低的 GC 成本，并且支持更多的 TCP 参数。</p>
<pre><code>&lt;dependency&gt;

    &lt;groupId&gt;io.netty&lt;/groupId&gt;

    &lt;artifactId&gt;netty-transport-native-epoll&lt;/artifactId&gt;

    &lt;version&gt;4.1.42.Final&lt;/version&gt;

&lt;/dependency&gt;
</code></pre>
<p>使用 Netty Native 非常简单，只需要替换相应的类即可：</p>
<p><img src="assets/CgqCHmARHOOAcWjJAADrOc_tFhY317.png" alt="图片1.png" /></p>
<h4>线程绑定</h4>
<p>如果是经常关注系统性能调优，一定挖掘过 Linux 操作系统 CPU 亲和性的黑科技招数。CPU 亲和性是指在多核 CPU 的机器上线程可以被强制运行在某个 CPU 上，而不会调度到其他 CPU，也被称为绑核。当绑定线程到某个固定的 CPU 后，不仅可以避免 CPU 切换的开销，而且可以提高 CPU Cache 命中率，对系统性能有一定提升。</p>
<p>在 C/C++、Golang 中实现绑核操作是非常容易的事，遗憾的是在 Java 中是比较麻烦的。目前 Java 中有一个开源 affinity 类库，GitHub 地址<a href="https://github.com/OpenHFT/Java-Thread-Affinity">https://github.com/OpenHFT/Java-Thread-Affinity</a>。如果你的项目想引入使用它，需要先引入 Maven 依赖：</p>
<pre><code>&lt;dependency&gt;

    &lt;groupId&gt;net.openhft&lt;/groupId&gt;

    &lt;artifactId&gt;affinity&lt;/artifactId&gt;

    &lt;version&gt;3.0.6&lt;/version&gt;

&lt;/dependency&gt;
</code></pre>
<p>affinity 类库可以和 Netty 轻松集成，比较常用的方式是创建一个 AffinityThreadFactory，然后传递给 EventLoopGroup，AffinityThreadFactory 负责创建 Worker 线程并完成绑核。代码实现如下所示：</p>
<pre><code>EventLoopGroup bossGroup = new NioEventLoopGroup(1);

ThreadFactory threadFactory = new AffinityThreadFactory(&quot;worker&quot;, AffinityStrategies.DIFFERENT_CORE);

EventLoopGroup workerGroup = new NioEventLoopGroup(4, threadFactory);

ServerBootstrap serverBootstrap = new ServerBootstrap().group(bossGroup, workerGroup);
</code></pre>
<h3>高可用篇</h3>
<h4>连接空闲检测 + 心跳检测</h4>
<p>连接空闲检测是指每隔一段时间检测连接是否有数据读写，如果服务端一直能收到客户端连接发送过来的数据，说明连接处于活跃状态，对于假死的连接是收不到对端发送的数据的。如果一段时间内没收到客户端发送的数据，并不能说明连接一定处于假死状态，有可能客户端就是长时间没有数据需要发送，但是建立的连接还是健康状态，所以服务端还需要通过心跳检测的机制判断客户端是否存活。</p>
<p>客户端可以定时向服务端发送一次心跳包，如果有 N 次没收到心跳数据，可以判断当前客户端已经下线或处于不健康状态。由此可见，连接空闲检测和心跳检测是应对连接假死的一种有效手段，通常空闲检测时间间隔要大于 2 个周期的心跳检测时间间隔，主要是为了排除网络抖动的造成心跳包未能成功收到。</p>
<p>TCP 中已经有 SO_KEEPALIVE 参数，为什么我们还要在应用层加入心跳机制呢？心跳机制不仅能说明应用程序是活跃状态，更重要的是可以判断应用程序是否还在正常工作。然而 TCP KEEPALIVE 是有严重缺陷的，KEEPALIVE 设计初衷是为了清除和回收处于死亡状态的连接，实时性不高。KEEPALIVE 只能检查连接是否活跃，但是不能判断连接是否可用，例如服务端如果处于高负载假死状态，但是连接依然是处于活跃状态的。</p>
<h4>解码器保护</h4>
<p>Netty 在实现数据解码时，需要等待到缓冲区有足够多的字节才能开始解码。为了避免缓冲区缓存太多数据造成内存耗尽，我们可以在解码器中设置一个最大字节的阈值，然后结合 Netty 提供的 TooLongFrameException 异常通知 ChannelPipeline 中其他 ChannelHandler。示例如下：</p>
<pre><code>public class MyDecoder extends ByteToMessageDecoder {

    private static final int MAX_FRAME_LIMIT = 1024;

    @Override

    public void decode(ChannelHandlerContext ctx, ByteBuf in, List&lt;Object&gt; out) {

        int readable = in.readableBytes();

        if (readable &gt; MAX_FRAME_LIMIT) {

            in.skipBytes(readable);

            throw new TooLongFrameException(&quot;too long frame&quot;);

        }

        // decode

    }

}
</code></pre>
<p>检测缓冲区可读字节是否大于 MAX_FRAME_LIMIT，如果超过忽略这些可读字节，对于应用程序在特定的场景下是一种有效的保护措施。</p>
<h4>线程池隔离</h4>
<p>我们知道，如果有复杂且耗时的业务逻辑，推荐的做法是在 ChannelHandler 处理器中自定义新的业务线程池，将耗时的操作提交到业务线程池中执行。建议根据业务逻辑的核心等级拆分出多个业务线程池，如果某类业务逻辑出现异常造成线程池资源耗尽，也不会影响到其他业务逻辑，从而提高应用程序整体可用率。对于 Netty I/O 线程来说，每个 EventLoop 可以与某类业务线程池绑定，避免出现多线程锁竞争。如下图所示：</p>
<p><img src="assets/Ciqc1GARHPmAVpH0AAbJ3pDMXRM753.png" alt="图片2.png" /></p>
<h4>流量整形</h4>
<p>流量整形（Traffic Shaping）是一种主动控制服务流量输出速率的措施，保证下游服务能够平稳处理。流量整形和流控的区别在于，流量整形不会丢弃和拒绝消息，无论流量洪峰有多大，它都会采用令牌桶算法控制流量以恒定的速率输出，如下图所示。</p>
<p><img src="assets/Ciqc1GAQzc2AOPD0AARXF7k43FA223.png" alt="Drawing 1.png" /></p>
<p>Netty 通过实现流量整形的抽象类 AbstractTrafficShapingHandler，提供了三种类型的流量整形策略：GlobalTrafficShapingHandler、ChannelTrafficShapingHandler 和 GlobalChannelTrafficShapingHandler，它们之间的关系如下：</p>
<pre><code>GlobalTrafficShapingHandler = ChannelTrafficShapingHandler + GlobalChannelTrafficShapingHandler
</code></pre>
<p>全局流量整形 GlobalChannelTrafficShapingHandler 作用范围是所有 Channel，用户可以设置全局报文的接收速率、发送速率、整形周期。Channel 级流量整形 ChannelTrafficShapingHandler 作用范围是单个 Channel，可以对不同的 Channel 设置流量整形策略。举个简单的例子，火爆的旅游景区不仅在大门口对游客限流（相当于 GlobalChannelTrafficShapingHandler），而且在景区内部不同的小景点也对游客有限流（相当于 ChannelTrafficShapingHandler），这两个流量整形策略加起来就是 GlobalTrafficShapingHandler。</p>
<p>流量整形并不能保证系统处于安全状态，当流量洪峰过大，数据会一直积压在内存中，所以流量整形和流控应该结合使用才能保证系统的高可用。</p>
<h3>堆外内存泄漏排查思路</h3>
<p>堆外内存泄漏问题是 Netty 应用程序的热点问题，经常遇到 Java 进程占用内存很高，但是堆内存并不高的情况。这里给你分享一些排查堆外内存泄漏的基本思路：</p>
<h4>堆外内存回收</h4>
<p>jmap -histo:live <code>&lt;pid&gt;</code> 手动触发 FullGC, 观察堆外内存是否被回收，如果正常回收很可能是因为堆外设置太小，可以通过 -XX:MaxDirectMemorySize 调整。当然这无法排除堆外内存缓慢泄漏的情况，需要借助其他工具进行分析。</p>
<h4>堆外内存代码监控</h4>
<p>前面的课程我们介绍过堆外内存回收原理，建议你再回过头复习下。JDK 默认采用 Cleaner 回收释放 DirectByteBuffer，Cleaner 继承于 PhantomReference，因为依赖 GC 进行处理，所以回收的时间是不可控的。对于 hasCleaner 的 DirectByteBuffer，Java 提供了一系列不同类型的 MXBean 用于获取 JVM 进程线程、内存等监控指标，代码实现如下：</p>
<pre><code>BufferPoolMXBean directBufferPoolMXBean = ManagementFactory.getPlatformMXBeans(BufferPoolMXBean.class).get(0);

LOGGER.info(&quot;DirectBuffer count: {}, MemoryUsed: {} K&quot;, directBufferPoolMXBean.getCount(), directBufferPoolMXBean.getMemoryUsed()/1024);
</code></pre>
<p>对于 Netty 中 noCleaner 的 DirectByteBuffer，直接通过 PlatformDependent.usedDirectMemory() 读取即可。</p>
<h4>Netty 自带检测工具</h4>
<p>Netty 提供了自带的内存泄漏检测工具，我们可以通过以下命令启用堆外内存泄漏检测工具：</p>
<pre><code>-Dio.netty.leakDetection.level=paranoid
</code></pre>
<p>Netty 一共提供了四种检测级别：</p>
<ol>
<li>disabled，关闭堆外内存泄漏检测；</li>
<li>simple，以 1% 的采样率进行堆外内存泄漏检测，消耗资源较少，属于默认的检测级别；</li>
<li>advanced，以 1% 的采样率进行堆外内存泄漏检测，并提供详细的内存泄漏报告；</li>
<li>paranoid，追踪全部堆外内存的使用情况，并提供详细的内存泄漏报告，属于最高的检测级别，性能开销较大，常用于本地调试排查问题。</li>
</ol>
<p>Netty 会检测 ByteBuf 是否已经不可达且引用计数大于 0，判定内存泄漏的位置并输出到日志中，你需要关注日志中 LEAK 关键字。</p>
<h4>MemoryAnalyzer 内存分析</h4>
<p>我们可以通过传统 Dump 内存的方法排查堆外内存泄漏问题，运行如下命令：</p>
<pre><code>jmap -dump:format=b,file=heap.dump pid
</code></pre>
<p>Dump 完内存堆栈之后，将其导入 MemoryAnalyzer 工具进行分析内存泄漏的可疑点，最终定位到代码源头。关于如何 MemoryAnalyzer 工具我在此就不展开了，需要你自行学习研究，这是每一个 Java 程序员的必备技能。</p>
<h4>Btrace 神器</h4>
<p>Btrace 是一款通过字节码检测 Java 程序的排障神器，它可以获取程序在运行过程中的一切信息，与 AOP 的使用方式类似。我们可以通过如下方式追踪 DirectByteBuffer 的堆外内存申请的源头：</p>
<pre><code>@BTrace

public class TraceDirectAlloc {

    @OnMethod(clazz = &quot;java.nio.Bits&quot;, method = &quot;reserveMemory&quot;)

    public static void printThreadStack() {

        jstack();

    }

}
</code></pre>
<h4>二分排查法：笨方法解决大问题</h4>
<p>堆外内存泄漏问题有时候非常隐蔽，并不是很容易定位发现。为了提高问题排查的效率，我们最好能够在本地模拟复现出堆外内存泄漏问题，如果本地能够成功复现，那么已经成功了一半了。</p>
<p>我们可以根据近期代码变更的记录，通过二分法对代码进行回滚，然后再次尝试是否可以复现出堆外内存泄漏问题，最终可以定位出有问题的代码 commit。该思路虽然是一种笨方法，但是很多场景下可以有效解决问题。</p>
<h3>总结</h3>
<p>以上都是项目实践中的一些重要技巧，对于我们上手 Netty 应用程序开发已经足够使用，还有更多 Netty  的技巧和使用心得需要我们去自己在实践中探索。纸上得来终觉浅，绝知此事要躬行，当你积累了丰富的经验，不管是项目开发还是问题排障，都会越来越得心应手。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="29&#32;&#32;编程思想：Netty&#32;中应用了哪些设计模式？.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="31&#32;结束语&#32;&#32;技术成长之路：如何打造自己的技术体系.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b4349515dc870ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
            document.getElementById("tip").innerHTML = "<a href='https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/Netty%20%E6%A0%B8%E5%BF%83%E5%8E%9F%E7%90%86%E5%89%96%E6%9E%90%E4%B8%8E%20RPC%20%E5%AE%9E%E8%B7%B5-%E5%AE%8C/&quot;&#32;+&#32;cookie&#32;+&#32;&quot;'>跳转到上次进度</a>"
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
