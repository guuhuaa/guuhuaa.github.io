<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>05 基于 Redis 的分布式缓存实现及加固策略.md</title>
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

                    <a class="current-tab" href="05&#32;基于&#32;Redis&#32;的分布式缓存实现及加固策略.md">05 基于 Redis 的分布式缓存实现及加固策略.md</a>
                    

                </li>
                <li>

                    
                    <a href="06&#32;Redis&#32;实际应用中的异常场景及其根因分析和解决方案.md">06 Redis 实际应用中的异常场景及其根因分析和解决方案.md</a>

                </li>
                <li>

                    
                    <a href="07&#32;Redis-Cluster&#32;故障倒换调优原理分析.md">07 Redis-Cluster 故障倒换调优原理分析.md</a>

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
                        <div><h1>05 基于 Redis 的分布式缓存实现及加固策略</h1>
<p>本文将从 Redis-Cluster 搭建切入，详解集群的创建原理和加固策略。之后，分析集群所存在的几种可靠性问题并给出解决方案，最后，介绍一个集群运维软件的实现方案。</p>
<h3>1. Redis-Cluster 搭建</h3>
<p>本节将介绍基于 Redis 和 Lettuce 搭建一个分布式缓存集群的方法。为了生动地呈现集群创建过程，我没有采用 Redis 集群管理工具 redis-trib，而是基于 Lettuce 编写 Java 代码实现集群的创建，相信，这将有利于读者更加深刻地理解 Redis 集群模式。</p>
<h4>1.1 方案简述</h4>
<p>Redis 集群模式至少需要三个主节点，作为举例，本文搭建一个3主3备的精简集群，麻雀虽小，五脏俱全。主备关系如下图所示，其中 M 代表 Master 节点，S 代表 Slave 节点，A-M 和 A-S 为一对主备节点。</p>
<p><img src="assets/a43e6950-966f-11e8-9f67-05ec09da262a" alt="enter image description here" /></p>
<p>按照上图所示的拓扑结构，如果节点 1 故障下线，那么节点 2 上的 A-S 将升主为 A-M，Redis 3 节点集群仍可用，如下图所示：</p>
<p><img src="assets/b04af9c0-966f-11e8-bee3-b1dbef72ca56" alt="enter image description here" /></p>
<p>特别说明：事实上，Redis 集群节点间是两两互通的，如下图所示，上面作为示意图，进行了适当简化。</p>
<p><img src="assets/c06bb2e0-966f-11e8-9c35-b59aad3fef8b" alt="enter image description here" /></p>
<h4>1.2 资源准备</h4>
<p>首先，下载 Redis 包。前往 Redis 官网下载 Redis 资源包，本文采用的 Redis 版本为 4.0.8。</p>
<p>接着，将下载的 Redis 资源包 <code>redis-4.0.8.tar.gz</code> 放到自定义目录下，解压，编译便可生成 Redis 服务端和本地客户端 bin 文件 <code>redis-server</code> 和 <code>redis-cli</code>，具体操作命令如下：</p>
<pre><code>tar xzf redis-4.0.8.tar.gz
cd redis-4.0.8
make

