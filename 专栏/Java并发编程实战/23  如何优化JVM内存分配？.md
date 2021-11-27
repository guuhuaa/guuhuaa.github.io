<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>23  如何优化JVM内存分配？.md</title>
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

                    
                    <a href="00&#32;开篇词你为什么需要学习并发编程？.md">00 开篇词你为什么需要学习并发编程？.md</a>

                </li>
                <li>

                    
                    <a href="01&#32;&#32;如何制定性能调优标准？.md">01  如何制定性能调优标准？.md</a>

                </li>
                <li>

                    
                    <a href="02&#32;&#32;如何制定性能调优策略？.md">02  如何制定性能调优策略？.md</a>

                </li>
                <li>

                    
                    <a href="03&#32;&#32;字符串性能优化不容小觑，百M内存轻松存储几十G数据.md">03  字符串性能优化不容小觑，百M内存轻松存储几十G数据.md</a>

                </li>
                <li>

                    
                    <a href="04&#32;&#32;慎重使用正则表达式.md">04  慎重使用正则表达式.md</a>

                </li>
                <li>

                    
                    <a href="05&#32;&#32;ArrayList还是LinkedList？使用不当性能差千倍.md">05  ArrayList还是LinkedList？使用不当性能差千倍.md</a>

                </li>
                <li>

                    
                    <a href="06&#32;&#32;Stream如何提高遍历集合效率？.md">06  Stream如何提高遍历集合效率？.md</a>

                </li>
                <li>

                    
                    <a href="07&#32;&#32;深入浅出HashMap的设计与优化.md">07  深入浅出HashMap的设计与优化.md</a>

                </li>
                <li>

                    
                    <a href="08&#32;&#32;网络通信优化之IO模型：如何解决高并发下IO瓶颈？.md">08  网络通信优化之IO模型：如何解决高并发下IO瓶颈？.md</a>

                </li>
                <li>

                    
                    <a href="09&#32;&#32;网络通信优化之序列化：避免使用Java序列化.md">09  网络通信优化之序列化：避免使用Java序列化.md</a>

                </li>
                <li>

                    
                    <a href="10&#32;&#32;网络通信优化之通信协议：如何优化RPC网络通信？.md">10  网络通信优化之通信协议：如何优化RPC网络通信？.md</a>

                </li>
                <li>

                    
                    <a href="11&#32;&#32;答疑课堂：深入了解NIO的优化实现原理.md">11  答疑课堂：深入了解NIO的优化实现原理.md</a>

                </li>
                <li>

                    
                    <a href="12&#32;&#32;多线程之锁优化（上）：深入了解Synchronized同步锁的优化方法.md">12  多线程之锁优化（上）：深入了解Synchronized同步锁的优化方法.md</a>

                </li>
                <li>

                    
                    <a href="13&#32;&#32;多线程之锁优化（中）：深入了解Lock同步锁的优化方法.md">13  多线程之锁优化（中）：深入了解Lock同步锁的优化方法.md</a>

                </li>
                <li>

                    
                    <a href="14&#32;&#32;多线程之锁优化（下）：使用乐观锁优化并行操作.md">14  多线程之锁优化（下）：使用乐观锁优化并行操作.md</a>

                </li>
                <li>

                    
                    <a href="15&#32;&#32;多线程调优（上）：哪些操作导致了上下文切换？.md">15  多线程调优（上）：哪些操作导致了上下文切换？.md</a>

                </li>
                <li>

                    
                    <a href="16&#32;&#32;多线程调优（下）：如何优化多线程上下文切换？.md">16  多线程调优（下）：如何优化多线程上下文切换？.md</a>

                </li>
                <li>

                    
                    <a href="17&#32;&#32;并发容器的使用：识别不同场景下最优容器.md">17  并发容器的使用：识别不同场景下最优容器.md</a>

                </li>
                <li>

                    
                    <a href="18&#32;&#32;如何设置线程池大小？.md">18  如何设置线程池大小？.md</a>

                </li>
                <li>

                    
                    <a href="19&#32;&#32;如何用协程来优化多线程业务？.md">19  如何用协程来优化多线程业务？.md</a>

                </li>
                <li>

                    
                    <a href="20&#32;&#32;磨刀不误砍柴工：欲知JVM调优先了解JVM内存模型.md">20  磨刀不误砍柴工：欲知JVM调优先了解JVM内存模型.md</a>

                </li>
                <li>

                    
                    <a href="21&#32;&#32;深入JVM即时编译器JIT，优化Java编译.md">21  深入JVM即时编译器JIT，优化Java编译.md</a>

                </li>
                <li>

                    
                    <a href="22&#32;&#32;如何优化垃圾回收机制？.md">22  如何优化垃圾回收机制？.md</a>

                </li>
                <li>

                    <a class="current-tab" href="23&#32;&#32;如何优化JVM内存分配？.md">23  如何优化JVM内存分配？.md</a>
                    

                </li>
                <li>

                    
                    <a href="24&#32;&#32;内存持续上升，我该如何排查问题？.md">24  内存持续上升，我该如何排查问题？.md</a>

                </li>
                <li>

                    
                    <a href="25&#32;&#32;答疑课堂：模块四热点问题解答.md">25  答疑课堂：模块四热点问题解答.md</a>

                </li>
                <li>

                    
                    <a href="26&#32;&#32;单例模式：如何创建单一对象优化系统性能？.md">26  单例模式：如何创建单一对象优化系统性能？.md</a>

                </li>
                <li>

                    
                    <a href="27&#32;&#32;原型模式与享元模式：提升系统性能的利器.md">27  原型模式与享元模式：提升系统性能的利器.md</a>

                </li>
                <li>

                    
                    <a href="28&#32;&#32;如何使用设计模式优化并发编程？.md">28  如何使用设计模式优化并发编程？.md</a>

                </li>
                <li>

                    
                    <a href="29&#32;&#32;生产者消费者模式：电商库存设计优化.md">29  生产者消费者模式：电商库存设计优化.md</a>

                </li>
                <li>

                    
                    <a href="30&#32;&#32;装饰器模式：如何优化电商系统中复杂的商品价格策略？.md">30  装饰器模式：如何优化电商系统中复杂的商品价格策略？.md</a>

                </li>
                <li>

                    
                    <a href="31&#32;&#32;答疑课堂：模块五思考题集锦.md">31  答疑课堂：模块五思考题集锦.md</a>

                </li>
                <li>

                    
                    <a href="32&#32;&#32;MySQL调优之SQL语句：如何写出高性能SQL语句？.md">32  MySQL调优之SQL语句：如何写出高性能SQL语句？.md</a>

                </li>
                <li>

                    
                    <a href="33&#32;&#32;MySQL调优之事务：高并发场景下的数据库事务调优.md">33  MySQL调优之事务：高并发场景下的数据库事务调优.md</a>

                </li>
                <li>

                    
                    <a href="34&#32;&#32;MySQL调优之索引：索引的失效与优化.md">34  MySQL调优之索引：索引的失效与优化.md</a>

                </li>
                <li>

                    
                    <a href="35&#32;&#32;记一次线上SQL死锁事故：如何避免死锁？.md">35  记一次线上SQL死锁事故：如何避免死锁？.md</a>

                </li>
                <li>

                    
                    <a href="36&#32;&#32;什么时候需要分表分库？.md">36  什么时候需要分表分库？.md</a>

                </li>
                <li>

                    
                    <a href="37&#32;&#32;电商系统表设计优化案例分析.md">37  电商系统表设计优化案例分析.md</a>

                </li>
                <li>

                    
                    <a href="38&#32;&#32;数据库参数设置优化，失之毫厘差之千里.md">38  数据库参数设置优化，失之毫厘差之千里.md</a>

                </li>
                <li>

                    
                    <a href="39&#32;&#32;答疑课堂：MySQL中InnoDB的知识点串讲.md">39  答疑课堂：MySQL中InnoDB的知识点串讲.md</a>

                </li>
                <li>

                    
                    <a href="41&#32;&#32;如何设计更优的分布式锁？.md">41  如何设计更优的分布式锁？.md</a>

                </li>
                <li>

                    
                    <a href="42&#32;&#32;电商系统的分布式事务调优.md">42  电商系统的分布式事务调优.md</a>

                </li>
                <li>

                    
                    <a href="43&#32;&#32;如何使用缓存优化系统性能？.md">43  如何使用缓存优化系统性能？.md</a>

                </li>
                <li>

                    
                    <a href="44&#32;&#32;记一次双十一抢购性能瓶颈调优.md">44  记一次双十一抢购性能瓶颈调优.md</a>

                </li>
                <li>

                    
                    <a href="加餐&#32;&#32;什么是数据的强、弱一致性？.md">加餐  什么是数据的强、弱一致性？.md</a>

                </li>
                <li>

                    
                    <a href="加餐&#32;&#32;推荐几款常用的性能测试工具.md">加餐  推荐几款常用的性能测试工具.md</a>

                </li>
                <li>

                    
                    <a href="答疑课堂：模块三热点问题解答.md">答疑课堂：模块三热点问题解答.md</a>

                </li>
                <li>

                    
                    <a href="结束语&#32;&#32;栉风沐雨，砥砺前行！.md">结束语  栉风沐雨，砥砺前行！.md</a>

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
                        <div><h1>23  如何优化JVM内存分配？</h1>
