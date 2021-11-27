<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>41  Kafka Streams DSL开发实例.md</title>
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

                    
                    <a href="38&#32;&#32;调优Kafka，你做到了吗？.md">38  调优Kafka，你做到了吗？.md</a>

                </li>
                <li>

                    
                    <a href="39&#32;&#32;从0搭建基于Kafka的企业级实时日志流处理平台.md">39  从0搭建基于Kafka的企业级实时日志流处理平台.md</a>

                </li>
                <li>

                    
                    <a href="40&#32;&#32;Kafka&#32;Streams与其他流处理平台的差异在哪里？.md">40  Kafka Streams与其他流处理平台的差异在哪里？.md</a>

                </li>
                <li>

                    <a class="current-tab" href="41&#32;&#32;Kafka&#32;Streams&#32;DSL开发实例.md">41  Kafka Streams DSL开发实例.md</a>
                    

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
                        <div><h1>41  Kafka Streams DSL开发实例</h1>
<p>你好，我是胡夕。今天我要和你分享的主题是：Kafka Streams DSL 开发实例。</p>
<p>DSL，也就是 Domain Specific Language，意思是领域特定语言。它提供了一组便捷的 API 帮助我们实现流式数据处理逻辑。今天，我就来分享一些 Kafka Streams 中的 DSL 开发方法以及具体实例。</p>
<h2>Kafka Streams 背景介绍</h2>
<p>在上一讲中，我们提到流处理平台是专门处理无限数据集的引擎。就 Kafka Streams 而言，它仅仅是一个客户端库。所谓的 Kafka Streams 应用，就是调用了 Streams API 的普通 Java 应用程序。只不过在 Kafka Streams 中，流处理逻辑是用<strong>拓扑</strong>来表征的。</p>
<p>一个拓扑结构本质上是一个有向无环图（DAG），它由多个处理节点（Node）和连接节点的多条边组成，如下图所示：</p>
<p><img src="assets/6187942d6827b95cef3937898ae6a53f.png" alt="img" /></p>
<p>图中的节点也称为处理单元或 Processor，它封装了具体的事件处理逻辑。Processor 在其他流处理平台也被称为操作算子。常见的操作算子包括转换（map）、过滤（filter）、连接（join）和聚合（aggregation）等。后面我会详细介绍几种常见的操作算子。</p>
<p>大体上，Kafka Streams 开放了两大类 API 供你定义 Processor 逻辑。</p>
<p>第 1 类就是我刚刚提到的 DSL，它是声明式的函数式 API，使用起来感觉和 SQL 类似，你不用操心它的底层是怎么实现的，你只需要调用特定的 API 告诉 Kafka Streams 你要做什么即可。</p>
<p>举个简单的例子，你可以看看下面这段代码，尝试理解下它是做什么的。</p>
<pre><code>movies.filter((title, movie) -&gt; movie.getGenre().equals(&quot; 动作片 &quot;)).xxx()...
</code></pre>
<p>这段代码虽然用了 Java 8 的 Lambda 表达式，但从整体上来看，它要做的事情应该还是很清晰的：它要从所有 Movie 事件中过滤出影片类型是“动作片”的事件。这就是 DSL 声明式 API 的实现方式。</p>
<p>第 2 类则是命令式的低阶 API，称为 Processor API。比起 DSL，这组 API 提供的实现方式更加灵活。你可以编写自定义的算子来实现一些 DSL 天然没有提供的处理逻辑。事实上，DSL 底层也是用 Processor API 实现的。</p>
<p>目前，Kafka Streams DSL 提供的 API 已经很丰富了，基本上能够满足我们大部分的处理逻辑需求，我今天重点介绍一下 DSL 的使用方法。</p>
<p><strong>不论是用哪组 API 实现，所有流处理应用本质上都可以分为两类：有状态的（Stateful）应用和无状态的（Stateless）应用</strong>。</p>
<p>有状态的应用指的是应用中使用了类似于连接、聚合或时间窗口（Window）的 API。一旦调用了这些 API，你的应用就变为有状态的了，也就是说你需要让 Kafka Streams 帮你保存应用的状态。</p>
<p>无状态的应用是指在这类应用中，某条消息的处理结果不会影响或依赖其他消息的处理。常见的无状态操作包括事件转换以及刚刚那个例子中的过滤等。</p>
<h2>关键概念</h2>
<p>了解了这些背景之后，你还需要掌握一些流处理领域内的关键概念，即流、表以及流表二元性，还有时间和时间窗口。</p>
<h3>流表二元性</h3>
<p>首先，我来介绍一下流处理中流和表的概念，以及它们之间的关系。</p>
<p>流就是一个永不停止（至少理论上是这样的）的事件序列，而表和关系型数据库中的概念类似，是一组行记录。在流处理领域，两者是有机统一的：<strong>流在时间维度上聚合之后形成表，表在时间维度上不断更新形成流，这就是所谓的流表二元性（Duality of Streams and Tables）</strong>。流表二元性在流处理领域内的应用是 Kafka 框架赖以成功的重要原因之一。</p>
<p>下面这张图展示了表转换成流，流再转换成表的全过程。</p>
<p><img src="assets/a7334e4100533de65286f12ca72f1544.png" alt="img" /></p>
<p>刚开始时，表中只有一条记录“张三：1”。将该条记录转成流，变成了一条事件。接着，表增加了新记录“李四：1”。针对这个变更，流中也增加了对应的新事件。之后，表中张三的对应值，从 1 更新为 2，流也增加了相应的更新事件。最后，表中添加了新数据“王五：1”，流也增加了新记录。至此，表转换成流的工作就完成了。</p>
<p>从这个过程中我们可以看出，流可以看作是表的变更事件日志（Changelog）。与之相反的是，流转换成表的过程，可以说是这个过程的逆过程：我们为流中的每条事件打一个快照（Snapshot），就形成了表。</p>
<p>流和表的概念在流处理领域非常关键。在 Kafka Streams DSL 中，流用<strong>KStream</strong>表示，而表用<strong>KTable</strong>表示。</p>
<p>Kafka Streams 还定义了<strong>GlobalKTable</strong>。本质上它和 KTable 都表征了一个表，里面封装了事件变更流，但是它和 KTable 的最大不同在于，当 Streams 应用程序读取 Kafka 主题数据到 GlobalKTable 时，它会读取主题<strong>所有分区的数据</strong>，而对 KTable 而言，Streams 程序实例只会读取<strong>部分分区的数据</strong>，这主要取决于 Streams 实例的数量。</p>
<h3>时间</h3>
<p>在流处理领域内，精确定义事件时间是非常关键的：一方面，它是决定流处理应用能否实现正确性的前提；另一方面，流处理中时间窗口等操作依赖于时间概念才能正常工作。</p>
<p>常见的时间概念有两类：事件发生时间（Event Time）和事件处理时间（Processing Time）。理想情况下，我们希望这两个时间相等，即事件一旦发生就马上被处理，但在实际场景中，这是不可能的，<strong>Processing Time 永远滞后于 Event Time</strong>，而且滞后程度又是一个高度变化，无法预知，就像“Streaming Systems”一书中的这张图片所展示的那样：</p>
<p><img src="assets/ab8e5206729b484b0a16f2bb9de3a792.png" alt="img" /></p>
<p>该图中的 45°虚线刻画的是理想状态，即 Event Time 等于 Processing Time，而粉色的曲线表征的是真实情况，即 Processing Time 落后于 Event Time，而且落后的程度（Lag）不断变化，毫无规律。</p>
<p>如果流处理应用要实现结果的正确性，就必须要使用基于 Event Time 的时间窗口，而不能使用基于 Processing Time 的时间窗口。</p>
<h3>时间窗口</h3>
<p>所谓的时间窗口机制，就是将流数据沿着时间线切分的过程。常见的时间窗口包括：固定时间窗口（Fixed Windows）、滑动时间窗口（Sliding Windows）和会话窗口（Session Windows）。Kafka Streams 同时支持这三类时间窗口。在后面的例子中，我会详细介绍如何使用 Kafka Streams API 实现时间窗口功能。</p>
<h2>运行 WordCount 实例</h2>
<p>好了，关于 Kafka Streams 及其 DSL 的基本概念我都阐述完了，下面我给出大数据处理领域的 Hello World 实例：WordCount 程序。</p>
<p>每个大数据处理框架第一个要实现的程序基本上都是单词计数。我们来看下 Kafka Streams DSL 如何实现 WordCount。我先给出完整代码，稍后我会详细介绍关键部分代码的含义以及运行它的方法。</p>
<pre><code>package kafkalearn.demo.wordcount;
 
 
import org.apache.kafka.clients.consumer.ConsumerConfig;
import org.apache.kafka.common.serialization.Serdes;
import org.apache.kafka.streams.KafkaStreams;
import org.apache.kafka.streams.StreamsBuilder;
import org.apache.kafka.streams.StreamsConfig;
import org.apache.kafka.streams.kstream.KStream;
import org.apache.kafka.streams.kstream.KTable;
import org.apache.kafka.streams.kstream.Produced;
 
 
import java.util.Arrays;
import java.util.Locale;
import java.util.Properties;
import java.util.concurrent.CountDownLatch;
 
 
public final class WordCountDemo {
    public static void main(final String[] args) {
        final Properties props = new Properties();
        props.put(StreamsConfig.APPLICATION_ID_CONFIG, &quot;wordcount-stream-demo&quot;);
        props.put(StreamsConfig.BOOTSTRAP_SERVERS_CONFIG, &quot;localhost:9092&quot;);
        props.put(StreamsConfig.DEFAULT_KEY_SERDE_CLASS_CONFIG, Serdes.String().getClass().getName());
        props.put(StreamsConfig.DEFAULT_VALUE_SERDE_CLASS_CONFIG, Serdes.String().getClass().getName());
        props.put(ConsumerConfig.AUTO_OFFSET_RESET_CONFIG, &quot;earliest&quot;);
 
 
        final StreamsBuilder builder = new StreamsBuilder();
 
 
        final KStream&lt;String, String&gt; source = builder.stream(&quot;wordcount-input-topic&quot;);
 
 
        final KTable&lt;String, Long&gt; counts = source
            .flatMapValues(value -&gt; Arrays.asList(value.toLowerCase(Locale.getDefault()).split(&quot; &quot;)))
            .groupBy((key, value) -&gt; value)
            .count();
 
 
        counts.toStream().to(&quot;wordcount-output-topic&quot;, Produced.with(Serdes.String(), Serdes.Long()));
 
 
        final KafkaStreams streams = new KafkaStreams(builder.build(), props);
        final CountDownLatch latch = new CountDownLatch(1);
 
 
        Runtime.getRuntime().addShutdownHook(new Thread(&quot;wordcount-stream-demo-jvm-hook&quot;) {
            @Override
            public void run() {
                streams.close();
                latch.countDown();
            }
        });
 
 
        try {
            streams.start();
            latch.await();
        } catch (final Throwable e) {
            System.exit(1);
        }
        System.exit(0)
</code></pre>
<p>在程序开头，我构造了一个 Properties 对象实例，对 Kafka Streams 程序的关键参数进行了赋值，比如 application id、bootstrap servers 和默认的 KV 序列化器（Serializer）和反序列化器（Deserializer）。其中，application id 是 Kafka Streams 应用的唯一标识，必须要显式地指定。默认的 KV 序列化器、反序列化器是为消息的 Key 和 Value 进行序列化和反序列化操作的。</p>
<p>接着，我构造了一个 StreamsBuilder 对象，并使用该对象实例创建了一个 KStream，这个 KStream 从名为 wordcount-input-topic 的 Kafka 主题读取消息。该主题消息由一组单词组成，单词间用空格分割，比如 zhangsan lisi wangwu。</p>
<p>由于我们要进行单词计数，所以就需要将消息中的单词提取出来。有了前面的概念介绍，你应该可以猜到，KTable 是很合适的存储结构，因此，下一步就是将刚才的这个 KStream 转换成 KTable。</p>
<p>我们先对单词进行分割，这里我用到了 flatMapValues 方法，代码中的 Lambda 表达式实现了从消息中提取单词的逻辑。由于 String.split() 方法会返回多个单词，因此我们使用 flatMapValues 而不是 mapValues。原因是，前者能够将多个元素“打散”成一组单词，而如果使用后者，我们得到的就不是一组单词，而是多组单词了。</p>
<p>这些都做完之后，程序调用 groupBy 方法对单词进行分组。由于是计数，相同的单词必须被分到一起，然后就是调用 count 方法对每个出现的单词进行统计计数，并保存在名为 counts 的 KTable 对象中。</p>
<p>最后，我们将统计结果写回到 Kafka 中。由于 KTable 是表，是静态的数据，因此这里要先将其转换成 KStream，然后再调用 to 方法写入到名为 wordcount-output-topic 的主题中。此时，counts 中事件的 Key 是单词，而 Value 是统计个数，因此我们在调用 to 方法时，同时指定了 Key 和 Value 的序列化器，分别是字符串序列化器和长整型序列化器。</p>
<p>至此，Kafka Streams 的流计算逻辑就编写完了，接下来就是构造 KafkaStreams 实例并启动它了。通常来说，这部分的代码都是类似的，即调用 start 方法启动整个流处理应用，以及配置一个 JVM 关闭钩子（Shutdown Hook）实现流处理应用的关闭等。</p>
<p>总体来说，Kafka Streams DSL 实现 WordCount 的方式还是很简单的，仅仅调用几个操作算子就轻松地实现了分布式的单词计数实时处理功能。事实上，现在主流的实时流处理框架越来越倾向于这样的设计思路，即通过提供丰富而便捷的开箱即用操作算子，简化用户的开发成本，采用类似于搭积木的方式快捷地构建实时计算应用。</p>
<p>待启动该 Java 程序之后，你需要创建出对应的输入和输出主题，并向输入主题不断地写入符合刚才所说的格式的单词行，之后，你需要运行下面的命令去查看输出主题中是否正确地统计了你刚才输入的单词个数：</p>
<pre><code>bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 \
    --topic wordcount-output-topic \
    --from-beginning \
    --formatter kafka.tools.DefaultMessageFormatter \
    --property print.key=true \
    --property print.value=true \
    --property key.deserializer=org.apache.kafka.common.serialization.StringDeserializer \
    --property value.deserializer=org.apache.kafka.common.serialization.LongDeserializer
</code></pre>
<h2>开发 API</h2>
<p>介绍了具体的例子之后，我们来看下 Kafka Streams 还提供了哪些功能强大的 API。我们可以重点关注两个方面，一个是常见的操作算子，另一个是时间窗口 API。</p>
<h3>常见操作算子</h3>
<p>操作算子的丰富程度和易用性是衡量流处理框架受欢迎程度的重要依据之一。Kafka Streams DSL 提供了很多开箱即用的操作算子，大体上分为两大类：<strong>无状态算子和有状态算子</strong>。下面我就向你分别介绍几个经常使用的算子。</p>
<p><strong>在无状态算子中，filter 的出场率是极高的</strong>。它执行的就是过滤的逻辑。依然拿 WordCount 为例，假设我们只想统计那些以字母 s 开头的单词的个数，我们可以在执行完 flatMapValues 后增加一行代码，代码如下：</p>
<pre><code>.filter(((key, value) -&gt; value.startsWith(&quot;s&quot;)))
</code></pre>
<p><strong>另一个常见的无状态算子当属 map 一族了</strong>。Streams DSL 提供了很多变体，比如 map、mapValues、flatMap 和 flatMapValues。我们已经见识了 flatMapValues 的威力，其他三个的功能也是类似的，只是所有带 Values 的变体都只对消息体执行转换，不触及消息的 Key，而不带 Values 的变体则能修改消息的 Key。</p>
<p>举个例子，假设当前消息没有 Key，而 Value 是单词本身，现在我们想要将消息变更成这样的 KV 对，即 Key 是单词小写，而 Value 是单词长度，那么我们可以调用 map 方法，代码如下：</p>
<pre><code>KStream&lt;String, Integer&gt; transformed = stream.map(
    (key, value) -&gt; KeyValue.pair(value.toLowerCase(), value.length()));
</code></pre>
<p>最后，我再介绍一组调试用的无状态算子：<strong>print 和 peek</strong>。Streams DSL 支持你使用这两个方法查看你的消息流中的事件。这两者的区别在于，print 是终止操作，一旦你调用了 print 方法，后面就不能再调用任何其他方法了，而 peek 则允许你在查看消息流的同时，依然能够继续对其进行处理，比如下面这两段代码所示：</p>
<pre><code>stream.print(Printed.toFile(&quot;streams.out&quot;).withLabel(&quot;debug&quot;));
stream.peek((key, value) -&gt; System.out.println(&quot;key=&quot; + key + &quot;, value=&quot; + value)).map(...);
</code></pre>
<p>常见的有状态操作算子主要涉及聚合（Aggregation）方面的操作，比如计数、求和、求平均值、求最大最小值等。Streams DSL 目前只提供了 count 方法用于计数，其他的聚合操作需要你自行使用 API 实现。</p>
<p>假设我们有个消息流，每条事件就是一个单独的整数，现在我们想要对其中的偶数进行求和，那么 Streams DSL 中的实现方法如下：</p>
<pre><code>final KTable&lt;Integer, Integer&gt; sumOfEvenNumbers = input
         .filter((k, v) -&gt; v % 2 == 0)
         .selectKey((k, v) -&gt; 1)
         .groupByKey()
         .reduce((v1, v2) -&gt; v1 + v2);
</code></pre>
<p>我简单解释一下 selectKey 调用。由于我们要对所有事件中的偶数进行求和，因此需要把这些消息的 Key 都调整成相同的值，因此这里我使用 selectKey 指定了一个 Dummy Key 值，即上面这段代码中的数值 1。它没有任何含义，仅仅是让所有消息都赋值上这个 Key 而已。真正核心的代码在于 reduce 调用，它是执行求和的关键逻辑。</p>
<h3>时间窗口实例</h3>
<p>前面说过，Streams DSL 支持 3 类时间窗口。前两类窗口通过<strong>TimeWindows.of 方法</strong>来实现，会话窗口通过<strong>SessionWindows.with</strong>来实现。</p>
<p>假设在刚才的 WordCount 实例中，我们想每一分钟统计一次单词计数，那么需要在调用 count 之前增加下面这行代码：</p>
<pre><code>.windowedBy(TimeWindows.of(Duration.ofMinutes(1)))
</code></pre>
<p>同时，你还需要修改 counts 的类型，此时它不再是 KTable&lt;String, Long&gt; 了，而变成了 KTable&lt;Windowed, Long&gt;，因为引入了时间窗口，所以，事件的 Key 也必须要携带时间窗口的信息。除了这两点变化，WordCount 其他部分代码都不需要修改。</p>
<p>可见，Streams DSL 在 API 封装性方面还是做得很好的，通常你只需要增加或删减几行代码，就能实现处理逻辑的修改了。</p>
<h2>小结</h2>
<p>好了，我们来小结一下。今天我跟你分享了 Kafka Streams 以及 DSL 的背景与概念，然后我根据实例展示了 WordCount 单词计数程序以及运行方法，最后，针对常见的操作算子和时间窗口，我给出了示例代码，这些内容应该可以帮你应对大部分的流处理开发。另外，我建议你经常性地查询一下<a href="https://kafka.apache.org/23/documentation/streams/developer-guide/dsl-api.html#aggregating">官网文档</a>，去学习一些更深入更高级的用法，比如固定时间窗口的用法。在很多场景中，我们都想知道过去一段时间内企业某个关键指标的值是多少，如果要实现这个需求，时间窗口是必然要涉及到的。</p>
<p><img src="assets/dcc10168b7e3fdc43a47effdba45304d.jpg" alt="img" /></p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="40&#32;&#32;Kafka&#32;Streams与其他流处理平台的差异在哪里？.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="42&#32;&#32;Kafka&#32;Streams在金融领域的应用.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b4345b098c570ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
