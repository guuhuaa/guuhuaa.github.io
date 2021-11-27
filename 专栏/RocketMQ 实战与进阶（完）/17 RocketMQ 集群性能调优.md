<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>17 RocketMQ 集群性能调优.md</title>
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

                    <a class="current-tab" href="17&#32;RocketMQ&#32;集群性能调优.md">17 RocketMQ 集群性能调优.md</a>
                    

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
                        <div><h1>17 RocketMQ 集群性能调优</h1>
<h3>前言</h3>
<p>本篇从系统参数和集群参数两个维度对 RocketMQ 集群进行优化，目的在于 RocketMQ 运行的更平稳。平稳往往比单纯提高 TPS 更重要，文中基于实际生产环境运行情况给出，另外在后面文章中会介绍由于参数设置而引发集群不稳定，业务受到影响的踩坑案例。</p>
<h3>系统参数调优</h3>
<p>在解压 RocketMQ 安装包后，在 bin 目录中有个 os.sh 的文件，该文件由 RocketMQ 官方推荐系统参数配置。通常这些参数可以满足系统需求，也可以根据情况进行调整。需要强调的是不要使用 Linux 内核版本 2.6 及以下版本，建议使用 Linux 内核版本在 3.10 及以上，如果使用 CentOS，可以选择 CentOS 7 及以上版本。选择 Linux 内核版本 2.6 出现的问题会在后面踩坑案例中提到。</p>
<h4><strong>最大文件数</strong></h4>
<p>设置用户的打开的最多文件数：</p>
<pre><code>vim /etc/security/limits.conf
# End of file
baseuser soft nofile 655360
baseuser hard nofile 655360
* soft nofile 655360
* hard nofile 655360

</code></pre>
<h4><strong>系统参数设置</strong></h4>
<p>系统参数的调整以官方给出的为主，下面对各个参数做个说明。设置时可以直接执行 <code>sh os.sh</code> 完成系统参数设定，也可以编辑 <code>vim /etc/sysctl.conf</code> 文件手动添加如下内容，添加后执行 <code>sysctl -p</code> 让其生效。</p>
<pre><code>vm.overcommit_memory=1
vm.drop_caches=1
vm.zone_reclaim_mode=0
vm.max_map_count=655360
vm.dirty_background_ratio=50
vm.dirty_ratio=50
vm.dirty_writeback_centisecs=360000
vm.page-cluster=3
vm.swappiness=1

</code></pre>
<p>参数说明：</p>
<table>
<thead>
<tr>
<th align="left">参数</th>
<th align="left">含义</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">overcommit_memory</td>
<td align="left">是否允许内存的过量分配 overcommit_memory=0 当用户申请内存的时候，内核会去检查是否有这么大的内存空间 overcommit_memory=1 内核始终认为，有足够大的内存空间，直到它用完了为止 overcommit_memory=2 内核禁止任何形式的过量分配内存</td>
</tr>
<tr>
<td align="left">drop_caches</td>
<td align="left">写入的时候，内核会清空缓存，腾出内存来，相当于 sync drop_caches=1 会清空页缓存，就是文件 drop_caches=2 会清空 inode 和目录树 drop_caches=3 都清空</td>
</tr>
<tr>
<td align="left">zone_reclaim_mode</td>
<td align="left">zone_reclaim_mode=0 系统会倾向于从其他节点分配内存 zone_reclaim_mode=1 系统会倾向于从本地节点回收 Cache 内存</td>
</tr>
<tr>
<td align="left">max_map_count</td>
<td align="left">定义了一个进程能拥有的最多的内存区域，默认为 65536</td>
</tr>
<tr>
<td align="left">dirty_background_ratio/dirty_ratio</td>
<td align="left">当 dirty cache 到了多少的时候，就启动 pdflush 进程，将 dirty cache 写回磁盘 当有 dirty_background_bytes/dirty_bytes 存在的时候，dirty_background_ratio/dirty_ratio 是被自动计算的</td>
</tr>
<tr>
<td align="left">dirty_writeback_centisecs</td>
<td align="left">pdflush 每隔多久，自动运行一次（单位是百分之一秒）</td>
</tr>
<tr>
<td align="left">page-cluster</td>
<td align="left">每次 swap in 或者 swap out 操作多少内存页为 2 的指数 page-cluster=0 表示 1 页 page-cluster=1 表示 2 页 page-cluster=2 表示 4 页 page-cluster=3 表示 8 页</td>
</tr>
<tr>
<td align="left">swappiness</td>
<td align="left">swappiness=0 仅在内存不足的情况下，当剩余空闲内存低于 vm.min_free_kbytes limit 时，使用交换空间 swappiness=1 内核版本 3.5 及以上、Red Hat 内核版本 2.6.32-303 及以上，进行最少量的交换，而不禁用交换 swappiness=10 当系统存在足够内存时，推荐设置为该值以提高性能 swappiness=60 默认值 swappiness=100 内核将积极的使用交换空间</td>
</tr>
</tbody>
</table>
<h3>集群参数调优</h3>
<h4><strong>生产环境配置</strong></h4>
<p>下面列出一份在生产环境使用的配置文件，并说明其参数所表示的含义，只需要稍加修改集群名称即可作为生产环境啊配置使用。</p>
<p>配置示例：</p>
<pre><code>brokerClusterName=testClusterA
brokerName=broker-a
brokerId=0
listenPort=10911
namesrvAddr=x.x.x.x:9876;x.x.x.x::9876
defaultTopicQueueNums=16
autoCreateTopicEnable=false
autoCreateSubscriptionGroup=false
deleteWhen=04
fileReservedTime=48
mapedFileSizeCommitLog=1073741824
mapedFileSizeConsumeQueue=50000000
destroyMapedFileIntervalForcibly=120000
redeleteHangedFileInterval=120000
diskMaxUsedSpaceRatio=88
storePathRootDir=/data/rocketmq/store
storePathCommitLog=/data/rocketmq/store/commitlog
storePathConsumeQueue=/data/rocketmq/store/consumequeue
storePathIndex=/data/rocketmq/store/index
storeCheckpoint=/data/rocketmq/store/checkpoint
abortFile=/data/rocketmq/store/abort
maxMessageSize=65536
flushCommitLogLeastPages=4
flushConsumeQueueLeastPages=2
flushCommitLogThoroughInterval=10000
flushConsumeQueueThoroughInterval=60000
brokerRole=ASYNC_MASTER
flushDiskType=ASYNC_FLUSH
maxTransferCountOnMessageInMemory=1000
transientStorePoolEnable=false
warmMapedFileEnable=false
pullMessageThreadPoolNums=128
slaveReadEnable=true
transferMsgByHeap=true
waitTimeMillsInSendQueue=1000

