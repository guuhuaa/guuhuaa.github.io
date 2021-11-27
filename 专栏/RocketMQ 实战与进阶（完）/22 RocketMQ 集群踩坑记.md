<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>22 RocketMQ 集群踩坑记.md</title>
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

                    
                    <a href="01&#32;搭建学习环境准备篇.md">01 搭建学习环境准备篇.md</a>

                </li>
                <li>

                    
                    <a href="02&#32;RocketMQ&#32;核心概念扫盲篇.md">02 RocketMQ 核心概念扫盲篇.md</a>

                </li>
                <li>

                    
                    <a href="03&#32;消息发送&#32;API&#32;详解与版本变迁说明.md">03 消息发送 API 详解与版本变迁说明.md</a>

                </li>
                <li>

                    
                    <a href="04&#32;结合实际应用场景谈消息发送.md">04 结合实际应用场景谈消息发送.md</a>

                </li>
                <li>

                    
                    <a href="05&#32;消息发送核心参数与工作原理详解.md">05 消息发送核心参数与工作原理详解.md</a>

                </li>
                <li>

                    
                    <a href="06&#32;消息发送常见错误与解决方案.md">06 消息发送常见错误与解决方案.md</a>

                </li>
                <li>

                    
                    <a href="07&#32;事务消息使用及方案选型思考.md">07 事务消息使用及方案选型思考.md</a>

                </li>
                <li>

                    
                    <a href="08&#32;消息消费&#32;API&#32;与版本变迁说明.md">08 消息消费 API 与版本变迁说明.md</a>

                </li>
                <li>

                    
                    <a href="09&#32;DefaultMQPushConsumer&#32;核心参数与工作原理.md">09 DefaultMQPushConsumer 核心参数与工作原理.md</a>

                </li>
                <li>

                    
                    <a href="10&#32;DefaultMQPushConsumer&#32;使用示例与注意事项.md">10 DefaultMQPushConsumer 使用示例与注意事项.md</a>

                </li>
                <li>

                    
                    <a href="11&#32;DefaultLitePullConsumer&#32;核心参数与实战.md">11 DefaultLitePullConsumer 核心参数与实战.md</a>

                </li>
                <li>

                    
                    <a href="12&#32;结合实际场景再聊&#32;DefaultLitePullConsumer&#32;的使用.md">12 结合实际场景再聊 DefaultLitePullConsumer 的使用.md</a>

                </li>
                <li>

                    
                    <a href="13&#32;结合实际场景顺序消费、消息过滤实战.md">13 结合实际场景顺序消费、消息过滤实战.md</a>

                </li>
                <li>

                    
                    <a href="14&#32;消息消费积压问题排查实战.md">14 消息消费积压问题排查实战.md</a>

                </li>
                <li>

                    
                    <a href="15&#32;RocketMQ&#32;常用命令实战.md">15 RocketMQ 常用命令实战.md</a>

                </li>
                <li>

                    
                    <a href="16&#32;RocketMQ&#32;集群性能摸高.md">16 RocketMQ 集群性能摸高.md</a>

                </li>
                <li>

                    
                    <a href="17&#32;RocketMQ&#32;集群性能调优.md">17 RocketMQ 集群性能调优.md</a>

                </li>
                <li>

                    
                    <a href="18&#32;RocketMQ&#32;集群平滑运维.md">18 RocketMQ 集群平滑运维.md</a>

                </li>
                <li>

                    
                    <a href="19&#32;RocketMQ&#32;集群监控（一）.md">19 RocketMQ 集群监控（一）.md</a>

                </li>
                <li>

                    
                    <a href="20&#32;RocketMQ&#32;集群监控（二）.md">20 RocketMQ 集群监控（二）.md</a>

                </li>
                <li>

                    
                    <a href="21&#32;RocketMQ&#32;集群告警.md">21 RocketMQ 集群告警.md</a>

                </li>
                <li>

                    <a class="current-tab" href="22&#32;RocketMQ&#32;集群踩坑记.md">22 RocketMQ 集群踩坑记.md</a>
                    

                </li>
                <li>

                    
                    <a href="23&#32;消息轨迹、ACL&#32;与多副本搭建.md">23 消息轨迹、ACL 与多副本搭建.md</a>

                </li>
                <li>

                    
                    <a href="24&#32;RocketMQ-Console&#32;常用页面指标获取逻辑.md">24 RocketMQ-Console 常用页面指标获取逻辑.md</a>

                </li>
                <li>

                    
                    <a href="25&#32;RocketMQ&#32;Nameserver&#32;背后的设计理念.md">25 RocketMQ Nameserver 背后的设计理念.md</a>

                </li>
                <li>

                    
                    <a href="26&#32;Java&#32;并发编程实战.md">26 Java 并发编程实战.md</a>

                </li>
                <li>

                    
                    <a href="27&#32;从&#32;RocketMQ&#32;学基于文件的编程模式（一）.md">27 从 RocketMQ 学基于文件的编程模式（一）.md</a>

                </li>
                <li>

                    
                    <a href="28&#32;从&#32;RocketMQ&#32;学基于文件的编程模式（二）.md">28 从 RocketMQ 学基于文件的编程模式（二）.md</a>

                </li>
                <li>

                    
                    <a href="29&#32;从&#32;RocketMQ&#32;学&#32;Netty&#32;网络编程技巧.md">29 从 RocketMQ 学 Netty 网络编程技巧.md</a>

                </li>
                <li>

                    
                    <a href="30&#32;RocketMQ&#32;学习方法之我见.md">30 RocketMQ 学习方法之我见.md</a>

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
                        <div><h1>22 RocketMQ 集群踩坑记</h1>
