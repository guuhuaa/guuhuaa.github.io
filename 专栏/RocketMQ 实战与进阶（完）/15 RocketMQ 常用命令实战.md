<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>15 RocketMQ 常用命令实战.md</title>
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

                    <a class="current-tab" href="15&#32;RocketMQ&#32;常用命令实战.md">15 RocketMQ 常用命令实战.md</a>
                    

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

                    
                    <a href="22&#32;RocketMQ&#32;集群踩坑记.md">22 RocketMQ 集群踩坑记.md</a>

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
                        <div><h1>15 RocketMQ 常用命令实战</h1>
<p>本篇整理在运维 RocketMQ 集群时的常用命令，明白命令的含义，在集群运维时得心应手，下面命令均在实际环境中执行过。</p>
<h3>集群命令汇总</h3>
<h4><strong>集群列表</strong></h4>
<p>命令 clusterList 用于查看集群各个节点的运行情况。可以看到该集群中有几个节点、主节点还是从节点、以及每个节点的写入 TPS 和读出的 TPS 等。</p>
<p>命令示例：</p>
<pre><code>$ bin/mqadmin clusterList -n x.x.x.x:9876
RocketMQLog:WARN No appenders could be found for logger (io.netty.util.internal.PlatformDependent0).
RocketMQLog:WARN Please initialize the logger system properly.
#Cluster Name     #Broker Name            #BID  #Addr                  #Version                #InTPS(LOAD)       #OutTPS(LOAD) #PCWait(ms) #Hour #SPACE
fat_mq            fat_mq_c                0     x.x.x.x:10911    V4_7_0                 262.95(0,0ms)       259.85(0,0ms)          0 55.09 0.3130

</code></pre>
<p><strong>字段含义</strong></p>
<table>
<thead>
<tr>
<th align="left">名称</th>
<th align="left">含义</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">-n</td>
<td align="left">Nameserver 地址</td>
</tr>
<tr>
<td align="left">Cluster Name</td>
<td align="left">集群名称</td>
</tr>
<tr>
<td align="left">Broker Name</td>
<td align="left">节点 Broker 名称</td>
</tr>
<tr>
<td align="left">BID</td>
<td align="left">Broker ID （0 为主节点，从节点非 0 表示）</td>
</tr>
<tr>
<td align="left">Addr</td>
<td align="left">节点地址（ip:port）</td>
</tr>
<tr>
<td align="left">Version</td>
<td align="left">RocketMQ 的版本号</td>
</tr>
<tr>
<td align="left">InTPS</td>
<td align="left">节点每秒写入的消息数量</td>
</tr>
<tr>
<td align="left">OutTPS</td>
<td align="left">节点每秒读出的消息数量</td>
</tr>
<tr>
<td align="left">PCWait</td>
<td align="left">pageCacheLockTimeMills（消息落盘会加锁，当前时间与最后一次加锁的差值）</td>
</tr>
<tr>
<td align="left">Hour</td>
<td align="left">磁盘存储多久的有效消息（当前时间与磁盘存储最早的一条消息时间戳的差值）</td>
</tr>
<tr>
<td align="left">SPACE</td>
<td align="left">磁盘已使用的占比</td>
</tr>
</tbody>
</table>
<h4><strong>集群中资源吞吐</strong></h4>
<p>命令 statsAll 可以查看集群中所有主题/消费组的实时吞吐情况。</p>
<p><strong>命令示例</strong></p>
<pre><code>$ bin/mqadmin statsAll -n x.x.x.x:9876
RocketMQLog:WARN No appenders could be found for logger (io.netty.util.internal.PlatformDependent0).
RocketMQLog:WARN Please initialize the logger system properly.
#Topic                            #Consumer Group                  #Accumulation      #InTPS     #OutTPS   #InMsg24Hour  #OutMsg24Hour
trade_eticket_created_topic       trade_eticket_created_consumer              0        0.00        0.00              0              0

</code></pre>
<p><strong>字段含义</strong></p>
<table>
<thead>
<tr>
<th align="left">名称</th>
<th align="left">含义</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">-n</td>
<td align="left">Nameserver 地址</td>
</tr>
<tr>
<td align="left">-a</td>
<td align="left">只打印活动的主题</td>
</tr>
<tr>
<td align="left">-t</td>
<td align="left">只打印指定的主题</td>
</tr>
<tr>
<td align="left">Topic</td>
<td align="left">主题名称</td>
</tr>
<tr>
<td align="left">Consumer Group</td>
<td align="left">消费组名称</td>
</tr>
<tr>
<td align="left">Accumulation</td>
<td align="left">消息堆积数量</td>
</tr>
<tr>
<td align="left">InTPS</td>
<td align="left">该主题每秒写入的消息数量</td>
</tr>
<tr>
<td align="left">OutTPS</td>
<td align="left">该消费组每秒消费的消息数量</td>
</tr>
<tr>
<td align="left">InMsg24Hour</td>
<td align="left">该主题 24 小时写入的消息总数</td>
</tr>
<tr>
<td align="left">OutMsg24Hour</td>
<td align="left">该消费组 24 小时消费的消息总数</td>
</tr>
</tbody>
</table>
<h3>主题命令汇总</h3>
<h4><strong>主题列表</strong></h4>
<p>通过 topicList 列出集群中的所有主题。</p>
<p>命令示例：</p>
<pre><code>$ bin/mqadmin topicList -n x.x.x.x:9876
RocketMQLog:WARN No appenders could be found for logger (io.netty.util.internal.PlatformDependent0).
RocketMQLog:WARN Please initialize the logger system properly.
mq_demo1_topic
mq_demo1_topic
mq_demo2_topic
...

</code></pre>
<p>字段含义：</p>
<table>
<thead>
<tr>
<th align="left">名称</th>
<th align="left">含义</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">-n</td>
<td align="left">Nameserver 地址</td>
</tr>
</tbody>
</table>
<h4><strong>主题创建/修改</strong></h4>
<p>使用 updateTopic 创建主题，也可以用该命令修改主题配置，例如：队列数量、权限等。</p>
<p>命令示例：</p>
<pre><code>$ bin/mqadmin updateTopic -n x.x.x.x:9876 -c fat_mq -t mq_demo_topic
RocketMQLog:WARN No appenders could be found for logger (io.netty.util.internal.PlatformDependent0).
RocketMQLog:WARN Please initialize the logger system properly.
create topic to x.x.x.x:10911 success.
TopicConfig [topicName=mq_demo_topic, readQueueNums=8, writeQueueNums=8, perm=RW-, topicFilterType=SINGLE_TAG, topicSysFlag=0, order=false]