<p>你好，我是刘超。</p>
<p>JVM 调优是一个系统而又复杂的过程，但我们知道，在大多数情况下，我们基本不用去调整 JVM 内存分配，因为一些初始化的参数已经可以保证应用服务正常稳定地工作了。</p>
<p>但所有的调优都是有目标性的，JVM 内存分配调优也一样。没有性能问题的时候，我们自然不会随意改变 JVM 内存分配的参数。那有了问题呢？有了什么样的性能问题我们需要对其进行调优呢？又该如何调优呢？这就是我今天要分享的内容。</p>
<h2>JVM 内存分配性能问题</h2>
<p>谈到 JVM 内存表现出的性能问题时，你可能会想到一些线上的 JVM 内存溢出事故。但这方面的事故往往是应用程序创建对象导致的内存回收对象难，一般属于代码编程问题。</p>
<p>但其实很多时候，在应用服务的特定场景下，JVM 内存分配不合理带来的性能表现并不会像内存溢出问题这么突出。可以说如果你没有深入到各项性能指标中去，是很难发现其中隐藏的性能损耗。</p>
<p>JVM 内存分配不合理最直接的表现就是频繁的 GC，这会导致上下文切换等性能问题，从而降低系统的吞吐量、增加系统的响应时间。因此，如果你在线上环境或性能测试时，发现频繁的 GC，且是正常的对象创建和回收，这个时候就需要考虑调整 JVM 内存分配了，从而减少 GC 所带来的性能开销。</p>
<h2>对象在堆中的生存周期</h2>
<p>了解了性能问题，那需要做的势必就是调优了。但先别急，在了解 JVM 内存分配的调优过程之前，我们先来看看一个新创建的对象在堆内存中的生存周期，为后面的学习打下基础。</p>
<p>在[第 20 讲]中，我讲过 JVM 内存模型。我们知道，在 JVM 内存模型的堆中，堆被划分为新生代和老年代，新生代又被进一步划分为 Eden 区和 Survivor 区，最后 Survivor 由 From Survivor 和 To Survivor 组成。</p>
<p>当我们新建一个对象时，对象会被优先分配到新生代的 Eden 区中，这时虚拟机会给对象定义一个对象年龄计数器（通过参数 -XX:MaxTenuringThreshold 设置）。</p>
<p>同时，也有另外一种情况，当 Eden 空间不足时，虚拟机将会执行一个新生代的垃圾回收（Minor GC）。这时 JVM 会把存活的对象转移到 Survivor 中，并给对象的年龄 +1。对象在 Survivor 中同样也会经历 MinorGC，每经过一次 MinorGC，对象的年龄将会 +1。</p>
<p>当然了，内存空间也是有设置阈值的，可以通过参数 -XX:PetenureSizeThreshold 设置直接被分配到老年代的最大对象，这时如果分配的对象超过了设置的阀值，对象就会直接被分配到老年代，这样做的好处就是可以减少新生代的垃圾回收。</p>
<h2>查看 JVM 堆内存分配</h2>
<p>我们知道了一个对象从创建至回收到堆中的过程，接下来我们再来了解下 JVM 堆内存是如何分配的。在默认不配置 JVM 堆内存大小的情况下，JVM 根据默认值来配置当前内存大小。我们可以通过以下命令来查看堆内存配置的默认值：</p>
<pre><code>java -XX:+PrintFlagsFinal -version | grep HeapSize 
jmap -heap 17284
</code></pre>
<p><img src="assets/436338cc5251291eeb6dbb57467443d5.png" alt="img" /></p>
<p><img src="assets/59941c65600fe4a11e5bc6b8304fe0de.png" alt="img" /></p>
<p>通过命令，我们可以获得在这台机器上启动的 JVM 默认最大堆内存为 1953MB，初始化大小为 124MB。</p>
<p>在 JDK1.7 中，默认情况下年轻代和老年代的比例是 1:2，我们可以通过–XX:NewRatio 重置该配置项。年轻代中的 Eden 和 To Survivor、From Survivor 的比例是 8:1:1，我们可以通过 -XX:SurvivorRatio 重置该配置项。</p>
<p>在 JDK1.7 中如果开启了 -XX:+UseAdaptiveSizePolicy 配置项，JVM 将会动态调整 Java 堆中各个区域的大小以及进入老年代的年龄，–XX:NewRatio 和 -XX:SurvivorRatio 将会失效，而 JDK1.8 是默认开启 -XX:+UseAdaptiveSizePolicy 配置项的。</p>
<p>还有，在 JDK1.8 中，不要随便关闭 UseAdaptiveSizePolicy 配置项，除非你已经对初始化堆内存 / 最大堆内存、年轻代 / 老年代以及 Eden 区 /Survivor 区有非常明确的规划了。否则 JVM 将会分配最小堆内存，年轻代和老年代按照默认比例 1:2 进行分配，年轻代中的 Eden 和 Survivor 则按照默认比例 8:2 进行分配。这个内存分配未必是应用服务的最佳配置，因此可能会给应用服务带来严重的性能问题。</p>
<h2>JVM 内存分配的调优过程</h2>
<p>我们先使用 JVM 的默认配置，观察应用服务的运行情况，下面我将结合一个实际案例来讲述。现模拟一个抢购接口，假设需要满足一个 5W 的并发请求，且每次请求会产生 20KB 对象，我们可以通过千级并发创建一个 1MB 对象的接口来模拟万级并发请求产生大量对象的场景，具体代码如下：</p>
<pre><code>	
	@RequestMapping(value = &quot;/test1&quot;)
	public String test1(HttpServletRequest request) {
		List&lt;Byte[]&gt; temp = new ArrayList&lt;Byte[]&gt;();
		
		Byte[] b = new Byte[1024*1024];
		temp.add(b);
		
		return &quot;success&quot;;
	}