</code></pre>
<p>最后，编译完成，在 src 目录下可以看到生成的 bin 文件 <code>redis-server</code> 和 <code>redis-cli</code>。</p>
<h4>1.3 集群配置</h4>
<p>写作本文时，手头只有一台机器，无法搭建物理层面的 3 节点集群，限于条件，我在同一台机器上创建 6 个 Redis 实例，构建 3 主 3 备精简集群。</p>
<h5><strong>（1） 创建目录</strong></h5>
<p>根据端口号分别创建名为 6379、6380、6381、6382、6383、6384 的文件夹。</p>
<h5><strong>（2）修改配置文件</strong></h5>
<p>在解压文件夹 <code>redis-4.0.8</code> 中有一个 Redis 配置文件 <code>redis.conf</code>，其中一些默认的配置项需要修改（配置项较多，本文仅为举例，修改一些必要的配置）。以下仅以 6379 端口为例进行配置，6380、6381等端口配置操作类似。将修改后的配置文件分别放入 6379~6384 文件夹中。</p>
<p><img src="assets/3bd42b30-cd23-11e8-8e49-d7b1f250ebf6" alt="enter image description here" /></p>
<h5><strong>（3）创建必要启停脚本</strong></h5>
<p>逐一手动拉起 Redis 进程较为麻烦，在此，我们可以编写简单的启停脚本完成 <code>redis-server</code> 进程的启停（<code>start.sh</code> 和 <code>stop.sh</code>）。</p>
<p><img src="assets/120e9810-9670-11e8-bee3-b1dbef72ca56" alt="enter image description here" /></p>
<h5><strong>（4）简单测试</strong></h5>
<p>至此，我们已经完成 Redis 集群创建的前期准备工作，在创建集群之前，我们可以简单测试一下，<code>redis-sever</code> 进程是否可以正常拉起。运行 <code>start.sh</code> 脚本，查看 <code>redis-server</code> 进程如下：</p>
<p><img src="assets/1b0eabd0-9670-11e8-9c35-b59aad3fef8b" alt="enter image description here" /></p>
<p>登录其中一个 Redis 实例的客户端（以 6379 为例），查看集群状态：很明显，以节点 6379 的视角来看，集群处于 Fail 状态，<code>clusterknownnodes:1</code> 表示集群中只有一个节点。</p>
<p><img src="assets/23e45430-9670-11e8-9c35-b59aad3fef8b" alt="enter image description here" /></p>
<h3>2. 基于 Lettuce 创建 Redis 集群</h3>
<blockquote>
<p>关于创建 Redis 集群，官方提供了一个 Ruby 编写的运维软件 <code>redis-trib.rb</code>，使用简单的命令便可以完成创建集群、添加节点、负载均衡等操作。正因为简单，用户很难通过黑盒表现理解其中细节，鉴于此，本节将基于 Lettuce 编写创建 Redis 集群的代码，让读者对 Redis 集群创建有一个更深入的理解。</p>
</blockquote>
<p>Redis 发展至今，其对应的开源客户端几乎涵盖所有语言，详情请见官网，本节采用 Java 语言开发的 Lettuce 作为 Redis 客户端。Lettuce 是一个可伸缩线程安全的 Redis 客户端，多个线程可以共享同一个 RedisConnection。它采用优秀 Netty NIO 框架来高效地管理多个连接。关于 Lettuce 的详情，后面章节中会详细介绍。</p>
<p><img src="assets/49ae3fa0-9670-11e8-bee3-b1dbef72ca56" alt="enter image description here" /></p>
<h4>2.1 Redis 集群创建的步骤</h4>
<h5><strong>（1）相互感知，初步形成集群。</strong></h5>
<p>在上文中，我们已经成功拉起了 6 个 <code>redis-server</code> 进程，每个进程视为一个节点，这些节点仍处于孤立状态，它们相互之间无法感知对方的存在，既然要创建集群，首先需要让这些孤立的节点相互感知，形成一个集群。</p>
<h5><strong>（2）分配 Slot 给期望的主节点。</strong></h5>
<p>形成集群之后，仍然无法提供服务，Redis 集群模式下，数据存储于 16384 个 Slot 中，我们需要将这些 Slot 指派给期望的主节点。何为期望呢？我们有 6 个节点，3 主 3 备，我们只能将 Slot 指派给 3 个主节点，至于哪些节点为主节点，我们可以自定义。</p>
<h5><strong>（3）设置从节点。</strong></h5>
<p>Slot 分配完成后，被分配 Slot 的节点将成为真正可用的主节点，剩下的没有分到 Slot 的节点，即便状态标志为 Master，实际上也不能提供服务。接下来，出于可靠性的考量，我们需要将这些没有被指派 Slot 的节点指定为可用主节点的从节点（Slave）。</p>
<p>经过上述三个步骤，一个精简的 3 主 3 备 Redis 集群就搭建完成了。</p>
<h4>2.2 基于 Lettuce 创建集群代码</h4>
<p>根据上述步骤，基于 Lettuce 创建集群的代码如下（仅供入门参考）：</p>
<pre><code>import java.util.ArrayList;
import java.util.List;

import io.lettuce.core.RedisClient;
import io.lettuce.core.RedisCommandTimeoutException;
import io.lettuce.core.RedisConnectionException;
import io.lettuce.core.RedisException;
import io.lettuce.core.RedisURI;
import io.lettuce.core.api.StatefulRedisConnection;

public class CreateCluster
{

    public static void main(String[] args) throws InterruptedException
    {
        createCluster();
    }

