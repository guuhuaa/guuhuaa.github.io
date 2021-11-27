<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>38  调优Kafka，你做到了吗？.md</title>
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

                    
                    <a href="00&#32;开篇词&#32;&#32;为什么要学习Kafka？.md">00 开篇词  为什么要学习Kafka？.md</a>

                </li>
                <li>

                    
                    <a href="01&#32;&#32;消息引擎系统ABC.md">01  消息引擎系统ABC.md</a>

                </li>
                <li>

                    
                    <a href="02&#32;&#32;一篇文章带你快速搞定Kafka术语.md">02  一篇文章带你快速搞定Kafka术语.md</a>

                </li>
                <li>

                    
                    <a href="03&#32;&#32;Kafka只是消息引擎系统吗？.md">03  Kafka只是消息引擎系统吗？.md</a>

                </li>
                <li>

                    
                    <a href="04&#32;&#32;我应该选择哪种Kafka？.md">04  我应该选择哪种Kafka？.md</a>

                </li>
                <li>

                    
                    <a href="05&#32;&#32;聊聊Kafka的版本号.md">05  聊聊Kafka的版本号.md</a>

                </li>
                <li>

                    
                    <a href="06&#32;&#32;Kafka线上集群部署方案怎么做？.md">06  Kafka线上集群部署方案怎么做？.md</a>

                </li>
                <li>

                    
                    <a href="07&#32;&#32;最最最重要的集群参数配置（上）.md">07  最最最重要的集群参数配置（上）.md</a>

                </li>
                <li>

                    
                    <a href="08&#32;&#32;最最最重要的集群参数配置（下）.md">08  最最最重要的集群参数配置（下）.md</a>

                </li>
                <li>

                    
                    <a href="09&#32;&#32;生产者消息分区机制原理剖析.md">09  生产者消息分区机制原理剖析.md</a>

                </li>
                <li>

                    
                    <a href="10&#32;&#32;生产者压缩算法面面观.md">10  生产者压缩算法面面观.md</a>

                </li>
                <li>

                    
                    <a href="11&#32;&#32;无消息丢失配置怎么实现？.md">11  无消息丢失配置怎么实现？.md</a>

                </li>
                <li>

                    
                    <a href="12&#32;&#32;客户端都有哪些不常见但是很高级的功能？.md">12  客户端都有哪些不常见但是很高级的功能？.md</a>

                </li>
                <li>

                    
                    <a href="13&#32;&#32;Java生产者是如何管理TCP连接的？.md">13  Java生产者是如何管理TCP连接的？.md</a>

                </li>
                <li>

                    
                    <a href="14&#32;&#32;幂等生产者和事务生产者是一回事吗？.md">14  幂等生产者和事务生产者是一回事吗？.md</a>

                </li>
                <li>

                    
                    <a href="15&#32;&#32;消费者组到底是什么？.md">15  消费者组到底是什么？.md</a>

                </li>
                <li>

                    
                    <a href="16&#32;&#32;揭开神秘的“位移主题”面纱.md">16  揭开神秘的“位移主题”面纱.md</a>

                </li>
                <li>

                    
                    <a href="17&#32;&#32;消费者组重平衡能避免吗？.md">17  消费者组重平衡能避免吗？.md</a>

                </li>
                <li>

                    
                    <a href="18&#32;&#32;Kafka中位移提交那些事儿.md">18  Kafka中位移提交那些事儿.md</a>

                </li>
                <li>

                    
                    <a href="19&#32;&#32;CommitFailedException异常怎么处理？.md">19  CommitFailedException异常怎么处理？.md</a>

                </li>
                <li>

                    
                    <a href="20&#32;&#32;多线程开发消费者实例.md">20  多线程开发消费者实例.md</a>

                </li>
                <li>

                    
                    <a href="21&#32;&#32;Java&#32;消费者是如何管理TCP连接的.md">21  Java 消费者是如何管理TCP连接的.md</a>

                </li>
                <li>

                    
                    <a href="22&#32;&#32;消费者组消费进度监控都怎么实现？.md">22  消费者组消费进度监控都怎么实现？.md</a>

                </li>
                <li>

                    
                    <a href="23&#32;&#32;Kafka副本机制详解.md">23  Kafka副本机制详解.md</a>

                </li>
                <li>

                    
                    <a href="24&#32;&#32;请求是怎么被处理的？.md">24  请求是怎么被处理的？.md</a>

                </li>
                <li>

                    
                    <a href="25&#32;&#32;消费者组重平衡全流程解析.md">25  消费者组重平衡全流程解析.md</a>

                </li>
                <li>

                    
                    <a href="26&#32;&#32;你一定不能错过的Kafka控制器.md">26  你一定不能错过的Kafka控制器.md</a>

                </li>
                <li>

                    
                    <a href="27&#32;&#32;关于高水位和Leader&#32;Epoch的讨论.md">27  关于高水位和Leader Epoch的讨论.md</a>

                </li>
                <li>

                    
                    <a href="28&#32;&#32;主题管理知多少.md">28  主题管理知多少.md</a>

                </li>
                <li>

                    
                    <a href="29&#32;&#32;Kafka动态配置了解下？.md">29  Kafka动态配置了解下？.md</a>

                </li>
                <li>

                    
                    <a href="30&#32;&#32;怎么重设消费者组位移？.md">30  怎么重设消费者组位移？.md</a>

                </li>
                <li>

                    
                    <a href="31&#32;&#32;常见工具脚本大汇总.md">31  常见工具脚本大汇总.md</a>

                </li>
                <li>

                    
                    <a href="32&#32;&#32;KafkaAdminClient：Kafka的运维利器.md">32  KafkaAdminClient：Kafka的运维利器.md</a>

                </li>
                <li>

                    
                    <a href="33&#32;&#32;Kafka认证机制用哪家？.md">33  Kafka认证机制用哪家？.md</a>

                </li>
                <li>

                    
                    <a href="34&#32;&#32;云环境下的授权该怎么做？.md">34  云环境下的授权该怎么做？.md</a>

                </li>
                <li>

                    
                    <a href="35&#32;&#32;跨集群备份解决方案MirrorMaker.md">35  跨集群备份解决方案MirrorMaker.md</a>

                </li>
                <li>

                    
                    <a href="36&#32;&#32;你应该怎么监控Kafka？.md">36  你应该怎么监控Kafka？.md</a>

                </li>
                <li>

                    
                    <a href="37&#32;&#32;主流的Kafka监控框架.md">37  主流的Kafka监控框架.md</a>

                </li>
                <li>

                    <a class="current-tab" href="38&#32;&#32;调优Kafka，你做到了吗？.md">38  调优Kafka，你做到了吗？.md</a>
                    

                </li>
                <li>

                    
                    <a href="39&#32;&#32;从0搭建基于Kafka的企业级实时日志流处理平台.md">39  从0搭建基于Kafka的企业级实时日志流处理平台.md</a>

                </li>
                <li>

                    
                    <a href="40&#32;&#32;Kafka&#32;Streams与其他流处理平台的差异在哪里？.md">40  Kafka Streams与其他流处理平台的差异在哪里？.md</a>

                </li>
                <li>

                    
                    <a href="41&#32;&#32;Kafka&#32;Streams&#32;DSL开发实例.md">41  Kafka Streams DSL开发实例.md</a>

                </li>
                <li>

                    
                    <a href="42&#32;&#32;Kafka&#32;Streams在金融领域的应用.md">42  Kafka Streams在金融领域的应用.md</a>

                </li>
                <li>

                    
                    <a href="加餐&#32;&#32;搭建开发环境、阅读源码方法、经典学习资料大揭秘.md">加餐  搭建开发环境、阅读源码方法、经典学习资料大揭秘.md</a>

                </li>
                <li>

                    
                    <a href="结束语&#32;&#32;以梦为马，莫负韶华！.md">结束语  以梦为马，莫负韶华！.md</a>

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
                        <div><h1>38  调优Kafka，你做到了吗？</h1>