</code></pre>
<p>字段含义：</p>
<table>
<thead>
<tr>
<th align="left">名称</th>
<th align="left">含义</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">-n</td>
<td align="left">Nameserver 地址</td>
</tr>
<tr>
<td align="left">-c</td>
<td align="left">集群名称</td>
</tr>
<tr>
<td align="left">-t</td>
<td align="left">要创建的 Topic 名称</td>
</tr>
<tr>
<td align="left">topicName</td>
<td align="left">主题名称</td>
</tr>
<tr>
<td align="left">readQueueNums</td>
<td align="left">读队列数量</td>
</tr>
<tr>
<td align="left">writeQueueNums</td>
<td align="left">写队列数量</td>
</tr>
<tr>
<td align="left">perm</td>
<td align="left">主题权限 RW 表示该主题拥有读写权限</td>
</tr>
<tr>
<td align="left">topicFilterType</td>
<td align="left">消息过滤类型</td>
</tr>
<tr>
<td align="left">topicSysFlag</td>
<td align="left">主题系统标记</td>
</tr>
<tr>
<td align="left">order</td>
<td align="left">是否有序主题</td>
</tr>
</tbody>
</table>
<h4><strong>主题路由</strong></h4>
<p>使用 topicRoute 命令可以查看 Topic 的路由信息，队列所在的 Broker 以及 Broker 所在的集群等。</p>
<p>命令示例：</p>
<pre><code>$ bin/mqadmin topicRoute -n x.x.x.x:9876 -t mq_demo_topic
RocketMQLog:WARN No appenders could be found for logger (io.netty.util.internal.PlatformDependent0).
RocketMQLog:WARN Please initialize the logger system properly.
{
    &quot;brokerDatas&quot;:[
        {
            &quot;brokerAddrs&quot;:{0:&quot;x.x.x.x:10911&quot;
            },
            &quot;brokerName&quot;:&quot;fat_mq_c&quot;,
            &quot;cluster&quot;:&quot;fat_mq&quot;
        }
    ],
    &quot;filterServerTable&quot;:{},
    &quot;queueDatas&quot;:[
        {
            &quot;brokerName&quot;:&quot;fat_mq_c&quot;,
            &quot;perm&quot;:6,
            &quot;readQueueNums&quot;:8,
            &quot;topicSynFlag&quot;:0,
            &quot;writeQueueNums&quot;:8
        }
    ]
}

</code></pre>
<p>字段含义：</p>
<table>
<thead>
<tr>
<th align="left">名称</th>
<th align="left">含义</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">-n</td>
<td align="left">Nameserver 地址</td>
</tr>
<tr>
<td align="left">-t</td>
<td align="left">主题名称</td>
</tr>
<tr>
<td align="left">brokerDatas</td>
<td align="left">broker 信息地址、节点名称、所在集群</td>
</tr>
<tr>
<td align="left">queueDatas</td>
<td align="left">队列数量、队列所在的 broker、权限等</td>
</tr>
</tbody>
</table>
<h4><strong>主题状态</strong></h4>
<p>使用 topicStatus 查看主题状态情况，例如：最小偏移量、最大偏移量、最新更新时间等。</p>
<p>命令示例：</p>
<pre><code>$ bin/mqadmin topicStatus -n x.x.x.x:9876 -t mq_demo_topic
RocketMQLog:WARN No appenders could be found for logger (io.netty.util.internal.PlatformDependent0).
RocketMQLog:WARN Please initialize the logger system properly.
#Broker Name                      #QID  #Min Offset           #Max Offset             #Last Updated
fat_mq_c                          0     6                     10                      2020-07-24 14:29:57,707
fat_mq_c                          1     4                     8                       2020-07-24 14:31:32,213
fat_mq_c                          2     20                    22                      2020-07-24 14:35:52,752
fat_mq_c                          3     14                    20                      2020-07-24 14:28:34,287

</code></pre>
<p>字段含义：</p>
<table>
<thead>
<tr>
<th align="left">名称</th>
<th align="left">含义</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">-n</td>
<td align="left">NameServer 地址</td>
</tr>
<tr>
<td align="left">-t</td>
<td align="left">主题名称</td>
</tr>
<tr>
<td align="left">Broker Name</td>
<td align="left">节点名称</td>
</tr>
<tr>
<td align="left">QID</td>
<td align="left">Queue ID 队列编号</td>
</tr>
<tr>
<td align="left">Min Offset</td>
<td align="left">该队列最小偏移量</td>
</tr>
<tr>
<td align="left">Max Offset</td>
<td align="left">该队列最大偏移量</td>
</tr>
<tr>
<td align="left">Last Updated</td>
<td align="left">最新写入消息的时间戳</td>
</tr>
</tbody>
</table>
<h4><strong>主题权限</strong></h4>
<p>可以通过 updateTopicPerm 修改主题的权限，有三种类型：写权限用 2 表示、读权限用 4 表示、读写权限用 6 表示。下面示例中将主题从读写权限变更为写权限。</p>
<p>命令示例：</p>
<pre><code>$ bin/mqadmin updateTopicPerm -c fat_mq -t mq_demo_topic -p 2 -n x.x.x.x:9876
RocketMQLog:WARN No appenders could be found for logger (io.netty.util.internal.PlatformDependent0).
RocketMQLog:WARN Please initialize the logger system properly.
update topic perm from 6 to 2 in x.x.x.x:10911 success.

</code></pre>
<p>字段含义：</p>
<table>
<thead>
<tr>
<th align="left">名称</th>
<th align="left">含义</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">-c</td>
<td align="left">集群名称</td>
</tr>
<tr>
<td align="left">-t</td>
<td align="left">主题名称</td>
</tr>
<tr>
<td align="left">-p</td>
<td align="left">权限（2:W，4:R，6:WR）</td>
</tr>
<tr>
<td align="left">-n</td>
<td align="left">NameServer 地址</td>
</tr>
</tbody>
</table>
<h4><strong>主题删除</strong></h4>
<p>通过 deleteTopic 删除主题，可以通过该命令对废弃主题进行删除。</p>
<p>命令示例：</p>
<pre><code>$ bin/mqadmin deleteTopic -n x.x.x.x:9876 -t mq_demo_topic -c fat_mq
RocketMQLog:WARN No appenders could be found for logger (io.netty.util.internal.PlatformDependent0).
RocketMQLog:WARN Please initialize the logger system properly.
delete topic [mq_demo_topic] from cluster [fat_mq] success.
delete topic [mq_demo_topic] from NameServer success.

</code></pre>
<p>字段含义：</p>
<table>
<thead>
<tr>
<th align="left">名称</th>
<th align="left">含义</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">-n</td>
<td align="left">Nameserver 地址</td>
</tr>
<tr>
<td align="left">-t</td>
<td align="left">主题名称</td>
</tr>
<tr>
<td align="left">-c</td>
<td align="left">集群名称</td>
</tr>
</tbody>
</table>
<h3>消费组命令汇总</h3>
<h4><strong>消费组创建</strong></h4>
<p>通过 updateSubGroup 可以创建消费组，创建成功会返回该消费组的配置信息。</p>
<p>命令示例：</p>
<pre><code>$ bin/mqadmin updateSubGroup -n x.x.x.x:9876 -c fat_mq -g mq_demo_consumer
RocketMQLog:WARN No appenders could be found for logger (io.netty.util.internal.PlatformDependent0).
RocketMQLog:WARN Please initialize the logger system properly.
create subscription group to x.x.x.x:10911 success.
SubscriptionGroupConfig [groupName=mq_demo_consumer, consumeEnable=true, consumeFromMinEnable=false, consumeBroadcastEnable=false, retryQueueNums=1, retryMaxTimes=16, brokerId=0, whichBrokerWhenConsumeSlowly=1, notifyConsumerIdsChangedEnable=true]

