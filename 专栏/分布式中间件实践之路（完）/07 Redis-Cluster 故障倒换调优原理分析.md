<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>07 Redis-Cluster 故障倒换调优原理分析.md</title>
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

                    
                    <a href="01&#32;开篇词：从中间件开始学习分布式.md">01 开篇词：从中间件开始学习分布式.md</a>

                </li>
                <li>

                    
                    <a href="02&#32;走进分布式中间件（课前必读）.md">02 走进分布式中间件（课前必读）.md</a>

                </li>
                <li>

                    
                    <a href="03&#32;主流分布式缓存方案的解读及比较.md">03 主流分布式缓存方案的解读及比较.md</a>

                </li>
                <li>

                    
                    <a href="04&#32;分布式一致性协议&#32;Gossip&#32;和&#32;Redis&#32;集群原理解析.md">04 分布式一致性协议 Gossip 和 Redis 集群原理解析.md</a>

                </li>
                <li>

                    
                    <a href="05&#32;基于&#32;Redis&#32;的分布式缓存实现及加固策略.md">05 基于 Redis 的分布式缓存实现及加固策略.md</a>

                </li>
                <li>

                    
                    <a href="06&#32;Redis&#32;实际应用中的异常场景及其根因分析和解决方案.md">06 Redis 实际应用中的异常场景及其根因分析和解决方案.md</a>

                </li>
                <li>

                    <a class="current-tab" href="07&#32;Redis-Cluster&#32;故障倒换调优原理分析.md">07 Redis-Cluster 故障倒换调优原理分析.md</a>
                    

                </li>
                <li>

                    
                    <a href="08&#32;基于&#32;Redis&#32;的分布式锁实现及其踩坑案例.md">08 基于 Redis 的分布式锁实现及其踩坑案例.md</a>

                </li>
                <li>

                    
                    <a href="09&#32;分布式一致性算法&#32;Raft&#32;和&#32;Etcd&#32;原理解析.md">09 分布式一致性算法 Raft 和 Etcd 原理解析.md</a>

                </li>
                <li>

                    
                    <a href="10&#32;基于&#32;Etcd&#32;的分布式锁实现原理及方案.md">10 基于 Etcd 的分布式锁实现原理及方案.md</a>

                </li>
                <li>

                    
                    <a href="11&#32;主流的分布式消息队列方案解读及比较.md">11 主流的分布式消息队列方案解读及比较.md</a>

                </li>
                <li>

                    
                    <a href="12&#32;搭建基于&#32;Kafka&#32;和&#32;ZooKeeper&#32;的分布式消息队列.md">12 搭建基于 Kafka 和 ZooKeeper 的分布式消息队列.md</a>

                </li>
                <li>

                    
                    <a href="13&#32;深入解读基于&#32;Kafka&#32;和&#32;ZooKeeper&#32;的分布式消息队列原理.md">13 深入解读基于 Kafka 和 ZooKeeper 的分布式消息队列原理.md</a>

                </li>
                <li>

                    
                    <a href="14&#32;深入浅出解读&#32;Kafka&#32;的可靠性机制.md">14 深入浅出解读 Kafka 的可靠性机制.md</a>

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
                        <div><h1>07 Redis-Cluster 故障倒换调优原理分析</h1>
