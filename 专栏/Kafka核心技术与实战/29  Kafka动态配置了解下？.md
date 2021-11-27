<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>29  Kafka动态配置了解下？.md</title>
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

                    <a class="current-tab" href="29&#32;&#32;Kafka动态配置了解下？.md">29  Kafka动态配置了解下？.md</a>
                    

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

                    
                    <a href="38&#32;&#32;调优Kafka，你做到了吗？.md">38  调优Kafka，你做到了吗？.md</a>

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
                        <div><h1>29  Kafka动态配置了解下？</h1>
<p>你好，我是胡夕。今天我要和你讨论的主题是：Kafka 的动态 Broker 参数配置。</p>
<h2>什么是动态 Broker 参数配置？</h2>
<p>在开始今天的分享之前，我们先来复习一下设置 Kafka 参数，特别是 Broker 端参数的方法。</p>
<p>在 Kafka 安装目录的 config 路径下，有个 server.properties 文件。通常情况下，我们会指定这个文件的路径来启动 Broker。如果要设置 Broker 端的任何参数，我们必须在这个文件中显式地增加一行对应的配置，之后启动 Broker 进程，令参数生效。我们常见的做法是，一次性设置好所有参数之后，再启动 Broker。当后面需要变更任何参数时，我们必须重启 Broker。但生产环境中的服务器，怎么能随意重启呢？所以，目前修改 Broker 端参数是非常痛苦的过程。</p>
<p>基于这个痛点，社区于 1.1.0 版本中正式引入了动态 Broker 参数（Dynamic Broker Configs）。所谓动态，就是指修改参数值后，无需重启 Broker 就能立即生效，而之前在 server.properties 中配置的参数则称为静态参数（Static Configs）。显然，动态调整参数值而无需重启服务，是非常实用的功能。如果你想体验动态 Broker 参数的话，那就赶快升级到 1.1 版本吧。</p>
<p>当然了，当前最新的 2.3 版本中的 Broker 端参数有 200 多个，社区并没有将每个参数都升级成动态参数，它仅仅是把一部分参数变成了可动态调整。那么，我们应该如何分辨哪些参数是动态参数呢？</p>
<p>如果你打开 1.1 版本之后（含 1.1）的 Kafka 官网，你会发现<a href="https://kafka.apache.org/documentation/#brokerconfigs">Broker Configs</a>表中增加了 Dynamic Update Mode 列。该列有 3 类值，分别是 read-only、per-broker 和 cluster-wide。我来解释一下它们的含义。</p>
<ul>
<li>read-only。被标记为 read-only 的参数和原来的参数行为一样，只有重启 Broker，才能令修改生效。</li>
<li>per-broker。被标记为 per-broker 的参数属于动态参数，修改它之后，只会在对应的 Broker 上生效。</li>
<li>cluster-wide。被标记为 cluster-wide 的参数也属于动态参数，修改它之后，会在整个集群范围内生效，也就是说，对所有 Broker 都生效。你也可以为具体的 Broker 修改 cluster-wide 参数。</li>
</ul>
<p>我来举个例子说明一下 per-broker 和 cluster-wide 的区别。Broker 端参数 listeners 想必你应该不陌生吧。它是一个 per-broker 参数，这表示你只能为单个 Broker 动态调整 listeners，而不能直接调整一批 Broker 的 listeners。log.retention.ms 参数是 cluster-wide 级别的，Kafka 允许为集群内所有 Broker 统一设置一个日志留存时间值。当然了，你也可以为单个 Broker 修改此值。</p>
<h2>使用场景</h2>
<p>你可能会问，动态 Broker 参数的使用场景都有哪些呢？实际上，因为不必重启 Broker，动态 Broker 参数的使用场景非常广泛，通常包括但不限于以下几种：</p>
<ul>
<li>动态调整 Broker 端各种线程池大小，实时应对突发流量。</li>
<li>动态调整 Broker 端连接信息或安全配置信息。</li>
<li>动态更新 SSL Keystore 有效期。</li>
<li>动态调整 Broker 端 Compact 操作性能。</li>
<li>实时变更 JMX 指标收集器 (JMX Metrics Reporter)。</li>
</ul>
<p>在这些使用场景中，动态调整线程池大小应该算是最实用的功能了。很多时候，当 Kafka Broker 入站流量（inbound data）激增时，会造成 Broker 端请求积压（Backlog）。有了动态参数，我们就能够动态增加网络线程数和 I/O 线程数，快速消耗一些积压。当突发流量过去后，我们也能将线程数调整回来，减少对资源的浪费。整个过程都不需要重启 Broker。你甚至可以将这套调整线程数的动作，封装进定时任务中，以实现自动扩缩容。</p>
<h2>如何保存？</h2>
<p>由于动态配置的特殊性，它必然有和普通只读参数不同的保存机制。下面我来介绍一下 Kafka 是如何保存动态配置的。</p>
<p>首先，Kafka 将动态 Broker 参数保存在 ZooKeeper 中，具体的 znode 路径如下图所示。</p>
<p><img src="assets/67125a22a27028e18bab9f03a6664859.png" alt="img" /></p>
<p>我来解释一下图中的内容。changes 是用来实时监测动态参数变更的，不会保存参数值；topics 是用来保存 Kafka 主题级别参数的。虽然它们不属于动态 Broker 端参数，但其实它们也是能够动态变更的。</p>
<p>users 和 clients 则是用于动态调整客户端配额（Quota）的 znode 节点。所谓配额，是指 Kafka 运维人员限制连入集群的客户端的吞吐量或者是限定它们使用的 CPU 资源。</p>
<p>分析到这里，我们就会发现，/config/brokers znode 才是真正保存动态 Broker 参数的地方。该 znode 下有两大类子节点。第一类子节点就只有一个，它有个固定的名字叫 &lt; default &gt;，保存的是前面说过的 cluster-wide 范围的动态参数；另一类则以 broker.id 为名，保存的是特定 Broker 的 per-broker 范围参数。由于是 per-broker 范围，因此这类子节点可能存在多个。</p>
<p>我们一起来看一张图片，它展示的是我的一个 Kafka 集群环境上的动态 Broker 端参数。</p>
<p><img src="assets/c4154989775023afb619f2fdb07f6f7c.png" alt="img" /></p>
<p>在这张图中，我首先查看了 /config/brokers 下的子节点，我们可以看到，这里面有 &lt; default &gt; 节点和名为 0、1 的子节点。&lt; default &gt; 节点中保存了我设置的 cluster-wide 范围参数；0 和 1 节点中分别保存了我为 Broker 0 和 Broker 1 设置的 per-broker 参数。</p>
<p>接下来，我分别展示了 cluster-wide 范围和 per-broker 范围的参数设置。拿 num.io.threads 参数为例，其 cluster-wide 值被动态调整为 12，而在 Broker 0 上被设置成 16，在 Broker 1 上被设置成 8。我为 Broker 0 和 Broker 1 单独设置的值，会覆盖掉 cluster-wide 值，但在其他 Broker 上，该参数默认值还是按 12 计算。</p>
<p>如果我们再把静态参数加进来一起讨论的话，cluster-wide、per-broker 和 static 参数的优先级是这样的：per-broker 参数 &gt; cluster-wide 参数 &gt; static 参数 &gt; Kafka 默认值。</p>
<p>另外，如果你仔细查看上图中的<strong>ephemeralOwner 字段</strong>，你会发现它们的值都是 0x0。这表示这些 znode 都是持久化节点，它们将一直存在。即使 ZooKeeper 集群重启，这些数据也不会丢失，这样就能保证这些动态参数的值会一直生效。</p>
<h2>如何配置？</h2>
<p>讲完了保存原理，我们来说说如何配置动态 Broker 参数。目前，设置动态参数的工具行命令只有一个，那就是 Kafka 自带的 kafka-configs 脚本。接下来，我来以 unclean.leader.election.enable 参数为例，演示一下如何动态调整。</p>
<p>下面这条命令展示了如何在集群层面设置全局值，即设置 cluster-wide 范围值。</p>
<pre><code>$ bin/kafka-configs.sh --bootstrap-server kafka-host:port --entity-type brokers --entity-default --alter --add-config unclean.leader.election.enable=true
Completed updating default config for brokers in the cluster,
</code></pre>
<p>总体来说命令很简单，但有一点需要注意。<strong>如果要设置 cluster-wide 范围的动态参数，需要显式指定 entity-default</strong>。现在，我们使用下面的命令来查看一下刚才的配置是否成功。</p>
<pre><code>$ bin/kafka-configs.sh --bootstrap-server kafka-host:port --entity-type brokers --entity-default --describe
Default config for brokers in the cluster are:
  unclean.leader.election.enable=true sensitive=false synonyms={DYNAMIC_DEFAULT_BROKER_CONFIG:unclean.leader.election.enable=true}