</code></pre>
<h3>AB 压测</h3>
<p>分别对应用服务进行压力测试，以下是请求接口的吞吐量和响应时间在不同并发用户数下的变化情况：</p>
<p><img src="assets/8b67579af661a666dff89d16ab2e2f26.jpg" alt="img" /></p>
<p>可以看到，当并发数量到了一定值时，吞吐量就上不去了，响应时间也迅速增加。那么，在 JVM 内部运行又是怎样的呢？</p>
<h3>分析 GC 日志</h3>
<p>此时我们可以通过 GC 日志查看具体的回收日志。我们可以通过设置 VM 配置参数，将运行期间的 GC 日志 dump 下来，具体配置参数如下：</p>
<pre><code> -XX:+PrintGCTimeStamps -XX:+PrintGCDetails -Xloggc:/log/heapTest.log

</code></pre>
<p>以下是各个配置项的说明：</p>
<ul>
<li>-XX:PrintGCTimeStamps：打印 GC 具体时间；</li>
<li>-XX:PrintGCDetails ：打印出 GC 详细日志；</li>
<li>-Xloggc: path：GC 日志生成路径。</li>
</ul>
<p>收集到 GC 日志后，我们就可以使用[第 22 讲]中介绍过的 GCViewer 工具打开它，进而查看到具体的 GC 日志如下：</p>
<p><img src="assets/bffd496963f6bbd345092c1454524dd1.jpeg" alt="img" /></p>
<p>主页面显示 FullGC 发生了 13 次，右下角显示年轻代和老年代的内存使用率几乎达到了 100%。而 FullGC 会导致 stop-the-world 的发生，从而严重影响到应用服务的性能。此时，我们需要调整堆内存的大小来减少 FullGC 的发生。</p>
<h3>参考指标</h3>
<p>我们可以将某些指标的预期值作为参考指标，上面的 GC 频率就是其中之一，那么还有哪些指标可以为我们提供一些具体的调优方向呢？</p>
<p>**GC 频率：**高频的 FullGC 会给系统带来非常大的性能消耗，虽然 MinorGC 相对 FullGC 来说好了许多，但过多的 MinorGC 仍会给系统带来压力。</p>
<p>**内存：**这里的内存指的是堆内存大小，堆内存又分为年轻代内存和老年代内存。首先我们要分析堆内存大小是否合适，其实是分析年轻代和老年代的比例是否合适。如果内存不足或分配不均匀，会增加 FullGC，严重的将导致 CPU 持续爆满，影响系统性能。</p>
<p>**吞吐量：**频繁的 FullGC 将会引起线程的上下文切换，增加系统的性能开销，从而影响每次处理的线程请求，最终导致系统的吞吐量下降。</p>
<p>**延时：**JVM 的 GC 持续时间也会影响到每次请求的响应时间。</p>
<h3>具体调优方法</h3>
<p>**调整堆内存空间减少 FullGC：**通过日志分析，堆内存基本被用完了，而且存在大量 FullGC，这意味着我们的堆内存严重不足，这个时候我们需要调大堆内存空间。</p>
<pre><code>java -jar -Xms4g -Xmx4g heapTest-0.0.1-SNAPSHOT.jar