<h3>集群节点进程神秘消失</h3>
<h4><strong>现象描述</strong></h4>
<p>接到告警和运维反馈，一个 RocketMQ 的节点不见了。此类现象在以前从未发生过，消失肯定有原因，开始查找日志，从集群的 broker.log、stats.log、storeerror.log、store.log、watermark.log 到系统的 message 日志没发现错误日志。集群流量出入在正常水位、CPU 使用率、CPU Load、磁盘 IO、内存、带宽等无明显变化。</p>
<h4><strong>原因分析</strong></h4>
<p>继续查原因，最终通过 history 查看了历史运维操作。发现运维同学在启动 Broker 时没有在后台启动，而是在当前 session 中直接启动了。</p>
<pre><code>sh bin/mqbroker -c conf/broker-a.conf

</code></pre>
<p>问题即出现在此命令，当 session 过期时 Broker 节点也就退出了。</p>
<h4><strong>解决方法</strong></h4>
<p>标准化运维操作，对运维的每次操作进行评审，将标准化的操作实现自动化运维就更好了。</p>
<p>正确启动 Broker 方式：</p>
<pre><code>nohup sh bin/mqbroker -c conf/broker-a.conf &amp;

</code></pre>
<h3>Master 节点 CPU 莫名飙高</h3>
<h4><strong>现象描述</strong></h4>
<p>RocketMQ 主节点 CPU 频繁飙高后回落，业务发送超时严重，由于两个从节点部署在同一个机器上，从节点还出现了直接挂掉的情况。</p>
<p>主节点 CPU 毛刺截图：</p>
<p><img src="assets/20200910105626655.png" alt="img" /></p>
<p>从节点 CPU 毛刺截图：</p>
<p><img src="assets/20200910105701883.png" alt="img" /></p>
<p>说明：中间缺失部分为掉线，没有采集到的情况。</p>
<p><strong>系统错误日志一</strong></p>
<pre><code>2020-03-16T17:56:07.505715+08:00 VECS0xxxx kernel: &lt;IRQ&gt;  [&lt;ffffffff81143c31&gt;] ? __alloc_pages_nodemask+0x7e1/0x960
2020-03-16T17:56:07.505717+08:00 VECS0xxxx kernel: java: page allocation failure. order:0, mode:0x20
2020-03-16T17:56:07.505719+08:00 VECS0xxxx kernel: Pid: 12845, comm: java Not tainted 2.6.32-754.17.1.el6.x86_64 #1
2020-03-16T17:56:07.505721+08:00 VECS0xxxx kernel: Call Trace:
2020-03-16T17:56:07.505724+08:00 VECS0xxxx kernel: &lt;IRQ&gt;  [&lt;ffffffff81143c31&gt;] ? __alloc_pages_nodemask+0x7e1/0x960
2020-03-16T17:56:07.505726+08:00 VECS0xxxx kernel: [&lt;ffffffff8148e700&gt;] ? dev_queue_xmit+0xd0/0x360
2020-03-16T17:56:07.505729+08:00 VECS0xxxx kernel: [&lt;ffffffff814cb3e2&gt;] ? ip_finish_output+0x192/0x380