</code></pre>
<p>从输出来看，我们成功地在全局层面上设置该参数值为 true。注意 sensitive=false 的字眼，它表明我们要调整的参数不是敏感数据。如果我们调整的是类似于密码这样的参数时，该字段就会为 true，表示这属于敏感数据。</p>
<p>好了，调整完 cluster-wide 范围的参数，我来演示下如何设置 per-broker 范围参数。我们还是以 unclean.leader.election.enable 参数为例，我现在为 ID 为 1 的 Broker 设置一个不同的值。命令如下：</p>
<pre><code>$ bin/kafka-configs.sh --bootstrap-server kafka-host:port --entity-type brokers --entity-name 1 --alter --add-config unclean.leader.election.enable=false
Completed updating config for broker: 1.
</code></pre>
<p>同样，我们使用下列命令，来查看一下刚刚的设置是否生效了。</p>
<pre><code>$ bin/kafka-configs.sh --bootstrap-server kafka-host:port --entity-type brokers --entity-name 1 --describe
Configs for broker 1 are:
  unclean.leader.election.enable=false sensitive=false synonyms={DYNAMIC_BROKER_CONFIG:unclean.leader.election.enable=false, DYNAMIC_DEFAULT_BROKER_CONFIG:unclean.leader.election.enable=true, DEFAULT_CONFIG:unclean.leader.election.enable=false}
