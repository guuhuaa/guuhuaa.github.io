<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>35  跨集群备份解决方案MirrorMaker.md</title>
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

                    <a class="current-tab" href="35&#32;&#32;跨集群备份解决方案MirrorMaker.md">35  跨集群备份解决方案MirrorMaker.md</a>
                    

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
                        <div><h1>35  跨集群备份解决方案MirrorMaker</h1>
<p>你好，我是胡夕。今天我要和你分享的主题是：Kafka 的跨集群数据镜像工具 MirrorMaker。</p>
<p>一般情况下，我们会使用一套 Kafka 集群来完成业务，但有些场景确实会需要多套 Kafka 集群同时工作，比如为了便于实现灾难恢复，你可以在两个机房分别部署单独的 Kafka 集群。如果其中一个机房出现故障，你就能很容易地把流量打到另一个正常运转的机房下。再比如，你想为地理相近的客户提供低延时的消息服务，而你的主机房又离客户很远，这时你就可以在靠近客户的地方部署一套 Kafka 集群，让这套集群服务你的客户，从而提供低延时的服务。</p>
<p>如果要实现这些需求，除了部署多套 Kafka 集群之外，你还需要某种工具或框架，来帮助你实现数据在集群间的拷贝或镜像。</p>
<p>值得注意的是，<strong>通常我们把数据在单个集群下不同节点之间的拷贝称为备份，而把数据在集群间的拷贝称为镜像</strong>（Mirroring）。</p>
<p>今天，我来重点介绍一下 Apache Kafka 社区提供的 MirrorMaker 工具，它可以帮我们实现消息或数据从一个集群到另一个集群的拷贝。</p>
<h2>什么是 MirrorMaker？</h2>
<p>从本质上说，MirrorMaker 就是一个消费者 + 生产者的程序。消费者负责从源集群（Source Cluster）消费数据，生产者负责向目标集群（Target Cluster）发送消息。整个镜像流程如下图所示：</p>
<p><img src="assets/fe4e9c756bf30933ec3dba10bad30e8c.png" alt="img" /></p>
<p>MirrorMaker 连接的源集群和目标集群，会实时同步消息。当然，你不要认为你只能使用一套 MirrorMaker 来连接上下游集群。事实上，很多用户会部署多套集群，用于实现不同的目的。</p>
<p>我们来看看下面这张图。图中部署了三套集群：左边的源集群负责主要的业务处理；右上角的目标集群可以用于执行数据分析；而右下角的目标集群则充当源集群的热备份。</p>
<p><img src="assets/63fb620532337fcfdfd1ca2df351a378.png" alt="img" /></p>
<h2>运行 MirrorMaker</h2>
<p>Kafka 默认提供了 MirrorMaker 命令行工具 kafka-mirror-maker 脚本，它的常见用法是指定生产者配置文件、消费者配置文件、线程数以及要执行数据镜像的主题正则表达式。比如下面的这个命令，就是一个典型的 MirrorMaker 执行命令。</p>
<pre><code>$ bin/kafka-mirror-maker.sh --consumer.config ./config/consumer.properties --producer.config ./config/producer.properties --num.streams 8 --whitelist &quot;.*&quot;
</code></pre>
<p>现在我来解释一下这条命令中各个参数的含义。</p>
<ul>
<li>consumer.config 参数。它指定了 MirrorMaker 中消费者的配置文件地址，最主要的配置项是<strong>bootstrap.servers</strong>，也就是该 MirrorMaker 从哪个 Kafka 集群读取消息。因为 MirrorMaker 有可能在内部创建多个消费者实例并使用消费者组机制，因此你还需要设置 group.id 参数。另外，我建议你额外配置 auto.offset.reset=earliest，否则的话，MirrorMaker 只会拷贝那些在它启动之后到达源集群的消息。</li>
<li>producer.config 参数。它指定了 MirrorMaker 内部生产者组件的配置文件地址。通常来说，Kafka Java Producer 很友好，你不需要配置太多参数。唯一的例外依然是<strong>bootstrap.servers</strong>，你必须显式地指定这个参数，配置拷贝的消息要发送到的目标集群。</li>
<li>num.streams 参数。我个人觉得，这个参数的名字很容易给人造成误解。第一次看到这个参数名的时候，我一度以为 MirrorMaker 是用 Kafka Streams 组件实现的呢。其实并不是。这个参数就是告诉 MirrorMaker 要创建多少个 KafkaConsumer 实例。当然，它使用的是多线程的方案，即在后台创建并启动多个线程，每个线程维护专属的消费者实例。在实际使用时，你可以根据你的机器性能酌情设置多个线程。</li>
<li>whitelist 参数。如命令所示，这个参数接收一个正则表达式。所有匹配该正则表达式的主题都会被自动地执行镜像。在这个命令中，我指定了“.*”，这表明我要同步源集群上的所有主题。</li>
</ul>
<h2>MirrorMaker 配置实例</h2>
<p>现在，我就在测试环境中为你演示一下 MirrorMaker 的使用方法。</p>
<p>演示的流程大致是这样的：首先，我们会启动两套 Kafka 集群，它们是单节点的伪集群，监听端口分别是 9092 和 9093；之后，我们会启动 MirrorMaker 工具，实时地将 9092 集群上的消息同步镜像到 9093 集群上；最后，我们启动额外的消费者来验证消息是否拷贝成功。</p>
<h3>第 1 步：启动两套 Kafka 集群</h3>
<p>启动日志如下所示：</p>
<blockquote>
<p>[2019-07-23 17:01:40,544] INFO Kafka version: 2.3.0 (org.apache.kafka.common.utils.AppInfoParser)
[2019-07-23 17:01:40,544] INFO Kafka commitId: fc1aaa116b661c8a (org.apache.kafka.common.utils.AppInfoParser)
[2019-07-23 17:01:40,544] INFO Kafka startTimeMs: 1563872500540 (org.apache.kafka.common.utils.AppInfoParser)
[2019-07-23 17:01:40,545] INFO [KafkaServer id=0] started (kafka.server.KafkaServer)</p>
</blockquote>
<blockquote>
<p>[2019-07-23 16:59:59,462] INFO Kafka version: 2.3.0 (org.apache.kafka.common.utils.AppInfoParser)
[2019-07-23 16:59:59,462] INFO Kafka commitId: fc1aaa116b661c8a (org.apache.kafka.common.utils.AppInfoParser)
[2019-07-23 16:59:59,462] INFO Kafka startTimeMs: 1563872399459 (org.apache.kafka.common.utils.AppInfoParser)
[2019-07-23 16:59:59,463] INFO [KafkaServer id=1] started (kafka.server.KafkaServer)</p>
</blockquote>
<h3>第 2 步：启动 MirrorMaker 工具</h3>
<p>在启动 MirrorMaker 工具之前，我们必须准备好刚刚提过的 Consumer 配置文件和 Producer 配置文件。它们的内容分别如下：</p>
<pre><code>consumer.properties：
bootstrap.servers=localhost:9092
group.id=mirrormaker
auto.offset.reset=earliest
producer.properties:
bootstrap.servers=localhost:9093
</code></pre>
<p>现在，我们来运行命令启动 MirrorMaker 工具。</p>
<pre><code>$ bin/kafka-mirror-maker.sh --producer.config ../producer.config --consumer.config ../consumer.config --num.streams 4 --whitelist &quot;.*&quot;
WARNING: The default partition assignment strategy of the mirror maker will change from 'range' to 'roundrobin' in an upcoming release (so that better load balancing can be achieved). If you prefer to make this switch in advance of that release add the following to the corresponding config: 'partition.assignment.strategy=org.apache.kafka.clients.consumer.RoundRobinAssignor'
</code></pre>
<p>请你一定要仔细阅读这个命令输出中的警告信息。这个警告的意思是，在未来版本中，MirrorMaker 内部消费者会使用轮询策略（Round-robin）来为消费者实例分配分区，现阶段使用的默认策略依然是基于范围的分区策略（Range）。Range 策略的思想很朴素，它是将所有分区根据一定的顺序排列在一起，每个消费者依次顺序拿走各个分区。</p>
<p>Round-robin 策略的推出时间要比 Range 策略晚。通常情况下，我们可以认为，社区推出的比较晚的分区分配策略会比之前的策略好。这里的好指的是能实现更均匀的分配效果。该警告信息的最后一部分内容提示我们，<strong>如果我们想提前“享用”轮询策略，需要手动地在 consumer.properties 文件中增加 partition.assignment.strategy 的设置</strong>。</p>
<h3>第 3 步：验证消息是否拷贝成功</h3>
<p>好了，启动 MirrorMaker 之后，我们可以向源集群发送并消费一些消息，然后验证是否所有的主题都能正确地同步到目标集群上。</p>
<p>假设我们在源集群上创建了一个 4 分区的主题 test，随后使用 kafka-producer-perf-test 脚本模拟发送了 500 万条消息。现在，我们使用下面这两条命令来查询一下，目标 Kafka 集群上是否存在名为 test 的主题，并且成功地镜像了这些消息。</p>
<pre><code>$ bin/kafka-run-class.sh kafka.tools.GetOffsetShell --broker-list localhost:9093 --topic test --time -2
test:0:0
$ bin/kafka-run-class.sh kafka.tools.GetOffsetShell --broker-list localhost:9093 --topic test --time -1
test:0:5000000
</code></pre>
<p>-1 和 -2 分别表示获取某分区最新的位移和最早的位移，这两个位移值的差值就是这个分区当前的消息数，在这个例子中，差值是 500 万条。这说明主题 test 当前共写入了 500 万条消息。换句话说，MirrorMaker 已经成功地把这 500 万条消息同步到了目标集群上。</p>
<p>讲到这里，你一定会觉得很奇怪吧，我们明明在源集群创建了一个 4 分区的主题，为什么到了目标集群，就变成单分区了呢？</p>
<p>原因很简单。<strong>MirrorMaker 在执行消息镜像的过程中，如果发现要同步的主题在目标集群上不存在的话，它就会根据 Broker 端参数 num.partitions 和 default.replication.factor 的默认值，自动将主题创建出来</strong>。在这个例子中，我们在目标集群上没有创建过任何主题，因此，在镜像开始时，MirrorMaker 自动创建了一个名为 test 的单分区单副本的主题。</p>
<p><strong>在实际使用场景中，我推荐你提前把要同步的所有主题按照源集群上的规格在目标集群上等价地创建出来</strong>。否则，极有可能出现刚刚的这种情况，这会导致一些很严重的问题。比如原本在某个分区的消息同步到了目标集群以后，却位于其他的分区中。如果你的消息处理逻辑依赖于这样的分区映射，就必然会出现问题。</p>
<p>除了常规的 Kafka 主题之外，MirrorMaker 默认还会同步内部主题，比如在专栏前面我们频繁提到的位移主题。MirrorMaker 在镜像位移主题时，如果发现目标集群尚未创建该主题，它就会根据 Broker 端参数 offsets.topic.num.partitions 和 offsets.topic.replication.factor 的值来制定该主题的规格。默认配置是 50 个分区，每个分区 3 个副本。</p>
<p>在 0.11.0.0 版本之前，Kafka 不会严格依照 offsets.topic.replication.factor 参数的值。这也就是说，如果你设置了该参数值为 3，而当前存活的 Broker 数量少于 3，位移主题依然能被成功创建，只是副本数取该参数值和存活 Broker 数之间的较小值。</p>
<p>这个缺陷在 0.11.0.0 版本被修复了，这就意味着，Kafka 会严格遵守你设定的参数值，如果发现存活 Broker 数量小于参数值，就会直接抛出异常，告诉你主题创建失败。因此，在使用 MirrorMaker 时，你一定要确保这些配置都是合理的。</p>
<h2>其他跨集群镜像方案</h2>
<p>讲到这里，MirrorMaker 的主要功能我就介绍完了。你大致可以感觉到执行 MirrorMaker 的命令是很简单的，而且它提供的功能很有限。实际上，它的运维成本也比较高，比如主题的管理就非常不便捷，同时也很难将其管道化。</p>
<p>基于这些原因，业界很多公司选择自己开发跨集群镜像工具。我来简单介绍几个。</p>
<p>1.<strong>Uber 的 uReplicator 工具</strong></p>
<p>Uber 公司之前也是使用 MirrorMaker 的，但是在使用过程中，他们发现了一些明显的缺陷，比如 MirrorMaker 中的消费者使用的是消费者组的机制，这不可避免地会碰到很多 Rebalance 的问题。</p>
<p>为此，Uber 自己研发了 uReplicator。它使用 Apache Helix 作为集中式的主题分区管理组件，并且重写了消费者程序，来替换之前 MirrorMaker 下的消费者，使用 Helix 来管理分区的分配，从而避免了 Rebalance 的各种问题。</p>
<p>讲到这里，我个人有个小小的感慨：社区最近正在花大力气去优化消费者组机制，力求改善因 Rebalance 导致的各种场景，但其实，其他框架开发者反而是不用 Group 机制的。他们宁愿自己开发一套机制来维护分区分配的映射。这些都说明 Kafka 中的消费者组还是有很大的提升空间的。</p>
<p>另外，Uber 专门写了一篇<a href="https://eng.uber.com/ureplicator/">博客</a>，详细说明了 uReplicator 的设计原理，并罗列了社区的 MirrorMaker 工具的一些缺陷以及 uReplicator 的应对方法。我建议你一定要读一读这篇博客。</p>
<p>2.<strong>LinkedIn 开发的 Brooklin Mirror Maker 工具</strong></p>
<p>针对现有 MirrorMaker 工具不易实现管道化的缺陷，这个工具进行了有针对性的改进，同时也对性能做了一些优化。目前，在 LinkedIn 公司，Brooklin Mirror Maker 已经完全替代了社区版的 MirrorMaker。如果你想深入了解它是如何做到的，我给你推荐一篇<a href="https://www.slideshare.net/jyouping/brooklin-mirror-maker-how-and-why-we-moved-away-from-kafka-mirror-maker">博客</a>，你可以详细阅读一下。</p>
<p>3.<strong>Confluent 公司研发的 Replicator 工具</strong></p>
<p>这个工具提供的是企业级的跨集群镜像方案，是市面上已知的功能最为强大的工具，可以便捷地为你提供 Kafka 主题在不同集群间的迁移。除此之外，Replicator 工具还能自动在目标集群上创建与源集群上配置一模一样的主题，极大地方便了运维管理。不过凡事有利就有弊，Replicator 是要收费的。如果你所在的公司预算充足，而且你们关心数据在多个集群甚至是多个数据中心间的迁移质量，不妨关注一下 Confluent 公司的<a href="https://www.confluent.io/confluent-replicator/">Replicator 工具</a>。</p>
<h2>小结</h2>
<p>好了，我们总结一下今天所讲的 MirrorMaker。它是 Apache Kafka 社区提供的跨集群镜像解决方案，主要实现将 Kafka 消息实时从一个集群同步复制或镜像到另一个集群。你可以把 MirrorMaker 应用到很多实际的场景中，比如数据备份、主备集群等。MirrorMaker 本身功能简单，应用灵活，但也有运维成本高、性能差等劣势，因此业界有厂商研发了自己的镜像工具。你可以根据自身的业务需求，选择合适的工具来帮助你完成跨集群的数据备份。</p>
<p><img src="assets/c0b75891bf37c1086dea98358c481d5e.jpg" alt="img" /></p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="34&#32;&#32;云环境下的授权该怎么做？.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="36&#32;&#32;你应该怎么监控Kafka？.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b43458e594c70ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