    private static void createCluster() throws InterruptedException
    {
        // 初始化集群节点列表，并指定主节点列表和从节点列表
        List&lt;ClusterNode&gt; clusterNodeList = new ArrayList&lt;ClusterNode&gt;();
        List&lt;ClusterNode&gt; masterNodeList = new ArrayList&lt;ClusterNode&gt;();
        List&lt;ClusterNode&gt; slaveNodeList = new ArrayList&lt;ClusterNode&gt;();
        String[] endpoints = {&quot;127.0.0.1:6379&quot;,&quot;127.0.0.1:6380&quot;,&quot;127.0.0.1:6381&quot;
                ,&quot;127.0.0.1:6382&quot;,&quot;127.0.0.1:6383&quot;,&quot;127.0.0.1:6384&quot;};
        int index = 0;
        for (String endpoint : endpoints)
        {
            String[] ipAndPort = endpoint.split(&quot;:&quot;);
            ClusterNode node = new ClusterNode(ipAndPort[0], Integer.parseInt(ipAndPort[1]));
            clusterNodeList.add(node);
            // 将6379，6380，6381设置为主节点，其余为从节点
            if (index &lt; 3)
            {
                masterNodeList.add(node);
            }
            else
            {
                slaveNodeList.add(node);
            }
            index++;
        }       
        // 分别与各个Redis节点建立通信连接
        for (ClusterNode node : clusterNodeList)
        {
            RedisURI redisUri = RedisURI.Builder.redis(node.getHost(), node.getPort()).build();
            RedisClient redisClient = RedisClient.create(redisUri);
            try
            {
                StatefulRedisConnection&lt;String, String&gt; connection = redisClient.connect();
                node.setConnection(connection);
            } catch (RedisException e)
            {
                System.out.println(&quot;connection failed--&gt;&quot; + node.getHost() + &quot;:&quot; + node.getPort());
            }
        }   

        // 执行cluster meet命令是各个孤立的节点相互感知，初步形成集群。
        // 只需以一个节点为基准，让所有节点与之meet即可
        ClusterNode firstNode = null;
        for (ClusterNode node : clusterNodeList)
        {
            if (firstNode == null)
            {
                firstNode = node;
            } 
            else
            {
                try
                {
                    node.getConnection().sync().clusterMeet(firstNode.getHost(), firstNode.getPort());
                } 
                catch (RedisCommandTimeoutException | RedisConnectionException e)
                {
                    System.out.println(&quot;meet failed--&gt;&quot; + node.getHost() + &quot;:&quot; + node.getPort());
                } 
            }
        }
        // 为主节点指派slot,将16384个slot分成三份：5461，5461，5462
        int[] slots = {0,5460,5461,10921,10922,16383};
        index = 0;
        for (ClusterNode node : masterNodeList)
        {
            node.setSlotsBegin(slots[index]);
            index++;
            node.setSlotsEnd(slots[index]);
            index++;
        }
        // 通过与各个主节点的连接，执行addSlots命令为主节点指派slot
        System.out.println(&quot;Start to set slots...&quot;);
        for (ClusterNode node : masterNodeList)
        {
            try
            {
                node.getConnection().sync().clusterAddSlots(createSlots(node.getSlotsBegin(), node.getSlotsEnd()));
            } 
            catch (RedisCommandTimeoutException | RedisConnectionException e)
            {
                System.out.println(&quot;add slots failed--&gt;&quot; + node.getHost() + &quot;:&quot; + node.getPort());
            }
        }
        // 延时5s，等待slot指派完成
        sleep(5000);
        // 为已经指派slot的主节点设置从节点,6379,6380,6381分别对应6382，6383，6384
        index = 0;
        for (ClusterNode node : slaveNodeList)
        {
            try
            {       
                node.getConnection().sync().clusterReplicate(masterNodeList.get(index).getMyId());      
            } 
            catch (RedisCommandTimeoutException | RedisConnectionException e)
            {
                System.out.println(&quot;replicate failed--&gt;&quot; + node.getHost() + &quot;:&quot; + node.getPort());
            } 
        }
        // 关闭连接,销毁客户端，释放资源
        for (ClusterNode node : clusterNodeList)
        {
            node.getConnection().close();
            node.getClient().shutdown();
        }
    }

    public static int[] createSlots(int from, int to)
    {
        int[] result = new int[to - from + 1];
        int counter = 0;
        for (int i = from; i &lt;= to; i++) 
        {
            result[counter++] = i;
        }
        return result;
    }

}
/*
 * 定义集群节点描述类
 */
class ClusterNode
{
    private String host;
    private int port;
    private int slotsBegin;
    private int slotsEnd;
    private String myId;
    private String masterId;
    private StatefulRedisConnection&lt;String, String&gt; connection;
    private RedisClient redisClient;