</code></pre>
<p>字段含义：</p>
<table>
<thead>
<tr>
<th align="left">名称</th>
<th align="left">含义</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">-n</td>
<td align="left">Nameserver 地址</td>
</tr>
<tr>
<td align="left">-c</td>
<td align="left">集群名称</td>
</tr>
<tr>
<td align="left">-g</td>
<td align="left">消费组名称</td>
</tr>
<tr>
<td align="left">groupName</td>
<td align="left">消费组名称</td>
</tr>
<tr>
<td align="left">consumeEnable</td>
<td align="left">是否开启消费，默认开启</td>
</tr>
<tr>
<td align="left">consumeFromMinEnable</td>
<td align="left">是否从最小位点消费，默认 false</td>
</tr>
<tr>
<td align="left">consumeBroadcastEnable</td>
<td align="left">是否开启广播消费，默认 false</td>
</tr>
<tr>
<td align="left">retryQueueNums</td>
<td align="left">重试队列数量，默认为 1</td>
</tr>
<tr>
<td align="left">retryMaxTimes</td>
<td align="left">消费重试次数，默认 16 次</td>
</tr>
<tr>
<td align="left">brokerId</td>
<td align="left">消费组所在的 brokerId</td>
</tr>
<tr>
<td align="left">whichBrokerWhenConsumeSlowly</td>
<td align="left">当 Master 节点消费慢时，默认在从节点 ID 为 1 的 broker 消费</td>
</tr>
</tbody>
</table>
<h4><strong>消费者状态</strong></h4>
<p>通过 consumerStatus 可以查看各个消费者的情况，包括版本、消费组名称等。</p>
<p>命令示例：</p>
<pre><code>$ bin/mqadmin consumerStatus -g mq_demo_consumer -n x.x.x.x:9876
RocketMQLog:WARN No appenders could be found for logger (io.netty.util.internal.PlatformDependent0).
RocketMQLog:WARN Please initialize the logger system properly.
001  <a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="84e7ebeaf7f1e9e1f6a9e7e8ede1eaf0a9ede0a9e0edf7e5f7f0e1f6dbe9f5a9fcaafcaafcaafcc4b6b5b5b3b5">[email&#160;protected]</a> V4_7_0               1595768036031/<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="6704080914120a02154a040b0e0209134a0e034a030e140614130215380a164a1f491f491f491f275556565056">[email&#160;protected]</a>
002  <a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="12717d7c61677f77603f717e7b777c663f7b763f767b6173616677604d7f633f6a3c6a3c6a3c6a52232b222a2b">[email&#160;protected]</a> V4_7_0               1595768036031/<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="13707c7d60667e76613e707f7a767d673e7a773e777a6072606776614c7e623e6b3d6b3d6b3d6b53222a232b2a">[email&#160;protected]</a>

</code></pre>
<p>字段含义：</p>
<table>
<thead>
<tr>
<th align="left">名称</th>
<th align="left">含义</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">-g</td>
<td align="left">消费组名称</td>
</tr>
<tr>
<td align="left">-n</td>
<td align="left">NameServer 地址</td>
</tr>
<tr>
<td align="left">输出第一列</td>
<td align="left">第几个消费者</td>
</tr>
<tr>
<td align="left">输出第二列</td>
<td align="left">clientId</td>
</tr>
<tr>
<td align="left">输出第三列</td>
<td align="left">该消费者使用的客户端 RocketMQ 版本</td>
</tr>
<tr>
<td align="left">输出第四列</td>
<td align="left">文件路径（filePath），该文件记录了消费者详细信息</td>
</tr>
</tbody>
</table>
<h4><strong>消费组进度</strong></h4>
<p>通过 consumerProgress 查看该消费组在订阅主题中每个 Queue 消息的消费进度。</p>
<p>命令示例：</p>
<pre><code>$ bin/mqadmin consumerProgress -g pglog_rmq_t_biz_extend_synchbase_consumer -n x.x.x.x:9876
RocketMQLog:WARN No appenders could be found for logger (io.netty.util.internal.PlatformDependent0).
RocketMQLog:WARN Please initialize the logger system properly.
#Topic                            #Broker Name                      #QID  #Broker Offset        #Consumer Offset      #Client IP           #Diff                 #LastTime
pglog_rmq_t_biz_extend            disaster_mq_a                     0     17227343              17227343              N/A                  0                     2020-07-26 21:09:30
pglog_rmq_t_biz_extend            disaster_mq_a                     1     16588873              16588873              N/A                  0                     2020-07-26 21:09:30
pglog_rmq_t_biz_extend            disaster_mq_a                     2     12053429              12053429              N/A                  0                     2020-07-26 21:09:35
...
Consume TPS: 3.98
Diff Total: 6

</code></pre>
<p>字段含义：</p>
<table>
<thead>
<tr>
<th align="left">名称</th>
<th align="left">含义</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">-g</td>
<td align="left">消费组名称</td>
</tr>
<tr>
<td align="left">-n</td>
<td align="left">NameServer 地址</td>
</tr>
<tr>
<td align="left">Topic</td>
<td align="left">订阅的主题</td>
</tr>
<tr>
<td align="left">Broker Name</td>
<td align="left">订阅主题所在的 Broker</td>
</tr>
<tr>
<td align="left">QID</td>
<td align="left">订阅主题的 Queue ID</td>
</tr>
<tr>
<td align="left">Broker Offset</td>
<td align="left">该 Queue 存储的消息偏移量</td>
</tr>
<tr>
<td align="left">Consumer Offset</td>
<td align="left">该 Queue 消费的消息偏移量</td>
</tr>
<tr>
<td align="left">Diff</td>
<td align="left">消息堆积情况</td>
</tr>
<tr>
<td align="left">LastTime</td>
<td align="left">上次消费消息的时间</td>
</tr>
<tr>
<td align="left">Consume TPS</td>
<td align="left">每秒钟消费消息的数量</td>
</tr>
<tr>
<td align="left">Diff Total</td>
<td align="left">消息堆积总数</td>
</tr>
</tbody>
</table>
<h4><strong>消息回溯</strong></h4>
<p>通过 resetOffsetByTime 可以将消费组重新定位到过去某个时间点重新开始消费。</p>
<p>命令示例：</p>
<pre><code>$ bin/mqadmin resetOffsetByTime -n x.x.x.x:9876 -g melon_consumer_0010 -t melon_test_0010 -s now
RocketMQLog:WARN No appenders could be found for logger (io.netty.util.internal.PlatformDependent0).
RocketMQLog:WARN Please initialize the logger system properly.
rollback consumer offset by specified group[melon_consumer_0010], topic[melon_test_0010], force[true], timestamp(string)[now], timestamp(long)[1595900214141]
#brokerName                               #queueId                                  #offset
dev_mq_b                                  5                                         281499
dev_mq_b                                  3                                         285922
dev_mq_d                                  5                                         12335
dev_mq_b                                  4                                         286157
dev_mq_b                                  1                                         279566
dev_mq_d                                  3                                         12336
dev_mq_b                                  2                                         281142
dev_mq_d                                  4                                         12333
dev_mq_d                                  1                                         12335
dev_mq_b                                  0                                         282808
dev_mq_d                                  2                                         12338
dev_mq_d                                  0                                         12343

</code></pre>
<p>字段含义：</p>
<table>
<thead>
<tr>
<th align="left">名称</th>
<th align="left">含义</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">-n</td>
<td align="left">NameServer 地址</td>
</tr>
<tr>
<td align="left">-g</td>
<td align="left">消费组名称</td>
</tr>
<tr>
<td align="left">-t</td>
<td align="left">消费组定于的主题名称</td>
</tr>
<tr>
<td align="left">-s</td>
<td align="left">回溯的时间戳（例如：1595815028792，now 表示当前时间）</td>
</tr>
<tr>
<td align="left">brokerName</td>
<td align="left">节点名称</td>
</tr>
<tr>
<td align="left">queueId</td>
<td align="left">队列 ID</td>
</tr>
<tr>
<td align="left">offset</td>
<td align="left">回溯后该队列消费的偏移量</td>
</tr>
</tbody>
</table>
<h3>Broker 命令汇总</h3>
<h4><strong>Broker 状态</strong></h4>
<p>通过 brokerStatus 命令了解集群中某个 Broker 的运行情况，例如：启动时间、版本、吞吐情况等。</p>
<p>命令示例：</p>
<pre><code>$ bin/mqadmin brokerStatus -b x.x.x.x:10911 -n x.x.x.x:9876
RocketMQLog:WARN No appenders could be found for logger (io.netty.util.internal.PlatformDependent0).
RocketMQLog:WARN Please initialize the logger system properly.
EndTransactionQueueSize         : 0
EndTransactionThreadPoolQueueCapacity: 100000
bootTimestamp                   : 1591673160936
brokerVersion                   : 353
brokerVersionDesc               : V4_7_0
commitLogDirCapacity            : Total : 98.3 GiB, Free : 93.5 GiB.
commitLogDiskRatio              : 0.04929098258492175
commitLogMaxOffset              : 3473383494
commitLogMinOffset              : 2147483648
consumeQueueDiskRatio           : 0.04929098258492175
dispatchBehindBytes             : 0
dispatchMaxBuffer               : 0
earliestMessageTimeStamp        : 1595621861014
getFoundTps                     : 0.0 0.0 0.0
getMessageEntireTimeMax         : 290
getMissTps                      : 786.5213478652134 783.8549478385495 783.5753864100321
getTotalTps                     : 786.5213478652134 783.8549478385495 783.5753864100321
getTransferedTps                : 0.0 0.0 0.0
msgGetTotalTodayMorning         : 2713099
msgGetTotalTodayNow             : 2713131
msgGetTotalYesterdayMorning     : 1478152
msgPutTotalTodayMorning         : 9303513
msgPutTotalTodayNow             : 9336203
msgPutTotalYesterdayMorning     : 6247199
pageCacheLockTimeMills          : 0
pullThreadPoolQueueCapacity     : 100000
pullThreadPoolQueueHeadWaitTimeMills: 0
pullThreadPoolQueueSize         : 0
putMessageAverageSize           : 326.0440501347282
putMessageDistributeTime        : [&lt;=0ms]:11 [0~10ms]:0 [10~50ms]:0 [50~100ms]:0 [100~200ms]:0 [200~500ms]:0 [500ms~1s]:0 [1~2s]:0 [2~3s]:0 [3~4s]:0 [4~5s]:0 [5~10s]:0 [10s~]:0
putMessageEntireTimeMax         : 930
putMessageSizeTotal             : 3044013439
putMessageTimesTotal            : 9336203
putTps                          : 0.9999000099990001 0.9999000099990001 0.999875015623047
queryThreadPoolQueueCapacity    : 20000
queryThreadPoolQueueHeadWaitTimeMills: 0
queryThreadPoolQueueSize        : 0
remainHowManyDataToCommit       : 0 B
remainHowManyDataToFlush        : 1.1 KiB
remainTransientStoreBufferNumbs : 3
runtime                         : [ 49 days, 21 hours, 38 minutes, 12 seconds ]
scheduleMessageOffset_1         : 2024,2024
scheduleMessageOffset_10        : 1035,1035
scheduleMessageOffset_11        : 885,885
scheduleMessageOffset_12        : 879,879
scheduleMessageOffset_13        : 889,889
scheduleMessageOffset_14        : 640349,640349
scheduleMessageOffset_15        : 848,848
scheduleMessageOffset_16        : 851,851
scheduleMessageOffset_17        : 870,870
scheduleMessageOffset_18        : 1288,1288
scheduleMessageOffset_2         : 1243954,1243954
scheduleMessageOffset_3         : 13682,13682
scheduleMessageOffset_4         : 5965,5965
scheduleMessageOffset_5         : 5134,5134
scheduleMessageOffset_6         : 4741,4741
scheduleMessageOffset_7         : 13475,13475
scheduleMessageOffset_8         : 2530,2530
scheduleMessageOffset_9         : 2270,2270
sendThreadPoolQueueCapacity     : 10000
sendThreadPoolQueueHeadWaitTimeMills: 0
sendThreadPoolQueueSize         : 0
startAcceptSendRequestTimeStamp : 0

</code></pre>
<p>字段含义：</p>
<table>
<thead>
<tr>
<th align="left">名称</th>
<th align="left">含义</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">-b</td>
<td align="left">Broker 的 IP 地址</td>
</tr>
<tr>
<td align="left">-n</td>
<td align="left">Nameserver 地址</td>
</tr>
<tr>
<td align="left">EndTransactionQueueSize</td>
<td align="left">END_TRANSACTION 的线程池请求数</td>
</tr>
<tr>
<td align="left">EndTransactionThreadPoolQueueCapacity</td>
<td align="left">END_TRANSACTION 线程池大小，默认 100000</td>
</tr>
<tr>
<td align="left">bootTimestamp</td>
<td align="left">Broker 启动时间</td>
</tr>
<tr>
<td align="left">brokerVersion</td>
<td align="left">Broker 版本</td>
</tr>
<tr>
<td align="left">brokerVersionDesc</td>
<td align="left">Broker 版本描述</td>
</tr>
<tr>
<td align="left">commitLogDirCapacity</td>
<td align="left">commitLog 目录磁盘使用情况</td>
</tr>
<tr>
<td align="left">commitLogDiskRatio</td>
<td align="left">commitLog 目录磁盘使用百分比</td>
</tr>
<tr>
<td align="left">commitLogMaxOffset</td>
<td align="left">commitLog 最大偏移量</td>
</tr>
<tr>
<td align="left">commitLogMinOffset</td>
<td align="left">commitLog 最小偏移量</td>
</tr>
<tr>
<td align="left">dispatchBehindBytes</td>
<td align="left">已在 commit log 中存储未转发到 consume queue 的数据（单位字节）</td>
</tr>
<tr>
<td align="left">dispatchMaxBuffer</td>
<td align="left">可忽略未被使用</td>
</tr>
<tr>
<td align="left">earliestMessageTimeStamp</td>
<td align="left">存储最早消息的时间戳</td>
</tr>
<tr>
<td align="left">getFoundTps</td>
<td align="left">拉取时被找到的消息 Tps 统计，分别表示前 10s、1 分钟、10 分钟平均 Tps</td>
</tr>
<tr>
<td align="left">getMessageEntireTimeMax</td>
<td align="left">查找单条消息的最大耗时</td>
</tr>
<tr>
<td align="left">getMissTps</td>
<td align="left">拉取时未被找到的消息 Tps 统计，分别表示前 10s、1 分钟、10 分钟平均 Tps</td>
</tr>
<tr>
<td align="left">getTotalTps</td>
<td align="left">拉取时总的消息 Tps 统计，分别表示前 10s、1 分钟、10 分钟平均 Tps</td>
</tr>
<tr>
<td align="left">getTransferedTps</td>
<td align="left">向拉取方传输消息 Tps 统计，分别表示前 10s、1 分钟、10 分钟平均 Tps</td>
</tr>
<tr>
<td align="left">msgGetTotalTodayMorning</td>
<td align="left">截止今天凌晨 12 点从该 broker 拉取的消息总数</td>
</tr>
<tr>
<td align="left">msgGetTotalTodayNow</td>
<td align="left">截止当前时间从该 broker 拉取的消息总数</td>
</tr>
<tr>
<td align="left">msgGetTotalYesterdayMorning</td>
<td align="left">截止昨天凌晨 12 点从该 broker 拉取的消息总数</td>
</tr>
<tr>
<td align="left">msgPutTotalTodayMorning</td>
<td align="left">截止今天凌晨 12 点从该 broker 写入的消息总数</td>
</tr>
<tr>
<td align="left">msgPutTotalTodayNow</td>
<td align="left">截止当前时间从该 broker 写入的消息总数</td>
</tr>
<tr>
<td align="left">msgPutTotalYesterdayMorning</td>
<td align="left">截止昨天凌晨 12 点从该 broker 写入的消息总数</td>
</tr>
<tr>
<td align="left">pageCacheLockTimeMills</td>
<td align="left">消息存储时会加锁，指从加锁现在的时间</td>
</tr>
<tr>
<td align="left">pullThreadPoolQueueCapacity</td>
<td align="left">拉取线程池队列初始容量，默认为 100000</td>
</tr>
<tr>
<td align="left">pullThreadPoolQueueHeadWaitTimeMills</td>
<td align="left">队列头部第一个任务从创建到现在一直未被执行的时间，即：队列第一个任务等待时间</td>
</tr>
<tr>
<td align="left">pullThreadPoolQueueSize</td>
<td align="left">拉取线程池队列当前任务数量</td>
</tr>
<tr>
<td align="left">putMessageAverageSize</td>
<td align="left">写入消息的平均大小</td>
</tr>
<tr>
<td align="left">putMessageDistributeTime</td>
<td align="left">消息存储的耗时分布情况。例如：[&lt;=0ms]:11 指存储时小于等于 0ms 的有 11 条消息</td>
</tr>
<tr>
<td align="left">putMessageEntireTimeMax</td>
<td align="left">消息存储的最大耗时</td>
</tr>
<tr>
<td align="left">putMessageSizeTotal</td>
<td align="left">存储消息的总大小</td>
</tr>
<tr>
<td align="left">putMessageTimesTotal</td>
<td align="left">存储消息的总条数</td>
</tr>
<tr>
<td align="left">putTps</td>
<td align="left">统计 10 秒、1 分钟、10 分钟写入平均 Tps</td>
</tr>
<tr>
<td align="left">queryThreadPoolQueueCapacity</td>
<td align="left">查询线程池队列初始容量，默认为 20000</td>
</tr>
<tr>
<td align="left">queryThreadPoolQueueHeadWaitTimeMills</td>
<td align="left">队列头部第一个任务从创建到现在一直未被执行的时间，即：队列第一个任务等待时间</td>
</tr>
<tr>
<td align="left">queryThreadPoolQueueSize</td>
<td align="left">查询线程池队列当前任务数量</td>
</tr>
<tr>
<td align="left">remainHowManyDataToCommit</td>
<td align="left">剩余多少数据未被写入到 fileChannel</td>
</tr>
<tr>
<td align="left">remainHowManyDataToFlush</td>
<td align="left">剩余多少数据未被刷到磁盘</td>
</tr>
<tr>
<td align="left">remainTransientStoreBufferNumbs</td>
<td align="left">堆外可用缓存区数量，初始大小为 5，每个大小 1G，为在开启队外内存传输时有效</td>
</tr>
<tr>
<td align="left">runtime</td>
<td align="left">该 broker 运行了多久了</td>
</tr>
<tr>
<td align="left">scheduleMessageOffset_1</td>
<td align="left">SCHEDULE_TOPIC_XXXX 第 1 个 Queue 的最大偏移量 （注：延迟消息存储在名字为 SCHEDULE_TOPIC_XXXX 的 topic 中）</td>
</tr>
<tr>
<td align="left">scheduleMessageOffset_10</td>
<td align="left">SCHEDULE_TOPIC_XXXX 第 10 个 Queue 的最大偏移量</td>
</tr>
<tr>
<td align="left">scheduleMessageOffset_11</td>
<td align="left">SCHEDULE_TOPIC_XXXX 第 11 个 Queue 的最大偏移量</td>
</tr>
<tr>
<td align="left">scheduleMessageOffset_12</td>
<td align="left">SCHEDULE_TOPIC_XXXX 第 12 个 Queue 的最大偏移量</td>
</tr>
<tr>
<td align="left">scheduleMessageOffset_13</td>
<td align="left">SCHEDULE_TOPIC_XXXX 第 13 个 Queue 的最大偏移量</td>
</tr>
<tr>
<td align="left">scheduleMessageOffset_14</td>
<td align="left">SCHEDULE_TOPIC_XXXX 第 14 个 Queue 的最大偏移量</td>
</tr>
<tr>
<td align="left">scheduleMessageOffset_15</td>
<td align="left">SCHEDULE_TOPIC_XXXX 第 15 个 Queue 的最大偏移量</td>
</tr>
<tr>
<td align="left">scheduleMessageOffset_16</td>
<td align="left">SCHEDULE_TOPIC_XXXX 第 16 个 Queue 的最大偏移量</td>
</tr>
<tr>
<td align="left">scheduleMessageOffset_17</td>
<td align="left">SCHEDULE_TOPIC_XXXX 第 17 个 Queue 的最大偏移量</td>
</tr>
<tr>
<td align="left">scheduleMessageOffset_18</td>
<td align="left">SCHEDULE_TOPIC_XXXX 第 18 个 Queue 的最大偏移量</td>
</tr>
<tr>
<td align="left">scheduleMessageOffset_2</td>
<td align="left">SCHEDULE_TOPIC_XXXX 第 2 个 Queue 的最大偏移量</td>
</tr>
<tr>
<td align="left">scheduleMessageOffset_3</td>
<td align="left">SCHEDULE_TOPIC_XXXX 第 3 个 Queue 的最大偏移量</td>
</tr>
<tr>
<td align="left">scheduleMessageOffset_4</td>
<td align="left">SCHEDULE_TOPIC_XXXX 第 4 个 Queue 的最大偏移量</td>
</tr>
<tr>
<td align="left">scheduleMessageOffset_5</td>
<td align="left">SCHEDULE_TOPIC_XXXX 第 5 个 Queue 的最大偏移量</td>
</tr>
<tr>
<td align="left">scheduleMessageOffset_6</td>
<td align="left">SCHEDULE_TOPIC_XXXX 第 6 个 Queue 的最大偏移量</td>
</tr>
<tr>
<td align="left">scheduleMessageOffset_7</td>
<td align="left">SCHEDULE_TOPIC_XXXX 第 7 个 Queue 的最大偏移量</td>
</tr>
<tr>
<td align="left">scheduleMessageOffset_8</td>
<td align="left">SCHEDULE_TOPIC_XXXX 第 8 个 Queue 的最大偏移量</td>
</tr>
<tr>
<td align="left">scheduleMessageOffset_9</td>
<td align="left">SCHEDULE_TOPIC_XXXX 第 9 个 Queue 的最大偏移量</td>
</tr>
<tr>
<td align="left">sendThreadPoolQueueCapacity</td>
<td align="left">发送线程池队列初始容量，默认为 10000</td>
</tr>
<tr>
<td align="left">sendThreadPoolQueueHeadWaitTimeMills</td>
<td align="left">队列头部第一个任务从创建到现在一直未被执行的时间，即：队列第一个任务等待时间</td>
</tr>
<tr>
<td align="left">sendThreadPoolQueueSize</td>
<td align="left">发送线程池队列当前任务数量</td>
</tr>
<tr>
<td align="left">startAcceptSendRequestTimeStamp</td>
<td align="left">可以配置在指定的时间 broker 接受客户端发送请求，默认启动后则接受发送请求</td>
</tr>
</tbody>
</table>
<h4><strong>Broker 配置查询</strong></h4>
<p>通过 getBrokerConfig 获取 Broker 的配置信息，下面指提供获取命令，具体参数的含义会在另篇中解读。</p>
<p>命令示例：</p>
<pre><code>$ bin/mqadmin getBrokerConfig -b  x.x.x.x:10911 -n x.x.x.x:9876
RocketMQLog:WARN No appenders could be found for logger (io.netty.util.internal.PlatformDependent0).
RocketMQLog:WARN Please initialize the logger system properly.
============x.x.x.x:10911============
serverSelectorThreads                             =  3
brokerRole                                        =  ASYNC_MASTER
serverSocketRcvBufSize                            =  131072
osPageCacheBusyTimeOutMills                       =  1000
shortPollingTimeMills                             =  1000
clientSocketRcvBufSize                            =  131072
clusterTopicEnable                                =  true
brokerTopicEnable                                 =  true
autoCreateTopicEnable                             =  true
maxErrorRateOfBloomFilter                         =  20
maxMsgsNumBatch                                   =  64
cleanResourceInterval                             =  10000
...

</code></pre>
<h4><strong>Broker 配置更新</strong></h4>
<p>我们可以通过 updateBrokerConfig 命令对 Broker 配置进行热更新，更新后实时生效，不需要重启 Broker 节点。</p>
<p>命令示例：</p>
<pre><code>$ bin/mqadmin updateBrokerConfig -b x.x.x.x:10911 -n dev-mq1.ttbike.com.cn:9876 -k slaveReadEnable -v true
RocketMQLog:WARN No appenders could be found for logger (io.netty.util.internal.PlatformDependent0).
RocketMQLog:WARN Please initialize the logger system properly.
update broker config success, x.x.x.x:10911

</code></pre>
<p>字段含义：</p>
<table>
<thead>
<tr>
<th align="left">名称</th>
<th align="left">含义</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">-b</td>
<td align="left">Broker 地址</td>
</tr>
<tr>
<td align="left">-n</td>
<td align="left">NameServer 地址</td>
</tr>
<tr>
<td align="left">-k</td>
<td align="left">需更新的配置的 key</td>
</tr>
<tr>
<td align="left">-v</td>
<td align="left">需更新配置 key 对应的值</td>
</tr>
</tbody>
</table>
<h4><strong>Broker 发送消息</strong></h4>
<p>可以使用 sendMsgStatus 命令对某个 Broker 发送测试消息，检测该 Broker 运行情况。</p>
<p>命令示例：</p>
<pre><code>bin/mqadmin sendMsgStatus -b dev_mq_d -n x.x.x.x:9876
RocketMQLog:WARN No appenders could be found for logger (io.netty.util.internal.PlatformDependent0).
RocketMQLog:WARN Please initialize the logger system properly.
rt:2ms, SendResult=SendResult [sendStatus=SEND_OK, msgId=0A6F4B60457D5ACF98009C90AD2C0001, offsetMsgId=0A6F4B6000002AC100000000D0B7A942, messageQueue=MessageQueue [topic=dev_mq_d, brokerName=dev_mq_d, queueId=0], queueOffset=4486548]rt:2ms,...

</code></pre>
<p>字段含义：</p>
<table>
<thead>
<tr>
<th align="left">名称</th>
<th align="left">含义</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">-b</td>
<td align="left">Broker 名称</td>
</tr>
<tr>
<td align="left">-n</td>
<td align="left">NameServer 地址</td>
</tr>
<tr>
<td align="left">-c</td>
<td align="left">指定发送消息数量，默认 50 条</td>
</tr>
<tr>
<td align="left">-s</td>
<td align="left">指定发送消息体大小，默认 128k</td>
</tr>
</tbody>
</table>
<h3>消息命令汇总</h3>
<h4><strong>打印主题消息</strong></h4>
<p>通过命令 printMsg 可以打印主题中的消息。</p>
<p>命令示例：</p>
<pre><code>$ bin/mqadmin printMsg -d true -n x.x.x.x:9876 -t melon_dev_test
RocketMQLog:WARN No appenders could be found for logger (io.netty.util.internal.PlatformDependent0).
RocketMQLog:WARN Please initialize the logger system properly.
minOffset=0, maxOffset=0, MessageQueue [topic=melon_dev_test, brokerName=dev_mq_b, queueId=2]minOffset=0, maxOffset=0, MessageQueue [topic=melon_dev_test, brokerName=dev_mq_d, queueId=4]minOffset=0, maxOffset=0, MessageQueue [topic=melon_dev_test, brokerName=dev_mq_b, queueId=4]minOffset=0, maxOffset=0, MessageQueue [topic=melon_dev_test, brokerName=dev_mq_d, queueId=6]minOffset=0, maxOffset=0, MessageQueue [topic=melon_dev_test, brokerName=dev_mq_b, queueId=6]minOffset=0, maxOffset=1, MessageQueue [topic=melon_dev_test, brokerName=dev_mq_d, queueId=8]MessageQueue [topic=melon_dev_test, brokerName=dev_mq_d, queueId=8] no matched msg. status=NO_MATCHED_MSG, offset=1minOffset=0, maxOffset=0, MessageQueue [topic=melon_dev_test, brokerName=dev_mq_b, queueId=8]minOffset=0, maxOffset=0, MessageQueue [topic=melon_dev_test, brokerName=dev_mq_d, queueId=10]minOffset=0, maxOffset=0, MessageQueue [topic=melon_dev_test, brokerName=dev_mq_d, queueId=0]minOffset=0, maxOffset=0, MessageQueue [topic=melon_dev_test, brokerName=dev_mq_b, queueId=0]minOffset=0, maxOffset=0, MessageQueue [topic=melon_dev_test, brokerName=dev_mq_d, queueId=2]minOffset=0, maxOffset=0, MessageQueue [topic=melon_dev_test, brokerName=dev_mq_b, queueId=10]minOffset=0, maxOffset=0, MessageQueue [topic=melon_dev_test, brokerName=dev_mq_d, queueId=12]minOffset=0, maxOffset=0, MessageQueue [topic=melon_dev_test, brokerName=dev_mq_b, queueId=12]minOffset=0, maxOffset=1, MessageQueue [topic=melon_dev_test, brokerName=dev_mq_d, queueId=14]MessageQueue [topic=melon_dev_test, brokerName=dev_mq_d, queueId=14] no matched msg. status=NO_MATCHED_MSG, offset=1minOffset=0, maxOffset=2, MessageQueue [topic=melon_dev_test, brokerName=dev_mq_b, queueId=14]MSGID: 0A6F4BA1743E7BA18F1B9F54E2210028 MessageExt [brokerName=dev_mq_b, queueId=14, storeSize=225, queueOffset=1, sysFlag=0, bornTimestamp=1596205940257, bornHost=/10.111.75.161:42806, storeTimestamp=1596205940257, storeHost=/10.111.75.95:10911, msgId=0A6F4B5F00002A9F000000138873E059, commitLogOffset=83893674073, bodyCRC=1649915861, reconsumeTimes=0, preparedTransactionOffset=0, toString()=Message{topic='melon_dev_test', flag=0, properties={MIN_OFFSET=0, uber-trace-id=7617a5ff2fa5bf68%3A7617a5ff2fa5bf68%3A0%3A0, MAX_OFFSET=2, UNIQ_KEY=0A6F4BA1743E7BA18F1B9F54E2210028, WAIT=true}, body=[104, 101, 108, 108, 111, 32, 98, 97, 98, 121], transactionId='null'}] BODY: hello baby

</code></pre>
<p>字段含义：</p>
<table>
<thead>
<tr>
<th align="left">名称</th>
<th align="left">含义</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">-d</td>
<td align="left">是否打印消息体，默认 false</td>
</tr>
<tr>
<td align="left">-n</td>
<td align="left">NameServer 地址</td>
</tr>
<tr>
<td align="left">-t</td>
<td align="left">主题名称</td>
</tr>
<tr>
<td align="left">-b</td>
<td align="left">开始时间戳，格式为 currentTimeMillis|yyyy-MM-dd#HH:mm:ss:SSS</td>
</tr>
<tr>
<td align="left">-c</td>
<td align="left">字符编码，默认 UTF-8</td>
</tr>
<tr>
<td align="left">-e</td>
<td align="left">结束时间戳，格式为 currentTimeMillis|yyyy-MM-dd#HH:mm:ss:SSS</td>
</tr>
<tr>
<td align="left">-s</td>
<td align="left">订阅的 tag，默认为全部（*），格式 TagA || TagB</td>
</tr>
</tbody>
</table>
<h4><strong>通过 MsgId 检索消息</strong></h4>
<p>通过 queryMsgById 命令检索存储在集群中的消息。</p>
<p>命令示例：</p>
<pre><code>$ bin/mqadmin queryMsgById -n x.x.x.x:9876 -i 0A6F4B5F00002A9F000000138873E059
RocketMQLog:WARN No appenders could be found for logger (io.netty.util.internal.PlatformDependent0).
RocketMQLog:WARN Please initialize the logger system properly.
OffsetID:            0A6F4B5F00002A9F000000138873E059
Topic:               melon_dev_test
Tags:                [null]
Keys:                [null]
Queue ID:            14
Queue Offset:        1
CommitLog Offset:    83893674073
Reconsume Times:     0
Born Timestamp:      2020-07-31 22:32:20,257
Store Timestamp:     2020-07-31 22:32:20,257
Born Host:           x.x.x.x:42806
Store Host:          x.x.x.x:10911
System Flag:         0
Properties:          {uber-trace-id=7617a5ff2fa5bf68%3A7617a5ff2fa5bf68%3A0%3A0, UNIQ_KEY=0A6F4BA1743E7BA18F1B9F54E2210028, WAIT=true}
Message Body Path:   /tmp/rocketmq/msgbodys/0A6F4BA1743E7BA18F1B9F54E2210028

MessageTrack [consumerGroup=melon_dev_consumer, trackType=NOT_ONLINE, exceptionDesc=CODE:206 DESC:the consumer group[melon_dev_consumer] not online]

</code></pre>
<p>字段含义：</p>
<table>
<thead>
<tr>
<th align="left">名称</th>
<th align="left">含义</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">-n</td>
<td align="left">NameServer 地址</td>
</tr>
<tr>
<td align="left">-i</td>
<td align="left">消息 ID</td>
</tr>
<tr>
<td align="left">OffsetID</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Topic</td>
<td align="left">主题名称</td>
</tr>
<tr>
<td align="left">Tags</td>
<td align="left">消息的 TAG</td>
</tr>
<tr>
<td align="left">Keys</td>
<td align="left">发送消息的 key</td>
</tr>
<tr>
<td align="left">Queue ID</td>
<td align="left">消息存储的 Queue</td>
</tr>
<tr>
<td align="left">Queue Offset</td>
<td align="left">消息在 Queue 中的偏移量</td>
</tr>
<tr>
<td align="left">CommitLog Offset</td>
<td align="left">消息在 commitLog 文件中的偏移量</td>
</tr>
<tr>
<td align="left">Reconsume Times</td>
<td align="left">重新消费的次数</td>
</tr>
<tr>
<td align="left">Born Timestamp</td>
<td align="left">消息诞生的时间戳</td>
</tr>
<tr>
<td align="left">Store Timestamp</td>
<td align="left">消息存储的时间戳</td>
</tr>
<tr>
<td align="left">Born Host</td>
<td align="left">发送消息的 IP 地址</td>
</tr>
<tr>
<td align="left">Store Host</td>
<td align="left">消息存储的 IP 地址</td>
</tr>
<tr>
<td align="left">System Flag</td>
<td align="left">标志信息</td>
</tr>
<tr>
<td align="left">Properties</td>
<td align="left">属性信息</td>
</tr>
<tr>
<td align="left">Message Body Path</td>
<td align="left">消息体存储路径</td>
</tr>
<tr>
<td align="left">MessageTrack</td>
<td align="left">消费情况</td>
</tr>
</tbody>
</table>
<h4><strong>通过 Key 检索消息</strong></h4>
<p>可以通过 queryMsgByKey 命令根据消息 Key 检索消息。</p>
<p>命令示例：</p>
<pre><code>$ bin/mqadmin queryMsgByKey -n x.x.x.x:9876 -t melon_dev_test -k orderNo1

RocketMQLog:WARN No appenders could be found for logger (io.netty.util.internal.PlatformDependent0).
RocketMQLog:WARN Please initialize the logger system properly.
#Message ID                                        #QID                                  #Offset
0A6F4BA1743E7BA18F1B022183DA002B                      2                                        0

</code></pre>
<p>字段含义：</p>
<table>
<thead>
<tr>
<th align="left">名称</th>
<th align="left">含义</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">-n</td>
<td align="left">NameServer 地址</td>
</tr>
<tr>
<td align="left">-t</td>
<td align="left">主题名称</td>
</tr>
<tr>
<td align="left">-k</td>
<td align="left">消息 key</td>
</tr>
<tr>
<td align="left">Message ID</td>
<td align="left">消息 ID</td>
</tr>
<tr>
<td align="left">QID</td>
<td align="left">消息存储的 Queue</td>
</tr>
<tr>
<td align="left">Offset</td>
<td align="left">消息在 Queue 的偏移量</td>
</tr>
</tbody>
</table>
<h4><strong>根据 Offset 检索消息</strong></h4>
<p>消息存储在 Broker 中的 queue 中，同样可以通过 offset 来检索消息。</p>
<p>命令示例：</p>
<pre><code>$ bin/mqadmin queryMsgByOffset -n x.x.x.x:9876 -t melon_dev_test -b dev_mq_b -i 2 -o 0
RocketMQLog:WARN No appenders could be found for logger (io.netty.util.internal.PlatformDependent0).
RocketMQLog:WARN Please initialize the logger system properly.
OffsetID:            0A6F4B5F00002A9F00000013A37FED85
Topic:               melon_dev_test
Tags:                [null]
Keys:                [orderNo1]
Queue ID:            2
Queue Offset:        0
CommitLog Offset:    84347448709
Reconsume Times:     0
Born Timestamp:      2020-08-01 09:55:50,874
Store Timestamp:     2020-08-01 09:55:50,875
Born Host:           x.x.x.x:42806
Store Host:          x.x.x.x:10911
System Flag:         0
Properties:          {MIN_OFFSET=0, uber-trace-id=74e72c15f101da93%3A74e72c15f101da93%3A0%3A0, MAX_OFFSET=1, KEYS=orderNo1, UNIQ_KEY=0A6F4BA1743E7BA18F1B022183DA002B, WAIT=true}
Message Body Path:   /tmp/rocketmq/msgbodys/0A6F4BA1743E7BA18F1B022183DA002B

</code></pre>
<p>字段含义：</p>
<table>
<thead>
<tr>
<th align="left">名称</th>
<th align="left">含义</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">-n</td>
<td align="left">NameServer 地址</td>
</tr>
<tr>
<td align="left">-t</td>
<td align="left">主题</td>
</tr>
<tr>
<td align="left">-b</td>
<td align="left">Broker 名字</td>
</tr>
<tr>
<td align="left">-i</td>
<td align="left">Queue ID</td>
</tr>
<tr>
<td align="left">-o</td>
<td align="left">偏移量 offset</td>
</tr>
<tr>
<td align="left">OffsetID</td>
<td align="left">消息 ID</td>
</tr>
<tr>
<td align="left">Topic</td>
<td align="left">主题名称</td>
</tr>
<tr>
<td align="left">Tags</td>
<td align="left">消息的 TAG</td>
</tr>
<tr>
<td align="left">Keys</td>
<td align="left">消息 KEY</td>
</tr>
<tr>
<td align="left">Queue ID</td>
<td align="left">消息存储的 Queue</td>
</tr>
<tr>
<td align="left">Queue Offset</td>
<td align="left">消息在 Queue 中的偏移量</td>
</tr>
<tr>
<td align="left">CommitLog Offset</td>
<td align="left">消息在 commitLog 文件中的偏移量</td>
</tr>
<tr>
<td align="left">Reconsume Times</td>
<td align="left">重新消费的次数</td>
</tr>
<tr>
<td align="left">Born Timestamp</td>
<td align="left">消息诞生的时间戳</td>
</tr>
<tr>
<td align="left">Store Timestamp</td>
<td align="left">消息存储的时间戳</td>
</tr>
<tr>
<td align="left">Born Host</td>
<td align="left">发送消息的 IP 地址</td>
</tr>
<tr>
<td align="left">System Flag</td>
<td align="left">标志信息</td>
</tr>
<tr>
<td align="left">Properties</td>
<td align="left">属性信息</td>
</tr>
<tr>
<td align="left">Message Body Path</td>
<td align="left">消息体存储路径</td>
</tr>
<tr>
<td align="left">MessageTrack</td>
<td align="left">消费情况</td>
</tr>
</tbody>
</table>
<h4><strong>根据 UniqueKey 检索消息</strong></h4>
<p>通过命令 queryMsgByUniqueKey 同样可以检索消息。</p>
<p>命令示例：</p>
<pre><code>$ bin/mqadmin queryMsgByUniqueKey -n dev-mq1.ttbike.com.cn:9876  -t melon_dev_test -i 0A6F4BA1743E7BA18F1B022183DA002B
RocketMQLog:WARN No appenders could be found for logger (io.netty.util.internal.PlatformDependent0).
RocketMQLog:WARN Please initialize the logger system properly.
Topic:               melon_dev_test
Tags:                [null]
Keys:                [orderNo1]
Queue ID:            2
Queue Offset:        0
CommitLog Offset:    84347448709
Reconsume Times:     0
Born Timestamp:      2020-08-01 09:55:50,874
Store Timestamp:     2020-08-01 09:55:50,875
Born Host:           x.x.x.x:42806
Store Host:          x.x.x.x:10911
System Flag:         0
Properties:          {uber-trace-id=74e72c15f101da93%3A74e72c15f101da93%3A0%3A0, KEYS=orderNo1, UNIQ_KEY=0A6F4BA1743E7BA18F1B022183DA002B, WAIT=true}
Message Body Path:   /tmp/rocketmq/msgbodys/0A6F4BA1743E7BA18F1B022183DA002B

</code></pre>
<p>字段含义：</p>
<p>字段含义同上面命令。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="14&#32;消息消费积压问题排查实战.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="16&#32;RocketMQ&#32;集群性能摸高.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script data-cfasync="false" src="../../cdn-cgi/scripts/5c5dd728/cloudflare-static/email-decode.min.js"></script><script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b434afebac570ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