</code></pre>
<p><strong>系统错误日志二</strong></p>
<pre><code> 30 2020-03-27T10:35:28.769900+08:00 VECSxxxx kernel: INFO: task AliYunDunUpdate:29054 blocked for more than 120 seconds.
 31 2020-03-27T10:35:28.769932+08:00 VECSxxxx kernel:      Not tainted 2.6.32-754.17.1.el6.x86_64 #1
 32 2020-03-27T10:35:28.771650+08:00 VECS0xxxx kernel: &quot;echo 0 &gt; /proc/sys/kernel/hung_task_timeout_secs&quot; disables this message.
 33 2020-03-27T10:35:28.774631+08:00 VECS0xxxx kernel: AliYunDunUpda D ffffffff815592fb     0 29054      1 0x10000080
 34 2020-03-27T10:35:28.777500+08:00 VECS0xxxx kernel: ffff8803ef75baa0 0000000000000082 ffff8803ef75ba68 ffff8803ef75ba64

</code></pre>
<p>说明：系统日志显示错误“page allocation failure”和“blocked for more than 120 second”错误，日志目录 /var/log/messages。</p>
<p><strong>GC 日志</strong></p>
<pre><code>2020-03-16T17:49:13.785+0800: 13484510.599: Total time for which application threads were stopped: 0.0072354 seconds, Stopping threads took: 0.0001536 seconds
2020-03-16T18:01:23.149+0800: 13485239.963: [GC pause (G1 Evacuation Pause) (young) 13485239.965: [G1Ergonomics (CSet Construction) start choosing CSet, _pending_cards: 7738, predicted base time: 5.74 ms, remaining time: 194.26 ms, target pause time: 200.00 ms]
 13485239.965: [G1Ergonomics (CSet Construction) add young regions to CSet, eden: 255 regions, survivors: 1 regions, predicted young region time: 0.52 ms]
 13485239.965: [G1Ergonomics (CSet Construction) finish choosing CSet, eden: 255 regions, survivors: 1 regions, old: 0 regions, predicted pause time: 6.26 ms, target pause time: 200.00 ms]
, 0.0090963 secs]
   [Parallel Time: 2.3 ms, GC Workers: 23]
      [GC Worker Start (ms): Min: 13485239965.1, Avg: 13485239965.4, Max: 13485239965.7, Diff: 0.6]
      [Ext Root Scanning (ms): Min: 0.0, Avg: 0.3, Max: 0.6, Diff: 0.6, Sum: 8.0]
      [Update RS (ms): Min: 0.1, Avg: 0.3, Max: 0.6, Diff: 0.5, Sum: 7.8]
         [Processed Buffers: Min: 2, Avg: 5.7, Max: 11, Diff: 9, Sum: 131]
      [Scan RS (ms): Min: 0.0, Avg: 0.0, Max: 0.1, Diff: 0.1, Sum: 0.8]
      [Code Root Scanning (ms): Min: 0.0, Avg: 0.0, Max: 0.0, Diff: 0.0, Sum: 0.3]
      [Object Copy (ms): Min: 0.2, Avg: 0.5, Max: 0.7, Diff: 0.4, Sum: 11.7]
      [Termination (ms): Min: 0.0, Avg: 0.0, Max: 0.0, Diff: 0.0, Sum: 0.3]
         [Termination Attempts: Min: 1, Avg: 1.0, Max: 1, Diff: 0, Sum: 23]
      [GC Worker Other (ms): Min: 0.0, Avg: 0.2, Max: 0.3, Diff: 0.3, Sum: 3.6]
      [GC Worker Total (ms): Min: 1.0, Avg: 1.4, Max: 1.9, Diff: 0.8, Sum: 32.6]
      [GC Worker End (ms): Min: 13485239966.7, Avg: 13485239966.9, Max: 13485239967.0, Diff: 0.3]
   [Code Root Fixup: 0.0 ms]
   [Code Root Purge: 0.0 ms]
   [Clear CT: 0.9 ms]
   [Other: 5.9 ms]
      [Choose CSet: 0.0 ms]
      [Ref Proc: 1.9 ms]
      [Ref Enq: 0.0 ms]
      [Redirty Cards: 1.0 ms]
      [Humongous Register: 0.0 ms]
      [Humongous Reclaim: 0.0 ms]
      [Free CSet: 0.2 ms]
   [Eden: 4080.0M(4080.0M)-&gt;0.0B(4080.0M) Survivors: 16.0M-&gt;16.0M Heap: 4176.5M(8192.0M)-&gt;96.5M(8192.0M)]
 [Times: user=0.05 sys=0.00, real=0.01 secs]