    public ClusterNode(String host, int port)
    {
        this.host = host;
        this.port = port;
        this.slotsBegin = 0;
        this.slotsEnd = 0;
        this.myId = null;
        this.masterId = null;
    }

    public String getHost()
    {
        return host;
    }

    public int getPort()
    {
        return port;
    }

    public void setMaster(String masterId)
    {
        this.masterId = masterId;
    }

    public String getMaster()
    {
        return masterId;
    }

    public void setMyId(String myId)
    {
        this.myId = myId;
    }

    public String getMyId()
    {
        return myId;
    }

    public void setSlotsBegin(int first)
    {
        this.slotsBegin = first;
    }

    public void setSlotsEnd(int last)
    {
        this.slotsEnd = last;
    }

    public int getSlotsBegin()
    {
        return slotsBegin;
    }

    public int getSlotsEnd()
    {
        return slotsEnd;
    }

    public void setConnection(StatefulRedisConnection&lt;String, String&gt; connection)
    {
        this.connection = connection;
    }

    public void setClient(RedisClient client)
    {
        this.redisClient = client;
    }

    public StatefulRedisConnection&lt;String, String&gt; getConnection()
    {
        return connection;
    }

    public RedisClient getClient()
    {
        return redisClient;
    }

}

</code></pre>
<p>运行上述代码创建集群，再次登录其中一个节点的客户端（以 6379 为例），通过命令：<code>cluster nodes</code>、<code>cluster info</code> 查看集群状态信息如下，集群已经处于可用状态。</p>
<p><img src="assets/614c8b30-9670-11e8-bd60-15398afc36e1" alt="enter image description here" /></p>
<h4>2.3 测试验证</h4>
<p>经过上述步骤，一个可用的 Redis 集群已经创建完毕，接下来，通过一段代码测试验证：</p>
<pre><code>public static void main(String[] args)
    {
        List&lt;ClusterNode&gt; clusterNodeList = new ArrayList&lt;ClusterNode&gt;();
        List&lt;RedisURI&gt; redisUriList = new ArrayList&lt;RedisURI&gt;();
        String[] endpoints = {&quot;127.0.0.1:6379&quot;,&quot;127.0.0.1:6380&quot;,&quot;127.0.0.1:6381&quot;
                ,&quot;127.0.0.1:6382&quot;,&quot;127.0.0.1:6383&quot;,&quot;127.0.0.1:6384&quot;};
        for (String endpoint : endpoints)
        {
            String[] ipAndPort = endpoint.split(&quot;:&quot;);
            ClusterNode node = new ClusterNode(ipAndPort[0], Integer.parseInt(ipAndPort[1]));
            clusterNodeList.add(node);
        }       
        //创建RedisURI
        for (ClusterNode node : clusterNodeList)
        {
            RedisURI redisUri = RedisURI.Builder.redis(node.getHost(), node.getPort()).build();
            redisUriList.add(redisUri);
        }   
        //创建Redis集群客户端，建立连接，执行set，get基本操作
        RedisClusterClient redisClusterClient = RedisClusterClient.create(redisUriList);
        StatefulRedisClusterConnection&lt;String, String&gt; conn = redisClusterClient.connect();
        RedisAdvancedClusterCommands&lt;String, String&gt; cmd = null;
        cmd = conn.sync();
        System.out.println(cmd.set(&quot;key-test&quot;, &quot;value-test&quot;));
        System.out.println(cmd.get(&quot;key-test&quot;));
        //关闭连接
        cmd.close();
        conn.close();
        redisClusterClient.shutdown();      
    }