</code></pre>
<p>以下是各个配置项的说明：</p>
<ul>
<li>-Xms：堆初始大小；</li>
<li>-Xmx：堆最大值。</li>
</ul>
<p>调大堆内存之后，我们再来测试下性能情况，发现吞吐量提高了 40% 左右，响应时间也降低了将近 50%。</p>
<p><img src="assets/5fd7c3f198018cf5e789c25bd4f14caf.png" alt="img" /></p>
<p>再查看 GC 日志，发现 FullGC 频率降低了，老年代的使用率只有 16% 了。</p>
<p><img src="assets/b924a13d8cb4e383b94e82d34125002e.jpeg" alt="img" /></p>
<p>**调整年轻代减少 MinorGC：**通过调整堆内存大小，我们已经提升了整体的吞吐量，降低了响应时间。那还有优化空间吗？我们还可以将年轻代设置得大一些，从而减少一些 MinorGC（[第 22 讲]有通过降低 Minor GC 频率来提高系统性能的详解）。</p>
<pre><code>java -jar -Xms4g -Xmx4g -Xmn3g heapTest-0.0.1-SNAPSHOT.jar

</code></pre>
<p>再进行 AB 压测，发现吞吐量上去了。</p>
<p><img src="assets/55de34ab7eccaf9ad83bac846d0cbf04.png" alt="img" /></p>
<p>再查看 GC 日志，发现 MinorGC 也明显降低了，GC 花费的总时间也减少了。</p>
<p><img src="assets/75f84993ba0c52d6d338d19dd4db1a5d.jpeg" alt="img" /></p>
<p>**设置 Eden、Survivor 区比例：**在 JVM 中，如果开启 AdaptiveSizePolicy，则每次 GC 后都会重新计算 Eden、From Survivor 和 To Survivor 区的大小，计算依据是 GC 过程中统计的 GC 时间、吞吐量、内存占用量。这个时候 SurvivorRatio 默认设置的比例会失效。</p>
<p>在 JDK1.8 中，默认是开启 AdaptiveSizePolicy 的，我们可以通过 -XX:-UseAdaptiveSizePolicy 关闭该项配置，或显示运行 -XX:SurvivorRatio=8 将 Eden、Survivor 的比例设置为 8:2。大部分新对象都是在 Eden 区创建的，我们可以固定 Eden 区的占用比例，来调优 JVM 的内存分配性能。</p>
<p>再进行 AB 性能测试，我们可以看到吞吐量提升了，响应时间降低了。</p>
<p><img src="assets/91eb734ea45dc8a24b7938401eafb7c2.png" alt="img" /></p>
<p><img src="assets/cfaef71dbc8ba4f149a6e134482370fd.jpeg" alt="img" /></p>
<h2>总结</h2>
<p>JVM 内存调优通常和 GC 调优是互补的，基于以上调优，我们可以继续对年轻代和堆内存的垃圾回收算法进行调优。这里可以结合上一讲的内容，一起完成 JVM 调优。</p>
<p>虽然分享了一些 JVM 内存分配调优的常用方法，但我还是建议你在进行性能压测后如果没有发现突出的性能瓶颈，就继续使用 JVM 默认参数，起码在大部分的场景下，默认配置已经可以满足我们的需求了。但满足不了也不要慌张，结合今天所学的内容去实践一下，相信你会有新的收获。</p>
<h2>思考题</h2>
<p>以上我们都是基于堆内存分配来优化系统性能的，但在 NIO 的 Socket 通信中，其实还使用到了堆外内存来减少内存拷贝，实现 Socket 通信优化。你知道堆外内存是如何创建和回收的吗？</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="22&#32;&#32;如何优化垃圾回收机制？.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="24&#32;&#32;内存持续上升，我该如何排查问题？.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b43442a18f370ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
            document.getElementById("tip").innerHTML = "<a href='https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/Java%E5%B9%B6%E5%8F%91%E7%BC%96%E7%A8%8B%E5%AE%9E%E6%88%98/&quot;&#32;+&#32;cookie&#32;+&#32;&quot;'>跳转到上次进度</a>"
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