<p>你好，我是胡夕。今天我要和你分享的主题是：如何调优 Kafka。</p>
<h2>调优目标</h2>
<p>在做调优之前，我们必须明确优化 Kafka 的目标是什么。通常来说，调优是为了满足系统常见的非功能性需求。在众多的非功能性需求中，性能绝对是我们最关心的那一个。不同的系统对性能有不同的诉求，比如对于数据库用户而言，性能意味着请求的响应时间，用户总是希望查询或更新请求能够被更快地处理完并返回。</p>
<p>对 Kafka 而言，性能一般是指吞吐量和延时。</p>
<p>吞吐量，也就是 TPS，是指 Broker 端进程或 Client 端应用程序每秒能处理的字节数或消息数，这个值自然是越大越好。</p>
<p>延时和我们刚才说的响应时间类似，它表示从 Producer 端发送消息到 Broker 端持久化完成之间的时间间隔。这个指标也可以代表端到端的延时（End-to-End，E2E），也就是从 Producer 发送消息到 Consumer 成功消费该消息的总时长。和 TPS 相反，我们通常希望延时越短越好。</p>
<p>总之，高吞吐量、低延时是我们调优 Kafka 集群的主要目标，一会儿我们会详细讨论如何达成这些目标。在此之前，我想先谈一谈优化漏斗的问题。</p>
<h2>优化漏斗</h2>
<p>优化漏斗是一个调优过程中的分层漏斗，我们可以在每一层上执行相应的优化调整。总体来说，层级越靠上，其调优的效果越明显，整体优化效果是自上而下衰减的，如下图所示：</p>
<p><img src="assets/94486dc0eb55b68855478ef7e5709359.png" alt="img" /></p>
<p><strong>第 1 层：应用程序层</strong>。它是指优化 Kafka 客户端应用程序代码。比如，使用合理的数据结构、缓存计算开销大的运算结果，抑或是复用构造成本高的对象实例等。这一层的优化效果最为明显，通常也是比较简单的。</p>
<p><strong>第 2 层：框架层</strong>。它指的是合理设置 Kafka 集群的各种参数。毕竟，直接修改 Kafka 源码进行调优并不容易，但根据实际场景恰当地配置关键参数的值，还是很容易实现的。</p>
<p><strong>第 3 层：JVM 层</strong>。Kafka Broker 进程是普通的 JVM 进程，各种对 JVM 的优化在这里也是适用的。优化这一层的效果虽然比不上前两层，但有时也能带来巨大的改善效果。</p>
<p><strong>第 4 层：操作系统层</strong>。对操作系统层的优化很重要，但效果往往不如想象得那么好。与应用程序层的优化效果相比，它是有很大差距的。</p>
<h2>基础性调优</h2>
<p>接下来，我就来分别介绍一下优化漏斗的 4 个分层的调优。</p>
<h3>操作系统调优</h3>
<p>我先来说说操作系统层的调优。在操作系统层面，你最好在挂载（Mount）文件系统时禁掉 atime 更新。atime 的全称是 access time，记录的是文件最后被访问的时间。记录 atime 需要操作系统访问 inode 资源，而禁掉 atime 可以避免 inode 访问时间的写入操作，减少文件系统的写操作数。你可以执行<strong>mount -o noatime 命令</strong>进行设置。</p>
<p>至于文件系统，我建议你至少选择 ext4 或 XFS。尤其是 XFS 文件系统，它具有高性能、高伸缩性等特点，特别适用于生产服务器。值得一提的是，在去年 10 月份的 Kafka 旧金山峰会上，有人分享了 ZFS 搭配 Kafka 的案例，我们在专栏[第 8 讲]提到过与之相关的<a href="https://www.confluent.io/kafka-summit-sf18/kafka-on-zfs">数据报告</a>。该报告宣称 ZFS 多级缓存的机制能够帮助 Kafka 改善 I/O 性能，据说取得了不错的效果。如果你的环境中安装了 ZFS 文件系统，你可以尝试将 Kafka 搭建在 ZFS 文件系统上。</p>
<p>另外就是 swap 空间的设置。我个人建议将 swappiness 设置成一个很小的值，比如 1～10 之间，以防止 Linux 的 OOM Killer 开启随意杀掉进程。你可以执行 sudo sysctl vm.swappiness=N 来临时设置该值，如果要永久生效，可以修改 /etc/sysctl.conf 文件，增加 vm.swappiness=N，然后重启机器即可。</p>
<p>操作系统层面还有两个参数也很重要，它们分别是<strong>ulimit -n 和 vm.max_map_count</strong>。前者如果设置得太小，你会碰到 Too Many File Open 这类的错误，而后者的值如果太小，在一个主题数超多的 Broker 机器上，你会碰到<strong>OutOfMemoryError：Map failed</strong>的严重错误，因此，我建议在生产环境中适当调大此值，比如将其设置为 655360。具体设置方法是修改 /etc/sysctl.conf 文件，增加 vm.max_map_count=655360，保存之后，执行 sysctl -p 命令使它生效。</p>
<p>最后，不得不提的就是操作系统页缓存大小了，这对 Kafka 而言至关重要。在某种程度上，我们可以这样说：给 Kafka 预留的页缓存越大越好，最小值至少要容纳一个日志段的大小，也就是 Broker 端参数 log.segment.bytes 的值。该参数的默认值是 1GB。预留出一个日志段大小，至少能保证 Kafka 可以将整个日志段全部放入页缓存，这样，消费者程序在消费时能直接命中页缓存，从而避免昂贵的物理磁盘 I/O 操作。</p>
<h3>JVM 层调优</h3>
<p>说完了操作系统层面的调优，我们来讨论下 JVM 层的调优，其实，JVM 层的调优，我们还是要重点关注堆设置以及 GC 方面的性能。</p>
<p>\1. 设置堆大小。</p>
<p>如何为 Broker 设置堆大小，这是很多人都感到困惑的问题。我来给出一个朴素的答案：<strong>将你的 JVM 堆大小设置成 6～8GB</strong>。</p>
<p>在很多公司的实际环境中，这个大小已经被证明是非常合适的，你可以安心使用。如果你想精确调整的话，我建议你可以查看 GC log，特别是关注 Full GC 之后堆上存活对象的总大小，然后把堆大小设置为该值的 1.5～2 倍。如果你发现 Full GC 没有被执行过，手动运行 jmap -histo:live &lt; pid &gt; 就能人为触发 Full GC。</p>
<p>2.GC 收集器的选择。</p>
<p><strong>我强烈建议你使用 G1 收集器，主要原因是方便省事，至少比 CMS 收集器的优化难度小得多</strong>。另外，你一定要尽力避免 Full GC 的出现。其实，不论使用哪种收集器，都要竭力避免 Full GC。在 G1 中，Full GC 是单线程运行的，它真的非常慢。如果你的 Kafka 环境中经常出现 Full GC，你可以配置 JVM 参数 -XX:+PrintAdaptiveSizePolicy，来探查一下到底是谁导致的 Full GC。</p>
<p>使用 G1 还很容易碰到的一个问题，就是<strong>大对象（Large Object）</strong>，反映在 GC 上的错误，就是“too many humongous allocations”。所谓的大对象，一般是指至少占用半个区域（Region）大小的对象。举个例子，如果你的区域尺寸是 2MB，那么超过 1MB 大小的对象就被视为是大对象。要解决这个问题，除了增加堆大小之外，你还可以适当地增加区域大小，设置方法是增加 JVM 启动参数 -XX:+G1HeapRegionSize=N。默认情况下，如果一个对象超过了 N/2，就会被视为大对象，从而直接被分配在大对象区。如果你的 Kafka 环境中的消息体都特别大，就很容易出现这种大对象分配的问题。</p>
<h3>Broker 端调优</h3>
<p>我们继续沿着漏斗往上走，来看看 Broker 端的调优。</p>
<p>Broker 端调优很重要的一个方面，就是合理地设置 Broker 端参数值，以匹配你的生产环境。不过，后面我们在讨论具体的调优目标时再详细说这部分内容。这里我想先讨论另一个优化手段，<strong>即尽力保持客户端版本和 Broker 端版本一致</strong>。不要小看版本间的不一致问题，它会令 Kafka 丧失很多性能收益，比如 Zero Copy。下面我用一张图来说明一下。</p>
<p><img src="assets/5310d7d29235b080c872e0a9eb396e6e.png" alt="img" /></p>
<p>图中蓝色的 Producer、Consumer 和 Broker 的版本是相同的，它们之间的通信可以享受 Zero Copy 的快速通道；相反，一个低版本的 Consumer 程序想要与 Producer、Broker 交互的话，就只能依靠 JVM 堆中转一下，丢掉了快捷通道，就只能走慢速通道了。因此，在优化 Broker 这一层时，你只要保持服务器端和客户端版本的一致，就能获得很多性能收益了。</p>
<h3>应用层调优</h3>
<p>现在，我们终于来到了漏斗的最顶层。其实，这一层的优化方法各异，毕竟每个应用程序都是不一样的。不过，有一些公共的法则依然是值得我们遵守的。</p>
<ul>
<li><strong>不要频繁地创建 Producer 和 Consumer 对象实例</strong>。构造这些对象的开销很大，尽量复用它们。</li>
<li><strong>用完及时关闭</strong>。这些对象底层会创建很多物理资源，如 Socket 连接、ByteBuffer 缓冲区等。不及时关闭的话，势必造成资源泄露。</li>
<li><strong>合理利用多线程来改善性能</strong>。Kafka 的 Java Producer 是线程安全的，你可以放心地在多个线程中共享同一个实例；而 Java Consumer 虽不是线程安全的，但我们在专栏[第 20 讲]讨论过多线程的方案，你可以回去复习一下。</li>
</ul>
<h2>性能指标调优</h2>
<p>接下来，我会给出调优各个目标的参数配置以及具体的配置原因，希望它们能够帮助你更有针对性地调整你的 Kafka 集群。</p>
<h3>调优吞吐量</h3>
<p>首先是调优吞吐量。很多人对吞吐量和延时之间的关系似乎有些误解。比如有这样一种提法还挺流行的：假设 Kafka 每发送一条消息需要花费 2ms，那么延时就是 2ms。显然，吞吐量就应该是 500 条 / 秒，因为 1 秒可以发送 1 / 0.002 = 500 条消息。因此，吞吐量和延时的关系可以用公式来表示：TPS = 1000 / Latency(ms)。但实际上，吞吐量和延时的关系远不是这么简单。</p>
<p>我们以 Kafka Producer 为例。假设它以 2ms 的延时来发送消息，如果每次只是发送一条消息，那么 TPS 自然就是 500 条 / 秒。但如果 Producer 不是每次发送一条消息，而是在发送前等待一段时间，然后统一发送<strong>一批</strong>消息，比如 Producer 每次发送前先等待 8ms，8ms 之后，Producer 共缓存了 1000 条消息，此时总延时就累加到 10ms（即 2ms + 8ms）了，而 TPS 等于 1000 / 0.01 = 100,000 条 / 秒。由此可见，虽然延时增加了 4 倍，但 TPS 却增加了将近 200 倍。这其实也是批次化（batching）或微批次化（micro-batching）目前会很流行的原因。</p>
<p>在实际环境中，用户似乎总是愿意用较小的延时增加的代价，去换取 TPS 的显著提升。毕竟，从 2ms 到 10ms 的延时增加通常是可以忍受的。事实上，Kafka Producer 就是采取了这样的设计思想。</p>
<p>当然，你可能会问：发送一条消息需要 2ms，那么等待 8ms 就能累积 1000 条消息吗？答案是可以的！Producer 累积消息时，一般仅仅是将消息发送到内存中的缓冲区，而发送消息却需要涉及网络 I/O 传输。内存操作和 I/O 操作的时间量级是不同的，前者通常是几百纳秒级别，而后者则是从毫秒到秒级别不等，因此，Producer 等待 8ms 积攒出的消息数，可能远远多于同等时间内 Producer 能够发送的消息数。</p>
<p>好了，说了这么多，我们该怎么调优 TPS 呢？我来跟你分享一个参数列表。</p>
<p><img src="assets/7aec00207dc149bd804d20df6e3b9ccb.jpg" alt="img" /></p>
<p>我稍微解释一下表格中的内容。</p>
<p>Broker 端参数 num.replica.fetchers 表示的是 Follower 副本用多少个线程来拉取消息，默认使用 1 个线程。如果你的 Broker 端 CPU 资源很充足，不妨适当调大该参数值，加快 Follower 副本的同步速度。因为在实际生产环境中，<strong>配置了 acks=all 的 Producer 程序吞吐量被拖累的首要因素，就是副本同步性能</strong>。增加这个值后，你通常可以看到 Producer 端程序的吞吐量增加。</p>
<p>另外需要注意的，就是避免经常性的 Full GC。目前不论是 CMS 收集器还是 G1 收集器，其 Full GC 采用的是 Stop The World 的单线程收集策略，非常慢，因此一定要避免。</p>
<p><strong>在 Producer 端，如果要改善吞吐量，通常的标配是增加消息批次的大小以及批次缓存时间，即 batch.size 和 linger.ms</strong>。目前它们的默认值都偏小，特别是默认的 16KB 的消息批次大小一般都不适用于生产环境。假设你的消息体大小是 1KB，默认一个消息批次也就大约 16 条消息，显然太小了。我们还是希望 Producer 能一次性发送更多的消息。</p>
<p>除了这两个，你最好把压缩算法也配置上，以减少网络 I/O 传输量，从而间接提升吞吐量。当前，和 Kafka 适配最好的两个压缩算法是<strong>LZ4 和 zstd</strong>，不妨一试。</p>
<p>同时，由于我们的优化目标是吞吐量，最好不要设置 acks=all 以及开启重试。前者引入的副本同步时间通常都是吞吐量的瓶颈，而后者在执行过程中也会拉低 Producer 应用的吞吐量。</p>
<p>最后，如果你在多个线程中共享一个 Producer 实例，就可能会碰到缓冲区不够用的情形。倘若频繁地遭遇 TimeoutException：Failed to allocate memory within the configured max blocking time 这样的异常，那么你就必须显式地增加<strong>buffer.memory</strong>参数值，确保缓冲区总是有空间可以申请的。</p>
<p>说完了 Producer 端，我们来说说 Consumer 端。Consumer 端提升吞吐量的手段是有限的，你可以利用多线程方案增加整体吞吐量，也可以增加 fetch.min.bytes 参数值。默认是 1 字节，表示只要 Kafka Broker 端积攒了 1 字节的数据，就可以返回给 Consumer 端，这实在是太小了。我们还是让 Broker 端一次性多返回点数据吧。</p>
<h3>调优延时</h3>
<p>讲完了调优吞吐量，我们来说说如何优化延时，下面是调优延时的参数列表。</p>
<p><img src="assets/2688329a0614601fed497f3858c98e3a.jpg" alt="img" /></p>
<p>在 Broker 端，我们依然要增加 num.replica.fetchers 值以加快 Follower 副本的拉取速度，减少整个消息处理的延时。</p>
<p>在 Producer 端，我们希望消息尽快地被发送出去，因此不要有过多停留，所以必须设置 linger.ms=0，同时不要启用压缩。因为压缩操作本身要消耗 CPU 时间，会增加消息发送的延时。另外，最好不要设置 acks=all。我们刚刚在前面说过，Follower 副本同步往往是降低 Producer 端吞吐量和增加延时的首要原因。</p>
<p>在 Consumer 端，我们保持 fetch.min.bytes=1 即可，也就是说，只要 Broker 端有能返回的数据，立即令其返回给 Consumer，缩短 Consumer 消费延时。</p>
<h2>小结</h2>
<p>好了，我们来小结一下。今天，我跟你分享了 Kafka 调优方面的内容。我们先从调优目标开始说起，然后我给出了调优层次漏斗，接着我分享了一些基础性调优，包括操作系统层调优、JVM 层调优以及应用程序调优等。最后，针对 Kafka 关心的两个性能指标吞吐量和延时，我分别从 Broker、Producer 和 Consumer 三个维度给出了一些参数值设置的最佳实践。</p>
<p>最后，我来分享一个性能调优的真实小案例。</p>
<p>曾经，我碰到过一个线上环境的问题：该集群上 Consumer 程序一直表现良好，但是某一天，它的性能突然下降，表现为吞吐量显著降低。我在查看磁盘读 I/O 使用率时，发现其明显上升，但之前该 Consumer Lag 很低，消息读取应该都能直接命中页缓存。此时磁盘读突然飙升，我就怀疑有其他程序写入了页缓存。后来经过排查，我发现果然有一个测试 Console Consumer 程序启动，“污染”了部分页缓存，导致主业务 Consumer 读取消息不得不走物理磁盘，因此吞吐量下降。找到了真实原因，解决起来就简单多了。</p>
<p>其实，我给出这个案例的真实目的是想说，对于性能调优，我们最好按照今天给出的步骤一步一步地窄化和定位问题。一旦定位了原因，后面的优化就水到渠成了。</p>
<p><img src="assets/d40b07ca7bcc0fc43c5266b0b2c81c38.jpg" alt="img" /></p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="37&#32;&#32;主流的Kafka监控框架.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="39&#32;&#32;从0搭建基于Kafka的企业级实时日志流处理平台.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b43459eab0170ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
            document.getElementById("tip").innerHTML = "<a href='https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/Kafka%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98/&quot;&#32;+&#32;cookie&#32;+&#32;&quot;'>跳转到上次进度</a>"
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