</code></pre>
<p>测试结果如下：</p>
<blockquote>
<p>OK；</p>
<p>value-test</p>
</blockquote>
<h3>3. Redis SSL 双向认证通信实现</h3>
<h4>3.1 Redis 自带的鉴权访问模式</h4>
<p>默认情况下，Redis 服务端是不允许远程访问的，打开其配置文件 <code>redis.conf</code>，可以看到如下配置：</p>
<p><img src="assets/9b307d70-9670-11e8-bd60-15398afc36e1" alt="enter image description here" /></p>
<p>根据说明，如果我们要远程访问，可以手动改变 <code>protected-mode</code> 配置，将 yes 状态置为 no 即可，也可在本地客服端 <code>redis-cli</code>，键入命令：<code>config set protected-mode no</code>。但是，这明显不是一个好的方法，去除保护机制，意味着严重安全风险。</p>
<p>鉴于此，我们可以采用鉴权机制，通过秘钥来鉴权访问，修改 <code>redis.conf</code>，添加 <code>requirepass mypassword</code> ，或者键入命令：<code>config set requirepass password</code> 设置鉴权密码。</p>
<p><img src="assets/a9e1a100-9670-11e8-bee3-b1dbef72ca56" alt="enter image description here" /></p>
<p>设置密码后，Lettuce 客户端访问 <code>redis-server</code> 就需要鉴权，增加一行代码即可，以单机模式为例：</p>
<p><img src="assets/bb32eae0-9670-11e8-9f67-05ec09da262a" alt="enter image description here" /></p>
<h5><strong>补充</strong></h5>
<p>除了通过密码鉴权访问，出于安全的考量，Redis 还提供了一些其它的策略：</p>
<ul>
<li>禁止高危命令</li>
</ul>
<p>修改 <code>redis.conf</code> 文件，添加如下配置，将高危原生命令重命名为自定义字符串：</p>
<pre><code>rename-command FLUSHALL &quot;user-defined&quot;
rename-command CONFIG   &quot;user-defined&quot;
rename-command EVAL     &quot;user-defined&quot;

</code></pre>
<p>虽然禁止高危命令有助于安全，但本质上只是一种妥协，也许是对加密鉴权信心不足吧。</p>
<ul>
<li>禁止外网访问</li>
</ul>
<p>Redis 配置文件 <code>redis.conf</code> 默认绑定本机地址，即 Redis 服务只在当前主机可用，配置如下：</p>
<pre><code>bind 127.0.0.1

</code></pre>
<p>这种方式，基本斩断了被远程攻击的可能性，但局限性更明显，Redis 基本退化成本地缓存了。</p>
<h4>3.2 SSL 双向认证通信</h4>
<p>通过上面的介绍，相信读者已经对 Redis 自带的加固策略有了一定了解。客观地讲，Redis 自带的安全策略很难满足对安全性要求普遍较高的商用场景，鉴于此，有必要优化。就 <code>Client-Server</code> 模式而言，成熟的安全策略有很多，本文仅介绍其一：SSL 双向认证通信。关于 SSL 双向认证通信的原理和具体实现方式，网上有大量的博文可供参考，并非本文重点，因此不做详细介绍。</p>
<h5><strong>总体流程</strong></h5>
<p>我们首先看下 SSL 双向认证通信的总体流程，如下图所示:</p>
<p><img src="assets/f1d17620-9670-11e8-bd60-15398afc36e1" alt="enter image description here" /></p>
<p>首先，Client 需要将 Server 的根证书 <code>ca.crt</code> 安装到自己的信任证书库中；同时，Server 也需要将根证书 <code>ca.crt</code> 安装到自己的信任证书库中。</p>
<p>接着，当 SSL 握手时，Server 先将服务器证书 <code>server.p12</code> 发给 Client，Client 收到后，到自己的信任证书库中进行验证，由于 <code>server.p12</code> 是根证书 CA 颁发的，所以验证必然通过。</p>
<p>然后，Client 将客户端证书 <code>client.p12</code> 发给 Server，同理， <code>client.p12</code> 是根证书 CA 颁发的，所以验证也将通过。</p>
<p>需要注意的是，从证书库中取证书需要提供密码，这个密码需保存到服务端和客户端的配置文件中。如果以明文形式保存，存在安全风险，因此，通常会对明文密码进行加密，配置文件中保存加密后的密文。然后，客户端和服务端对应的鉴权程序首先对密文解密获得证书库明文密码，再从证书库中取得证书。</p>
<h5><strong>实现方案</strong></h5>
<p>我们从服务端、客户端三个方面看下 SSL 双向认证通信的实现方案。</p>
<ul>
<li>服务端</li>
</ul>
<p>Redis 本身不支持 SSL 双向认证通信，因此，需要修改源码，且涉及修改较多，本文仅列出要点，具体实现层面代码不列。</p>
<p><strong>config.c</strong></p>
<p>SSL 双向认证通信涉及的 keyStore 和 trustStore 密码密文、路径等信息可由 Redis 的配置文件 <code>redis.conf</code> 提供，如此，我们需要修改加载配置文件的源码（config.c-&gt;loadServerConfigFromString(char *config)），部分修改如下：</p>
<p><img src="assets/03a25040-9671-11e8-9c35-b59aad3fef8b" alt="enter image description here" /></p>
<p><strong>redis.h</strong></p>
<p>Redis 的客户端（redisClient）和服务端（redisServer）都需要适配，部分代码如下：</p>
<p><img src="assets/0bb767c0-9671-11e8-9f67-05ec09da262a" alt="enter image description here" /></p>
<p><img src="assets/19777490-9671-11e8-bd60-15398afc36e1" alt="enter image description here" /></p>
<p><strong>hiredis.h</strong></p>
<p>修改创建连接的原函数：</p>
<p><img src="assets/28862170-9671-11e8-9f67-05ec09da262a" alt="enter image description here" /></p>
<p><strong>anet.h</strong></p>
<p>定义 SSL 通信涉及的一些函数（实现在 anet.c 中）：</p>
<p><img src="assets/2e74d680-9671-11e8-9c35-b59aad3fef8b" alt="enter image description here" /></p>
<ul>
<li>客户端</li>
</ul>
<p>Lettuce 支持 SSL 双向认证通信，需要增加一些代码，以单机模式为例：</p>
<pre><code>// 获取trustStore的密码的密文
String trustPd = System.getProperty(&quot;redis_trustStore_password&quot;);
// 对密码的密文进行解密获得明文密码，解密算法很多，这里是自研代码
trustPd = CipherMgr.decrypt(trustPd);