<p>Redis-Cluster 是 Redis 官方推出的集群方案，其分布式一致性协议基于 Gossip 算法（第03课中已经详细介绍）。当 Redis-Cluster 出现主节点故障后，集群会经历故障检测、选举、故障倒换三大步骤，在此期间 Redis-Cluster 是不能提供服务的，鉴于此，优化这三个步骤的耗时，便是保障集群可用性、提升性能的关键点之一。</p>
<p>需要说明的是，优化耗时并没有普适性的方案，而是需要根据集群的规模和应用场景有针对性的优化，因此，犹如 JVM 的优化，掌握优化的原理才能“治本”，以不变应万变。</p>
<h3>1. Redis-Cluster 故障检测原理及优化分析</h3>
<p>Redis-Cluster 中出现主节点故障后，检测故障需要经历单节点视角检测、检测信息传播、下线判决三个步骤，下文将结合源码分析。</p>
<h4>1.1 单点视角检测</h4>
<p>在第 03 课中介绍过，集群中的每个节点都会定期通过集群内部通信总线向集群中的其它节点发送 PING 消息，用于检测对方是否在线。如果接收 PING 消息的节点没有在规定的时间内（<code>cluster_node_timeout</code>）向发送 PING 消息的节点返回 PONG 消息，那么，发送 PING 消息的节点就会将接收 PING 消息的节点标注为疑似下线状态（Probable Fail，PFAIL）。如下源码：</p>
<p><img src="assets/b77d4f90-a2ea-11e8-9b2d-01357ecc007a" alt="enter image description here" /></p>
<p>需要注意的是，判断 PFAIL 的依据也是参数 <code>cluster_node_timeout</code>。如果 <code>cluster_node_timeout</code> 设置过大，就会造成故障的主节点不能及时被检测到，集群恢复耗时增加，进而造成集群可用性降低。</p>
<h4>1.2 检测信息传播</h4>
<p>集群中的各个节点会通过相互发送消息的方式来交换自己掌握的集群中各个节点的状态信息，如在线、疑似下线（PFAIL）、下线（FAIL）。例如，当一个主节点 A 通过消息得知主节点 B 认为主节点 C 疑似下线时，主节点 A 会更新自己保存的集群状态信息，将从 B 获得的下线报告保存起来。</p>
<h4>1.3 基于检测信息作下线判决</h4>
<p>如果在一个集群里，超过半数的主节点都将某个节点 X 报告为疑似下线 (PFAIL)，那么，节点 X 将被标记为下线（FAIL），并广播出去。所有收到这条 FAIL 消息的节点都会立即将节点 X 标记为 FAIL。至此，故障检测完成。</p>
<p>下线判决相关的源码位于 <code>cluster.c</code> 的函数 <code>void markNodeAsFailingIfNeeded(clusterNode *node)</code> 中，如下所示：</p>
<p><img src="assets/8ded1b10-a2ef-11e8-bd43-c7fbf0d980da" alt="enter image description here" /></p>
<p>通过源码可以清晰地看出，将一个节点标记为 FAIL 状态，需要满足两个条件：</p>
<ul>
<li>有超过半数的主节点将 Node 标记为 PFAIL 状态；</li>
<li>当前节点也将 Node 标记为 PFAIL 状态。</li>
</ul>
<p>所谓当前节点可以是集群中任意一个节点，由于 Redis-Cluster 是“无中心” 的，集群中任意正常节点都能执行函数 markNodeAsFailingIfNeeded，不过，由于 Gossip 协议的特点，总有先后顺序。如果确认 Node 已经进入了 FAIL 状态，那么当前节点还会向其它节点发送 FAIL 消息，让其它节点也将 Node 标记为 FAIL 。需要注意的是：</p>
<ul>
<li>集群判断一个 Node 进入 FAIL 所需的条件是弱（Weak）的， 因为其它节点对 Node 的状态报告并不是实时的，而是有一段时间间隔（这段时间内 Node 的状态可能已经发生了改变）；</li>
<li>尽管当前节点会向其它节点发送 FAIL 消息，但因为网络分区（Network Partition）的问题，有一部分节点可能无法感知 Node 标记为 FAIL；</li>
<li>只要我们成功将 Node 标记为 FAIL，那么这个 FAIL 状态最终（Eventually）总会传播至整个集群的所有节点。</li>
</ul>
<h4>1.4 节点故障检测优化</h4>
<p>通过上面的分析，很明显参数 <code>cluster_node_timeout</code> 对节点故障检测的优化至关重要。当集群规模较小时，为了加快节点故障检测和故障倒换的速度、保障可用性，可将 <code>cluster_node_timeout</code> 设置得小一点。</p>
<p>我曾经主导过一个项目，客户要求集群单节点故障条件下，恢复时间不得超过 10 s。考虑到 Redis-Cluster 只有6个节点，通信成本可以容忍，我将 <code>cluster_node_timeout</code> 设置为 3 s，经测试，集群单节点故障恢复时间缩短至 8 s，满足了客户需求。</p>
<h3>2. Redis-Cluster 选举原理及优化分析</h3>
<h4>2.1 从节点拉票</h4>
<p>基于故障检测信息的传播，集群中所有正常节点都将感知到某个主节点下线（Fail）的信息，当然也包括这个下线主节点的所有从节点。当从节点发现自己复制的主节点的状态为已下线时，从节点就会向集群广播一条请求消息，请求所有收到这条消息并且具有投票权的主节点给自己投票。</p>
<p><img src="assets/a97b9c40-a3a2-11e8-a938-3b329a942b7b" alt="enter image description here" /></p>
<h4>2.2 拉票优先级</h4>
<p>严格得讲，从节点在发现其主节点下线时，并不是立即发起故障转移流程而进行“拉票”的，而是要等待一段时间，在未来的某个时间点才发起选举，这个时间点的计算有两种方式。</p>
<h5><strong>方式一</strong></h5>
<p>如下代码所示，在故障主节点的所有从节点中，计算当前节点（当然也是故障主节点的从节点）的排名，排名按照复制偏移量计算，偏移量最大的从节点与主节点信息差异也最小，排名也就等于 0，其余从节点排名依次递增。通过排名计算发起选举的等待时间，根据源码，排名等于 0 的从节点无需等待即可发起拉票，其它排位的从节点则须等待，等待时间计算方法如下：</p>
<pre><code>(newRank - oldRank)*1000ms，