</code></pre>
<p>说明：GC 日志正常。</p>
<p><strong>Broker 错误日志</strong></p>
<pre><code>2020-03-16 17:55:15 ERROR BrokerControllerScheduledThread1 - SyncTopicConfig Exception, x.x.x.x:10911 
org.apache.rocketmq.remoting.exception.RemotingTimeoutException: wait response on the channel &lt;x.x.x.x:10909&gt; timeout, 3000(ms)
        at org.apache.rocketmq.remoting.netty.NettyRemotingAbstract.invokeSyncImpl(NettyRemotingAbstract.java:427) ~[rocketmq-remoting-4.5.2.jar:4.5.2]
        at org.apache.rocketmq.remoting.netty.NettyRemotingClient.invokeSync(NettyRemotingClient.java:375) ~[rocketmq-remoting-4.5.2.jar:4.5.2]

</code></pre>
<p>说明：通过查看 RocketMQ 的集群和 GC 日志，只能说明但是网络不可用，造成主从同步问题；并未发现 Broker 自身出问题了。</p>
<h4><strong>原因分析</strong></h4>
<p>系统使用 CentOS 6，内核版本为 2.6。通过摸排并未发现 broker 和 GC 本身的问题，却发现了系统 message 日志有频繁的“page allocation failure”和“blocked for more than 120 second”错误。所以将目光聚焦在系统层面，通过尝试系统参数设置，例如：min_free_kbytes 和 zone_reclaim_mode，然而并不能消除 CPU 毛刺问题。通过与社区朋友的会诊讨论，内核版本 2.6 操作系统内存回收存在 Bug。我们决定更换集群的操作系统。</p>
<h4><strong>解决办法</strong></h4>
<p>将集群的 CentOS 6 升级到 CentOS 7，内核版本也从 2.6 升级到了 3.10，升级后 CPU 毛刺问题不在乎出现。升级方式采取的方式先扩容后缩容，先把 CentOS 7 的节点加入集群后，再将 CentOS 6 的节点移除，详见前面实战部分“RocketMQ 集群平滑运维”。</p>
<pre><code>Linux version 3.10.0-1062.4.1.el7.x86_64 (<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="bfd2d0dcd4ddcad6d3dbffd4ddcad6d3dbdacd91ddccc6cc91dcdad1cbd0cc91d0cdd8">[email&#160;protected]</a>) (gcc version 4.8.5 20150623 (Red Hat 4.8.5-39) (GCC) ) #1 SMP Fri Oct 18 17:15:30 UTC 2019

</code></pre>
<h3>集群频繁抖动发送超时</h3>
<h4><strong>现象描述</strong></h4>
<p>监控和业务同学反馈发送超时，而且频繁出现。具体现象如下图。</p>
<p><strong>预热现象</strong></p>
<p><img src="assets/20200910095246617.jpg" alt="img" /></p>
<p><img src="assets/20200910095328878.jpg" alt="img" /></p>
<p>说明：上图分别为开启预热时（<code>warmMapedFileEnable=true</code>）集群的发送 RT 监控、Broker 开启预热设置时的日志。</p>
<p><strong>内存传输现象</strong></p>
<p><img src="assets/20200910095358560.jpg" alt="CPU 抖动" /></p>
<p><img src="assets/20200910095449761.jpg" alt="img" /></p>
<p><img src="assets/20200910095559121.jpg" alt="img" /></p>
<p>说明：上图分别为开启堆外内存传输（<code>transferMsgByHeap=fals</code>e）时的 CPU 抖动截图、系统内存分配不足截图、Broker 日志截图。</p>
<h4><strong>原因分析</strong></h4>
<p>上面展现的两种显现均会导致集群 CPU 抖动、客户端发送超时，对业务造成影响。</p>
<p>预热设置：在预热文件时会填充 1 个 G 的假值 0 作为占位符，提前分配物理内存，防止消息写入时发生缺页异常。然而往往伴随着磁盘写入耗时过长、CPU 小幅抖动、业务具体表现为发送耗时过长，超时错误增多。关闭预热配置从集群 TPS 摸高情况来看并未有明显的差异，但是从稳定性角度关闭却很有必要。</p>
<p>堆外内存：transferMsgByHeap 设置为 false 时，通过堆外内存传输数据，相比堆内存传输减少了数据拷贝、零字节拷贝、效率更高。但是可能造成堆外内存分配不够，触发系统内存回收和落盘操作，设置为 true 时运行更加平稳。</p>
<h4><strong>解决办法</strong></h4>
<p>预热 warmMapedFileEnable 默认为 false，保持默认即可。如果开启了，可以通过热更新关闭。</p>
<pre><code>bin/mqadmin updateBrokerConfig -b x.x.x.x:10911 -n x.x.x.x:9876 -k warmMapedFileEnable -v false

</code></pre>
<p>内存传输参数 transferMsgByHeap 默认为 true（即：通过堆内内存传输）保持默认即可。如果关闭了，可以通过热更新开启。</p>
<pre><code>bin/mqadmin updateBrokerConfig -b x.x.x.x:10911 -n x.x.x.x:9876 -k transferMsgByHeap -v true

</code></pre>
<h3>用了此属性消费性能下降一半</h3>
<h4><strong>现象描述</strong></h4>
<p>配置均采用 8C16G，RocketMQ 的消费线程 20 个，通过测试消费性能在 1.5 万 tps 左右。通过 tcpdump 显示在消费的机器存在频繁的域名解析过程；10.x.x.185 向 DNS 服务器 100.x.x.136.domain 和 10.x.x.138.domain 请求解析。而 10.x.x.185 这台机器又是消息发送者的机器 IP，测试的发送和消费分别部署在两台机器上。</p>
<p>问题：消费时为何会有消息发送方的 IP 呢？而且该 IP 还不断进行域名解析。</p>
<p><img src="assets/20200911100907927.jpg" alt="img" /></p>
<h4><strong>原因分析</strong></h4>
<p>通过 dump 线程堆栈，如下图：</p>
<p><img src="assets/20200911101209514.jpg" alt="img" /></p>
<p>代码定位：在消费时有通过 MessageExt.bornHost.getBornHostNameString 获取消费这信息。</p>
<pre><code>public class MessageExt extends Message {
    private static final long serialVersionUID = 5720810158625748049L;
    private int queueId;
    private int storeSize;
    private long queueOffset;
    private int sysFlag;
    private long bornTimestamp;
    private SocketAddress bornHost;
    private long storeTimestamp;
    private SocketAddress storeHost;
    private String msgId;
    private long commitLogOffset;
    private int bodyCRC;
    private int reconsumeTimes;
    private long preparedTransactionOffset;
}

</code></pre>
<p>调用 GetBornHostNameString 获取 HostName 时会根据 IP 反查 DNS 服务器：</p>
<pre><code>InetSocketAddress inetSocketAddress = (InetSocketAddress)this.bornHost;
return inetSocketAddress.getAddress().getHostName();

</code></pre>
<h4><strong>解决办法</strong></h4>
<p>消费的时候不要使用 MessageExt.bornHost.getBornHostNameString 即可，去掉该属性，配置 8C16G 的机器消费性能在 3 万 TPS，提升了 1 倍。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="21&#32;RocketMQ&#32;集群告警.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="23&#32;消息轨迹、ACL&#32;与多副本搭建.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script data-cfasync="false" src="../../cdn-cgi/scripts/5c5dd728/cloudflare-static/email-decode.min.js"></script><script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b434b29ad3670ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
            document.getElementById("tip").innerHTML = "<a href='https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/RocketMQ%20%E5%AE%9E%E6%88%98%E4%B8%8E%E8%BF%9B%E9%98%B6%EF%BC%88%E5%AE%8C%EF%BC%89/&quot;&#32;+&#32;cookie&#32;+&#32;&quot;'>跳转到上次进度</a>"
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