// 获取keyStore的密码的密文
String keyPd = System.getProperty(&quot;redis_keyStore_password&quot;);
// 对密码的密文进行解密获得明文密码
keyPd = CipherMgr.decrypt(keyPd);

// 加密算法套件，此处client_cipher=TLS_RSA_WITH_AES_128_GCM_SHA256
List&lt;String&gt; cipherList = new ArrayList&lt;String&gt;();
cipherList.add(System.getProperty(&quot;client_cipher&quot;));

// 构建SslOptions
SslOptions sslOptions = SslOptions.builder()
.truststore(new File(System.getProperty(&quot;redis_trustStore_location&quot;)),
        trustPd)
.keystore(new File(System.getProperty(&quot;redis_keyStore_location&quot;)), keyPd)
.cipher(cipherList).build();

ClusterClientOptions option = (ClusterClientOptions) ClusterClientOptions.builder()
.sslOptions(sslOptions).build();

// 利用redis-server所绑定的IP和Port创建URI，
RedisURI redisURI = RedisURI.create(&quot;100.x.x.152&quot;, 6379);

// 创建集Redis集群模式客户端
RedisClient redisClient = RedisClient.create(redisURI);
// 为客户端设置SSL选项
redisClient.setOptions(option);
StatefulRedisConnection&lt;String, String&gt; connect = redisClient.connect();
RedisCommands&lt;String, String&gt; cmd = connect.sync();

// 执行基本的set、get操作
cmd.set(&quot;key&quot;, &quot;value&quot;);
cmd.get(&quot;key&quot;);

</code></pre>
<h3>4. Redis 集群可靠性问题</h3>
<p>为了便于理解（同时也为了规避安全违规风险），我将原方案进行了适度简化，以 3 主 3 备 Redis 集群为例阐述方案（<code>redis-cluster</code> 模式最少需要三个主节点），如下图所示，其中 A-M 表示主节点 A，A-S 表示主节点 A 对应的从节点，以此类推。</p>
<p><img src="assets/5e5c0580-9671-11e8-bee3-b1dbef72ca56" alt="enter image description here" /></p>
<h4>4.1 可靠性问题一</h4>
<p>Redis 集群并不是将 <code>redis-server</code> 进程启动便可自行建立的。在各个节点启动 <code>redis-server</code> 进程后，形成的只是 6 个“孤立”的 Redis 节点而已，它们相互不知道对方的存在，拓扑结构如下：</p>
<p><img src="assets/6aa306e0-9671-11e8-bd60-15398afc36e1" alt="enter image description here" /></p>
<p>查看每个 Redis 节点的集群配置文件 <code>cluster-config-file</code>，你将看到类似以下内容：</p>
<pre><code>2eca4324c9ee6ac49734e2c1b1f0ce9e74159796 192.168.1.3:6379 myself,master - 0 0 0 connected
vars currentEpoch 0 lastVoteEpoch 0

</code></pre>
<p>很明显，每个 Redis 节点都视自己为 Master 角色，其拓扑结构中也只有自己。为了建立集群，Redis 官方提供了一个基于 Ruby 语言的工具 <code>redis-trib.rb</code>，使用命令便可以创建集群。以 3 主 3 备集群为例，假设节点 IP 和 Port 分别为：</p>
<pre><code>192.168.1.3:6379,192.168.1.3:6380,192.168.1.4:6379,192.168.1.4:6380,192.168.1.5:6379,192.168.1.5:6380 