</code></pre>
<p>参数说明：</p>
<table>
<thead>
<tr>
<th align="left">参数</th>
<th align="left">含义</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">brokerClusterName</td>
<td align="left">集群名称</td>
</tr>
<tr>
<td align="left">brokerName</td>
<td align="left">broker 名称</td>
</tr>
<tr>
<td align="left">brokerId</td>
<td align="left">0 表示 Master 节点</td>
</tr>
<tr>
<td align="left">listenPort</td>
<td align="left">broker 监听端口</td>
</tr>
<tr>
<td align="left">namesrvAddr</td>
<td align="left">namesrvAddr 地址</td>
</tr>
<tr>
<td align="left">defaultTopicQueueNums</td>
<td align="left">创建 Topic 时默认的队列数量</td>
</tr>
<tr>
<td align="left">autoCreateTopicEnable</td>
<td align="left">是否允许自动创建主题，生产环境建议关闭，非生产环境可以开启</td>
</tr>
<tr>
<td align="left">autoCreateSubscriptionGroup</td>
<td align="left">是否允许自动创建消费组，生产环境建议关闭，非生产环境可以开启</td>
</tr>
<tr>
<td align="left">deleteWhen</td>
<td align="left">清理过期日志时间，04 表示凌晨 4 点开始清理</td>
</tr>
<tr>
<td align="left">fileReservedTime</td>
<td align="left">日志保留的时间单位小时，48 即 48 小时，保留 2 天</td>
</tr>
<tr>
<td align="left">mapedFileSizeCommitLog</td>
<td align="left">日志文件大小</td>
</tr>
<tr>
<td align="left">mapedFileSizeConsumeQueue</td>
<td align="left">ConsumeQueue 文件大小</td>
</tr>
<tr>
<td align="left">destroyMapedFileIntervalForcibly</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">redeleteHangedFileInterval</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">diskMaxUsedSpaceRatio</td>
<td align="left">磁盘最大使用率，超过使用率会发起日志清理操作</td>
</tr>
<tr>
<td align="left">storePathRootDir</td>
<td align="left">RocketMQ 日志等数据存储的根目录</td>
</tr>
<tr>
<td align="left">storePathCommitLog</td>
<td align="left">CommitLog 存储目录</td>
</tr>
<tr>
<td align="left">storePathConsumeQueue</td>
<td align="left">ConsumeQueue 存储目录</td>
</tr>
<tr>
<td align="left">storePathIndex</td>
<td align="left">索引文件存储目录</td>
</tr>
<tr>
<td align="left">storeCheckpoint</td>
<td align="left">checkpoint 文件存储目录</td>
</tr>
<tr>
<td align="left">abortFile</td>
<td align="left">abort 文件存储目录</td>
</tr>
<tr>
<td align="left">maxMessageSize</td>
<td align="left">单条消息允许的最大字节</td>
</tr>
<tr>
<td align="left">flushCommitLogLeastPages</td>
<td align="left">未 flush 的消息大小超过设置页时，才执行 flush 操作；一页大小为 4K</td>
</tr>
<tr>
<td align="left">flushConsumeQueueLeastPages</td>
<td align="left">未 flush 的消费队列大小超过设置页时，才执行 flush 操作；一页大小为 4K</td>
</tr>
<tr>
<td align="left">flushCommitLogThoroughInterval</td>
<td align="left">两次执行消息 flush 操作的间隔时间，默认为 10 秒</td>
</tr>
<tr>
<td align="left">flushConsumeQueueThoroughInterval</td>
<td align="left">两次执行消息队列 flush 操作的间隔时间，默认为 60 秒</td>
</tr>
<tr>
<td align="left">brokerRole</td>
<td align="left">broker 角色 ASYNC_MASTER 异步复制的 Master 节点 SYNC_MASTER 同步复制的 Master 节点 SLAVE 从节点</td>
</tr>
<tr>
<td align="left">flushDiskType</td>
<td align="left">刷盘类型 ASYNC_FLUSH 异步刷盘 SYNC_FLUSH 同步刷盘</td>
</tr>
<tr>
<td align="left">maxTransferCountOnMessageInMemory</td>
<td align="left">消费时允许一次拉取的最大消息数</td>
</tr>
<tr>
<td align="left">transientStorePoolEnable</td>
<td align="left">是否开启堆外内存传输</td>
</tr>
<tr>
<td align="left">warmMapedFileEnable</td>
<td align="left">是否开启文件预热</td>
</tr>
<tr>
<td align="left">pullMessageThreadPoolNums</td>
<td align="left">拉取消息线程池大小</td>
</tr>
<tr>
<td align="left">slaveReadEnable</td>
<td align="left">是否开启允许从 Slave 节点读取消息 内存的消息大小占物理内存的比率，当超过默认 40%会从 slave 的 0 节点读取 通过 accessMessageInMemoryMaxRatio 设置内存的消息大小占物理内存的比率</td>
</tr>
<tr>
<td align="left">transferMsgByHeap</td>
<td align="left">消息消费时是否从堆内存读取</td>
</tr>
<tr>
<td align="left">waitTimeMillsInSendQueue</td>
<td align="left">发送消息时在队列中等待时间，超过会抛出超时错误</td>
</tr>
</tbody>
</table>
<h4><strong>调优建议</strong></h4>
<p>对 Broker 的几个属性可能影响到集群性能的稳定性，下面进行特别说明。</p>
<p><strong>1. 开启异步刷盘</strong></p>
<p>除了一些支付类场景、或者 TPS 较低的场景（例如：TPS 在 2000 以下）生产环境建议开启异步刷盘，提高集群吞吐。</p>
<pre><code>flushDiskType=ASYNC_FLUSH