</code></pre>
<p>这条命令的输出信息很多。我们关注两点即可。</p>
<ol>
<li>在 Broker 1 层面上，该参数被设置成了 false，这表明命令运行成功了。</li>
<li>从倒数第二行可以看出，在全局层面上，该参数值依然是 true。这表明，我们之前设置的 cluster-wide 范围参数值依然有效。</li>
</ol>
<p>如果我们要删除 cluster-wide 范围参数或 per-broker 范围参数，也非常简单，分别执行下面的命令就可以了。</p>
<pre><code># 删除 cluster-wide 范围参数
$ bin/kafka-configs.sh --bootstrap-server kafka-host:port --entity-type brokers --entity-default --alter --delete-config unclean.leader.election.enable
Completed updating default config for brokers in the cluster,
# 删除 per-broker 范围参数
$ bin/kafka-configs.sh --bootstrap-server kafka-host:port --entity-type brokers --entity-name 1 --alter --delete-config unclean.leader.election.enable
Completed updating config for broker: 1.
</code></pre>
<p><strong>删除动态参数要指定 delete-config</strong>。当我们删除完动态参数配置后，再次运行查看命令，结果如下：</p>
<pre><code># 查看 cluster-wide 范围参数
$ bin/kafka-configs.sh --bootstrap-server kafka-host:port  --entity-type brokers --entity-default --describe
Default config for brokers in the cluster are:
# 查看 Broker 1 上的动态参数配置
$ bin/kafka-configs.sh --bootstrap-server kafka-host:port  --entity-type brokers --entity-name 1 --describe
Configs for broker 1 are:
</code></pre>
<p>此时，刚才配置的所有动态参数都已经被成功移除了。</p>
<p>刚刚我只是举了一个参数的例子，如果你想要知道动态 Broker 参数都有哪些，一种方式是在 Kafka 官网中查看 Broker 端参数列表，另一种方式是直接运行无参数的 kafka-configs 脚本，该脚本的说明文档会告诉你当前动态 Broker 参数都有哪些。我们可以先来看看下面这两张图。</p>
<p><img src="assets/400532989c3214f00a2f764fe7983cf1.png" alt="img" /></p>
<p><img src="assets/eb99853bca3d91ad3a53db5dbe3e3b67.png" alt="img" /></p>
<p>看到有这么多动态 Broker 参数，你可能会问：这些我都需要调整吗？你能告诉我最常用的几个吗？根据我的实际使用经验，我来跟你分享一些有较大几率被动态调整值的参数。</p>
<p><strong>1.log.retention.ms。</strong></p>
<p>修改日志留存时间应该算是一个比较高频的操作，毕竟，我们不可能完美地预估所有业务的消息留存时长。虽然该参数有对应的主题级别参数可以设置，但拥有在全局层面上动态变更的能力，依然是一个很好的功能亮点。</p>
<p><strong>2.num.io.threads 和 num.network.threads。</strong></p>
<p>这是我们在前面提到的两组线程池。就我个人而言，我觉得这是动态 Broker 参数最实用的场景了。毕竟，在实际生产环境中，Broker 端请求处理能力经常要按需扩容。如果没有动态 Broker 参数，我们是无法做到这一点的。</p>
<p><strong>3. 与 SSL 相关的参数。</strong></p>
<p>主要是 4 个参数（ssl.keystore.type、ssl.keystore.location、ssl.keystore.password 和 ssl.key.password）。允许动态实时调整它们之后，我们就能创建那些过期时间很短的 SSL 证书。每当我们调整时，Kafka 底层会重新配置 Socket 连接通道并更新 Keystore。新的连接会使用新的 Keystore，阶段性地调整这组参数，有利于增加安全性。</p>
<p><strong>4.num.replica.fetchers。</strong></p>
<p>这也是我认为的最实用的动态 Broker 参数之一。Follower 副本拉取速度慢，在线上 Kafka 环境中一直是一个老大难的问题。针对这个问题，常见的做法是增加该参数值，确保有充足的线程可以执行 Follower 副本向 Leader 副本的拉取。现在有了动态参数，你不需要再重启 Broker，就能立即在 Follower 端生效，因此我说这是很实用的应用场景。</p>
<h2>小结</h2>
<p>好了，我们来小结一下。今天，我们重点讨论了 Kafka 1.1.0 版本引入的动态 Broker 参数。这类参数最大的好处在于，无需重启 Broker，就可以令变更生效，因此能够极大地降低运维成本。除此之外，我还给出了动态参数的保存机制和设置方法。在专栏的后面，我还会给出动态参数设置的另一种方法，敬请期待。</p>
<p><img src="assets/c7e3eff159216101b78911221fae4afc.png" alt="img" /></p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="28&#32;&#32;主题管理知多少.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="30&#32;&#32;怎么重设消费者组位移？.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b4345654d5470ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