</code></pre>
<p>则建立集群的命令如下：</p>
<pre><code>redis-trib.rb create --replicas 1 192.168.1.3:6379 192.168.1.3:6380 192.168.1.4:6379 192.168.1.4:6380 192.168.1.5:6379 192.168.1.5:6380

</code></pre>
<p>使用 <code>redis-trib.rb</code> 建立集群虽然便捷，不过，由于 Ruby 语言本身的一系列安全缺陷，有些时候并不是明智的选择。考虑到 Lettuce 提供了极为丰富的 Redis 高级功能，我们完全可以使用 Lettuce 来创建集群，这一点在上一节已经介绍过。</p>
<h4>4.2 节点故障</h4>
<p>三个物理节点，分别部署两个 <code>redis-server</code>，且交叉互为主备，这样做可以提高可靠性：如节点 1 宕机，主节点 A-M 对应的从节点 A-S 将发起投票，作为唯一的备节点，其必然升主成功，与 B-M、C-M 构成新的集群，继续提供服务，如下图所示：</p>
<p><img src="assets/7a5b8850-9671-11e8-9c35-b59aad3fef8b" alt="enter image description here" /></p>
<h4>4.3 故障节点恢复</h4>
<p>接续上一节，如果宕机的节点 1 经过修复重新上线，根据 Redis 集群原理，节点 1 上的 A-M 将意识到自己已经被替代，将降级为备，形成的集群拓扑结构如下：</p>
<p><img src="assets/81b34340-9671-11e8-9f67-05ec09da262a" alt="enter image description here" /></p>
<h4>4.4 可靠性问题二</h4>
<p>基于上述拓扑结构，如果节点 3 宕机，Redis 集群将只有一个主节点 C-M 存活，存活的主节点总数少于集群主节点总数的一半 （<code>1&lt;3/2+1</code>），集群无法自愈，不能继续提供服务。</p>
<p>为了解决这个问题，我们可以设计一个常驻守护进程对 Redis 集群的状态进行监控，当出现主-备状态不合理的情况（如节点 1 重新上线后的拓扑结构），守护进程主动发起主备倒换（clusterFailover），将节点 1 上的 A-S 升为主，节点 3 上的 A-M 降为备，如此，集群拓扑结构恢复正常，并且能够支持单节点故障。</p>
<p><img src="assets/8e851f80-9671-11e8-bee3-b1dbef72ca56" alt="enter image description here" /></p>
<p><strong>注：</strong> Lettuce 提供了主备倒换的方法，示例代码如下：</p>
<pre><code>// slaveConn为Lettuce与从节点建立的连接
slaveConn.sync().clusterFailover(true)