</code></pre>
<p><strong>2. 开启 Slave 读权限</strong></p>
<p>消息占用物理内存的大小通过 accessMessageInMemoryMaxRatio 来配置默认为 40%；如果消费的消息不在内存中，开启 slaveReadEnable 时会从 slave 节点读取；提高 Master 内存利用率。</p>
<pre><code>slaveReadEnable=true

</code></pre>
<p><strong>3. 消费一次拉取消息数量</strong></p>
<p>消费时一次拉取的数量由 broker 和 consumer 客户端共同决定，默认为 32 条。Broker 端参数由 maxTransferCountOnMessageInMemory 设置。consumer 端由 pullBatchSize 设置。Broker 端建议设置大一些，例如 1000，给 consumer 端留有较大的调整空间。</p>
<pre><code>maxTransferCountOnMessageInMemory=1000

</code></pre>
<p><strong>4. 发送队列等待时间</strong></p>
<p>消息发送到 Broker 端，在队列的等待时间由参数 waitTimeMillsInSendQueue 设置，默认为 200ms。建议设置大一些，例如：1000ms~5000ms。设置过短，发送客户端会引起超时。</p>
<pre><code>waitTimeMillsInSendQueue=1000

</code></pre>
<p><strong>5. 主从异步复制</strong></p>
<p>为提高集群性能，在生成环境建议设置为主从异步复制，经过压力测试主从同步复制性能过低。</p>
<pre><code>brokerRole=ASYNC_MASTER

</code></pre>
<p><strong>6. 提高集群稳定性</strong></p>
<p>为了提高集群稳定性，对下面三个参数进行特别说明，在后面踩坑案例中也会提到。</p>
<p>关闭堆外内存：</p>
<pre><code>transientStorePoolEnable=false

</code></pre>
<p>关闭文件预热：</p>
<pre><code>warmMapedFileEnable=false

</code></pre>
<p>开启堆内传输：</p>
<pre><code>transferMsgByHeap=true
</code></pre>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="16&#32;RocketMQ&#32;集群性能摸高.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="18&#32;RocketMQ&#32;集群平滑运维.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b434b0e88f370ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