</code></pre>
<p>其中，newRank 和 oldRank 分别表示本次和上一次排名。</p>
<p>注意，如果当前系统时间小于需要等待的时刻，则返回，下一个周期再检查。</p>
<p>源码如下：</p>
<p><img src="assets/c67c3500-a39a-11e8-80dc-8d254ca863fe" alt="enter image description here" /></p>
<h5><strong>方式二</strong></h5>
<p>既然是拉票，就有可能因未能获得半数投票而失败，一轮选举失败后，需要等待一段时间（<code>auth_retry_time</code>）才能清理标志位，准备下一轮拉票。从节点拉票之前也需要等待，等待时间计算方法如下：</p>
<pre><code>mstime() + 500ms + random()%500ms + rank*1000ms

</code></pre>
<p>其中，500 ms 为固定延时，主要为了留出时间，使主节点下线的消息能传播到集群中其它节点，这样集群中的主节点才有可能投票；<code>random()%500ms</code> 表示随机延时，为了避免两个从节点同时开始故障转移流程；rank 表示从节点的排名，排名是指当前从节点在下线主节点的所有从节点中的排名，排名主要是根据复制数据量来定，复制数据量越多，排名越靠前，因此，具有较多复制数据量的从节点可以更早发起故障转移流程，从而更可能成为新的主节点。</p>
<p>源码如下：</p>
<p><img src="assets/df21fe20-a39d-11e8-a938-3b329a942b7b" alt="enter image description here" /></p>
<h5><strong>可优化点</strong></h5>
<p>上面提到的 <code>auth_retry_time</code> 是一个潜在的可优化点，也是一个必要的注意点，其计算方法如下源码所示：</p>
<p><img src="assets/3e9611b0-a39f-11e8-8b4a-cf3651600922" alt="enter image description here" /></p>
<p>从中可以看出，<code>auth_retry_time</code> 的取值为 <code>4*cluster_node_timeout (cluster_node_timeout&gt;1s)</code>。如果一轮选举没有成功，再次发起投票需要等待 <code>4*cluster_node_timeout</code>，按照 <code>cluster_node_timeout</code> 默认值为 15 s 计算，再次发起投票需要等待至少一分钟，如果故障的主节点只有一个从节点，则难以保证高可用。</p>
<p>在实际应用中，每个主节点通常设置 1-2 个从节点，为了避免首轮选举失败后的长时间等待，可根据需要修改源码，将 <code>auth_retry_time</code> 的值适当减小，如 10 s 左右。</p>
<h4>2.3 主节点投票</h4>
<p>如果一个主节点具有投票权（负责处理 Slot 的主节点)，并且这个主节点尚未投票给其它从节点，那么这个主节点将向请求投票的从节点返回一条回应消息，表示支持该从节点升主。</p>
<h4>2.4 根据投票结果决策</h4>
<p>在一个具有 N 个主节点投票的集群中，理论上每个参与拉票的从节点都可以收到一定数量的主节点投票，但是，在同一轮选举中，只可能有一个从节点收到的票数大于 <code>N/2 + 1</code>，也只有这个从节点可以升级为主节点，并代替已下线的主节点继续工作。</p>
<h4>2.5 选举失败</h4>
<p>跟生活中的选举一样，选举可能失败——没有一个候选从节点获得超过半数的主节点投票。遇到这种情况，集群将会进入下一轮选举，直到选出新的主节点为止。</p>
<h4>2.6 选举算法</h4>
<p>选举新主节点的算法是基于 Raft 算法的 Leader Election 方法来实现的，关于 Raft 算法，在第07课中将有详细介绍，此处了解即可。</p>
<h3>3. Redis-Cluster 的 Failover 原理</h3>
<p>所有发起投票的从节点中，只有获得超过半数主节点投票的从节点有资格升级为主节点，并接管故障主节点所负责的 Slots，源码如下：</p>
<p><img src="assets/b720d8a0-a3a3-11e8-8b4a-cf3651600922" alt="enter image description here" /></p>
<p>主要包括以下几个过程。</p>
<p>（1）身份切换</p>
<p>通过选举晋升的从节点会执行一系列的操作，清除曾经为从的信息，改头换面，成为新的主节点。</p>
<p>（2）接管职权</p>
<p>新的主节点会通过轮询所有 Slot，撤销所有对已下线主节点的 Slot 指派，消除影响，并且将这些 Slot 全部指派给自己。</p>
<p>（3）广而告之</p>
<p>升主了，必须让圈子里都知道，新的主节点会向集群中广播一条 PONG 消息，将自己升主的信息通知到集群中所有节点。</p>
<p>（4）履行义务</p>
<p>在其位谋其政，新的主节点开始处理自己所负责 Slot 对应的请求，至此，故障转移完成。</p>
<p>上述过程由 <code>cluster.c</code> 中的函数 <code>void clusterFailoverReplaceYourMaster(void)</code> 完成，源码如下所示：</p>
<p><img src="assets/62702c50-a3a5-11e8-a938-3b329a942b7b" alt="enter image description here" /></p>
<h3>4. 客户端的优化思路</h3>
<p>Redis-Cluster 发生故障后，集群的拓扑结构一定会发生改变，如下图所示：</p>
<p><img src="assets/7a5b8850-9671-11e8-9c35-b59aad3fef8b" alt="enter image description here" /></p>
<p>一个 3 主 3 从的集群，其中一台服务器因故障而宕机，从而导致该服务器上部署的两个 Redis 实例（一个 Master，一个 Slava）下线，集群的拓扑结构变成了 3 主 1 备。</p>
<h4>4.1 客户端如何感知 Redis-Cluster 发生故障？</h4>
<p>结合上面介绍的故障场景，<strong>思考这样一个问题</strong>：当 Redis-Cluster 发生故障，集群拓扑结构变化时，如果客户端没有及时感知到，继续试图对已经故障的节点进行“读写操作”，势必会出现异常，那么，如何应对这种场景呢？</p>
<p>Redis 的高级客户端很多，覆盖数十种编程语言，如常见的 Java 客户端 Jedis、Lettuce、Redisson。不同客户端针对上述问题的处理方式也不尽相同，一般有以下几种处理策略：</p>
<ul>
<li><strong>主动型</strong></li>
</ul>
<p>客户端发起一个定时任务，与 Redis-Cluster 保持 “心跳”，定时检测 Redis-Cluster 的拓扑结构和运行状态，一旦集群拓扑结构发生改变，迅速刷新客户端缓存的集群信息，从而使客户端保持对服务端（Redis-Cluster）认知的实时性。</p>
<ul>
<li><strong>被动型：</strong></li>
</ul>
<p>这是一种比较 “懒惰” 的策略，客户端不主动监测服务端的状态。当 Redis-Cluster 发生故障，集群拓扑结构变化后，客户端仍然按照之前缓存的集群信息进行 “读写操作” ，就必然出现异常，客户端捕获该异常，然后读取集群的状态信息并刷新自己缓存的集群信息。</p>
<p>需要说明的是，通常进行 “读写操作” 都有重试机制，不会因一次失败就判断为集群问题，而去刷新缓存的集群信息，因此，客户端这种被动的刷新策略往往会消耗较多的时间，时效性相较于主动监测要差。</p>
<ul>
<li><strong>基本型：</strong></li>
</ul>
<p>针对 Redis-Cluster 故障，很多开源客户端根本就没有应对措施，只是简单地将异常抛出，需要开发者自己去实现相应的处理策略。</p>
<blockquote>
<p>补充：对于 Redis-Cluster 故障的场景，有些开源客户端的应对措施更为复杂：集群故障后，拓扑结构变化，客户端不仅无法主动感知，甚至客户端与服务端（Redis-Cluster）之间的连接也会变得不可用，而这种 “不可用” 背后往往伴随着超时策略和重试机制，经过它们的判别后，才会最终抛出异常。用户捕获该异常后，需要重建连接，而后关闭旧连接并释放旧连接占用的资源。</p>
</blockquote>
<p>上面的描述中，超时策略和重试机制是最为耗时的一环，同时，这也是优化空间最大的一环。</p>
<h4>4.2 Redis-Cluster 故障后，客户端耗时优化举例</h4>
<p>基于 4.1 节的分析，相信读者已经可以构想出优化思路。在此，我将以 Redis 的高级 Java 客户端 Lettuce 为例，简单介绍一下客户端的耗时优化。</p>
<p>2017 年，国内某电商巨头的仓储系统出现故障（一台服务器宕机），管理页面登录超时（超过一分钟才登录完成），经过评估，判定为系统性能缺陷，需要优化。通过分解登录耗时，发现缓存访问耗时长达 28 秒，进一步排查确认宕机的服务器上部署有两个 Redis 节点，结合日志分析，发现 Redis-Cluster 故障后（两个 Redis 节点下线），客户端感知故障耗 20 秒，为症结所在。</p>
<p>为了优化耗时，我当时阅读了开源客户端 Lettuce 的源码,原来 Lettuce 的连接超时机制采用的超时时间为 10s，部分源码如下：</p>
<p><img src="assets/f909d460-d2d8-11e8-93cf-c998d6347dcb" alt="enter image description here" /></p>
<p>当 Redis-Cluster 故障后，客户端（Lettuce）感知到连接不可用后会分别与故障的 Redis 节点进行重试，而重试的超时时间为 10s，两个节点耗时 <code>10*2 s = 20 s</code>。</p>
<p>至此，优化就显得很简单了，比如，思路 1 缩短超时参数 <code>DEFAULT_CONNECT_TIMEOUT</code>，思路 2 中 客户端感知到连接不可用之后不进行重试，直接重建新连接，关闭旧连接。</p>
<h3>5. 后记</h3>
<p>本课的内容较为基础，重点在于向读者介绍一种 “优化” 思路，当遇到问题时，不要手足无措，而是分别从服务端、客户端以及它们之间的连接入手，分析其运作机制，寻找可优化点。此外，不要迷信开源软件，在真相大白前，所有代码都是“嫌疑人”。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="06&#32;Redis&#32;实际应用中的异常场景及其根因分析和解决方案.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="08&#32;基于&#32;Redis&#32;的分布式锁实现及其踩坑案例.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b4350086f32645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
            document.getElementById("tip").innerHTML = "<a href='https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/%E5%88%86%E5%B8%83%E5%BC%8F%E4%B8%AD%E9%97%B4%E4%BB%B6%E5%AE%9E%E8%B7%B5%E4%B9%8B%E8%B7%AF%EF%BC%88%E5%AE%8C%EF%BC%89/&quot;&#32;+&#32;cookie&#32;+&#32;&quot;'>跳转到上次进度</a>"
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