</code></pre>
<h4>4.5 可靠性问题三</h4>
<p>接续 4.1 节，如果节点 1 故障后无法修复，为了保障可靠性，通常会用一个新的节点来替换掉故障的节点——所谓故障替换。拓扑结构如下：</p>
<p><img src="assets/962f4030-9671-11e8-9c35-b59aad3fef8b" alt="enter image description here" /></p>
<p>新的节点上面部署两个 <code>redis-server</code> 进程，由于是新建节点，<code>redis-server</code> 进程对应的集群配置文件 <code>cluster-config-file</code> 中只包含自身的信息，并没有整个集群的信息，简言之，新建的节点上的两个 <code>redis-server</code> 进程是“孤立”的。</p>
<p>为了重新组成集群，我们需要两个步骤：</p>
<ol>
<li>将新节点上的两个 <code>redis-server</code> 纳入现有集群，通过 <code>clusterMeet()</code> 方法可以完成；</li>
<li>为新加入集群的两个 <code>redis-server</code> 设置主节点：节点 3 上的两个主 A-M 和 B-M 都没有对应的从节点，因此，可将新加入的两个 <code>redis-server</code> 分别设置为它们的从节点。</li>
</ol>
<p>完成上述两个步骤后，Redis 集群的拓扑结构将演变成如下形态：</p>
<p><img src="assets/a0b9eb90-9671-11e8-bee3-b1dbef72ca56" alt="enter image description here" /></p>
<p>很明显，变成了问题一的形态，继续通过问题一的解决方案便可修复。</p>
<h4>4.6 其它</h4>
<p>上面仅介绍了几个较为常见的问题，在实际使用 Redis 的过程中可能遇到的问题远不止这些。在第 05 课中，我将介绍一些更为复杂的异常场景。</p>
<h3>5. 基于 Lettuce 的 Redis 集群运维软件设计及实现</h3>
<p>不同的应用场景，关注的问题、可能出现的异常不尽相同，上文中介绍的问题仅仅是一种商业应用场景中遇到的。为了解决上述问题，可基于 Lettuce 设计一个常驻守护进程，实现集群创建、添加节点、平衡主备节点分布、集群运行状态监测、故障自检及故障自愈等功能。</p>
<h4>5.1 总体流程图</h4>
<p>下面是精简后的流程图：</p>
<p><img src="assets/a93a20f0-9671-11e8-bd60-15398afc36e1" alt="enter image description here" /></p>
<p>流程图中，ETCD 选主部分需要特别说明一下，ETCD 和 ZooKeeper 类似，可提供 Leader 选举功能。Redis 集群模式下，在各个 Redis 进程所在主机上均启动一个常驻守护进程，以提高可靠性，但是，为了避免冲突，只有被 ETCD 选举为 Leader 的节点上的常驻守护进程可以执行 “守护” 流程，其它主机上的守护进程呈 “休眠” 状态。关于 Leader 选举的实现，方式很多，本文仅以 ETCD 为例。</p>
<h4>5.2 实现</h4>
<p><strong>集群状态检测</strong></p>
<p>读者应该知道，Redis 集群中每个节点都保存有集群所有节点的状态信息，虽然这些信息可能并不准确。通过状态信息，我们可以判断集群是否存在以及集群的运行状态，基于 Lettuce 提供的方法，简要代码如下：</p>
<p><img src="assets/cab6ab40-9671-11e8-bee3-b1dbef72ca56" alt="enter image description here" /></p>
<p>上面代码只从一个节点的视角进行了检查，完整的代码将遍历所有节点，从所有节点的视角分别检查。</p>
<p><strong>Redis 集群创建</strong></p>
<p>大家可参考第二节“2. 基于 Lettuce 创建 Redis 集群”中的内容。</p>
<p><strong>替换故障节点</strong></p>
<p>（1）加入新节点</p>
<p>替换上来的新节点本质上是“孤立”的，需要先加入现有集群：通过集群命令 RedisAdvancedClusterCommands 对象调用 <code>clusterMeet()</code> 方法，便可实现：</p>
<p><img src="assets/5ac7ecd0-9672-11e8-bd60-15398afc36e1" alt="enter image description here" /></p>
<p>（2）为新节点设置主备关系</p>
<p>首先需要明确，当前集群中哪些 Master 没有 Slave，然后，新节点通过 <code>clusterReplicate()</code> 方法成为对应 Master 的 Slave：</p>
<pre><code>slaveConn.sync().clusterReplicate(masterNode);

</code></pre>
<p><strong>平衡主备节点的分布</strong></p>
<p>（1）状态检测</p>
<p>常驻守护进程通过遍历各个节点获取到的集群状态信息，可以确定某些 Host 上 Master 和 Slave 节点数量不平衡，比如，经过多次故障后，某个 Host 上的 Redis 节点角色全部变成了 Master，不仅影响性能，还会危及可靠性。这个环节的关键点是如何区分 Master 和 Slave，通常我们以是否被指派 Slot 为依据：</p>
<p><img src="assets/736e0b70-9672-11e8-bee3-b1dbef72ca56" alt="enter image description here" /></p>
<p>（2）平衡</p>
<p>如何平衡呢，在创建 Redis 集群的时候，开发者需要制定一个合理的集群拓扑结构（或者算法）来指导集群的创建，如本文介绍的 3 主 3 备模式。那么，在平衡的时候，同样可以依据制定的拓扑结构进行恢复。具体操作很简单：调用 Lettuce 提供的 <code>clusterFailover()</code> 方法即可。</p>
<h4>参考文献与致谢：</h4>
<p>本文的一些图片和文字引用了一些博客和论文，尊重原创是每一个写作者应坚守的底线，在此，将本文引用过的文章一一列出，以表敬意：</p>
<ol>
<li><a href="https://www.cnblogs.com/qiuxiangmuyu/p/6405511.html">密码学之 SSL 双向认证以及证书的制作和使用</a></li>
<li><a href="https://lettuce.io/">Lettuce</a></li>
</ol>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="04&#32;分布式一致性协议&#32;Gossip&#32;和&#32;Redis&#32;集群原理解析.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="06&#32;Redis&#32;实际应用中的异常场景及其根因分析和解决方案.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b434ffd2af7645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
