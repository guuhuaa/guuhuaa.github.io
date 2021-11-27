<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>21 案例：分布式 MySQL 集群工具 Vitess 实践分析.md</title>
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

                    
                    <a href="00&#32;为什么我们要学习&#32;Kubernetes&#32;技术.md">00 为什么我们要学习 Kubernetes 技术.md</a>

                </li>
                <li>

                    
                    <a href="01&#32;重新认识&#32;Kubernetes&#32;的核心组件.md">01 重新认识 Kubernetes 的核心组件.md</a>

                </li>
                <li>

                    
                    <a href="02&#32;深入理解&#32;Kubernets&#32;的编排对象.md">02 深入理解 Kubernets 的编排对象.md</a>

                </li>
                <li>

                    
                    <a href="03&#32;DevOps&#32;场景下落地&#32;K8s&#32;的困难分析.md">03 DevOps 场景下落地 K8s 的困难分析.md</a>

                </li>
                <li>

                    
                    <a href="04&#32;微服务应用场景下落地&#32;K8s&#32;的困难分析.md">04 微服务应用场景下落地 K8s 的困难分析.md</a>

                </li>
                <li>

                    
                    <a href="05&#32;解决&#32;K8s&#32;落地难题的方法论提炼.md">05 解决 K8s 落地难题的方法论提炼.md</a>

                </li>
                <li>

                    
                    <a href="06&#32;练习篇：K8s&#32;核心实践知识掌握.md">06 练习篇：K8s 核心实践知识掌握.md</a>

                </li>
                <li>

                    
                    <a href="07&#32;容器引擎&#32;containerd&#32;落地实践.md">07 容器引擎 containerd 落地实践.md</a>

                </li>
                <li>

                    
                    <a href="08&#32;K8s&#32;集群安装工具&#32;kubeadm&#32;的落地实践.md">08 K8s 集群安装工具 kubeadm 的落地实践.md</a>

                </li>
                <li>

                    
                    <a href="09&#32;南北向流量组件&#32;IPVS&#32;的落地实践.md">09 南北向流量组件 IPVS 的落地实践.md</a>

                </li>
                <li>

                    
                    <a href="10&#32;东西向流量组件&#32;Calico&#32;的落地实践.md">10 东西向流量组件 Calico 的落地实践.md</a>

                </li>
                <li>

                    
                    <a href="11&#32;服务发现&#32;DNS&#32;的落地实践.md">11 服务发现 DNS 的落地实践.md</a>

                </li>
                <li>

                    
                    <a href="12&#32;练习篇：K8s&#32;集群配置测验.md">12 练习篇：K8s 集群配置测验.md</a>

                </li>
                <li>

                    
                    <a href="13&#32;理解对方暴露服务的对象&#32;Ingress&#32;和&#32;Service.md">13 理解对方暴露服务的对象 Ingress 和 Service.md</a>

                </li>
                <li>

                    
                    <a href="14&#32;应用网关&#32;OpenResty&#32;对接&#32;K8s&#32;实践.md">14 应用网关 OpenResty 对接 K8s 实践.md</a>

                </li>
                <li>

                    
                    <a href="15&#32;Service&#32;层引流技术实践.md">15 Service 层引流技术实践.md</a>

                </li>
                <li>

                    
                    <a href="16&#32;Cilium&#32;容器网络的落地实践.md">16 Cilium 容器网络的落地实践.md</a>

                </li>
                <li>

                    
                    <a href="17&#32;应用流量的优雅无损切换实践.md">17 应用流量的优雅无损切换实践.md</a>

                </li>
                <li>

                    
                    <a href="18&#32;练习篇：应用流量无损切换技术测验.md">18 练习篇：应用流量无损切换技术测验.md</a>

                </li>
                <li>

                    
                    <a href="19&#32;使用&#32;Rook&#32;构建生产可用存储环境实践.md">19 使用 Rook 构建生产可用存储环境实践.md</a>

                </li>
                <li>

                    
                    <a href="20&#32;有状态应用的默认特性落地分析.md">20 有状态应用的默认特性落地分析.md</a>

                </li>
                <li>

                    <a class="current-tab" href="21&#32;案例：分布式&#32;MySQL&#32;集群工具&#32;Vitess&#32;实践分析.md">21 案例：分布式 MySQL 集群工具 Vitess 实践分析.md</a>
                    

                </li>
                <li>

                    
                    <a href="22&#32;存储对象&#32;PV、PVC、Storage&#32;Classes&#32;的管理落地实践.md">22 存储对象 PV、PVC、Storage Classes 的管理落地实践.md</a>

                </li>
                <li>

                    
                    <a href="23&#32;K8s&#32;集群中存储对象灾备的落地实践.md">23 K8s 集群中存储对象灾备的落地实践.md</a>

                </li>
                <li>

                    
                    <a href="24&#32;练习篇：K8s&#32;集群配置测验.md">24 练习篇：K8s 集群配置测验.md</a>

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
                        <div><h1>21 案例：分布式 MySQL 集群工具 Vitess 实践分析</h1>
<p>对于 Kubernetes 的有状态应用部署来说，当然最有挑战的例子就是拿 MySQL 集群部署最为经典。在近 10 年的数据库流行度来讲，每一个开发者接触到最多的就是 MySQL 数据库了。几乎人人都知道 MySQL Master/Slave 方式的集群搭建方式，其架构的复杂度可想而知。当我们技术把 MySQL 集群搭建到 Kubernetes 集群的时候就不得不考虑如何利用云原生特性把集群搭建起来。这里笔者并不想去分析如何徒手分解安装 MySQL 集群的 YAML，而是通过有过成功迁移云原生集群工具 Vitess 来总结真实的实践过程。</p>
<h3>Vitess 工具介绍</h3>
<p>Vitess 号称可以水平扩展 MySQL 数据库集群管理工具。最早被我们熟知的新闻就是京东在 618 大促中全面采用云原生技术，其中数据库分片集群管理这块就是采用的 Vitess。接下来我们首先快速体验一下在 Kubernetes 下使用 Vitess 的过程。</p>
<h4><strong>初始化环境</strong></h4>
<p>采用单机部署，在 AWS 上启动一台内存大于 8G 的虚拟机，通过安装 K3s 快速构建一套 Kubernetes 环境。</p>
<pre><code class="language-bash"># 初始化 Kubernetes 单机集群
curl https://releases.rancher.com/install-docker/19.03.sh | sh
curl -sfL https://get.k3s.io | sh -

# 下载 kubectl
curl -LO https://storage.googleapis.com/kubernetes-release/release/v1.14.9/bin/linux/amd64/kubectl
# 安装 MySQL 客户端
apt install mysql-client

# 下载安装客户端 vtctlclient 最新版本：
wget https://github.com/vitessio/vitess/releases/download/v8.0.0/vitess-8.0.0-7e09d0c.tar.gz
tar zxvf vitess-8.0.0-7e09d0c.tar.gz &amp;&amp; cp vitess-8.0.0-7e09d0c/bin/vtctlclient /usr/local/bin/

# 下载 vitess operator 例子
git clone https://github.com/vitessio/vitess.git
cd vitess/examples/operator
k3s kubectl apply -f operator.yaml

<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="9eecf1f1eadef7eeb3afa9acb3adafb3aca9b3acaead">[email&#160;protected]</a>:~/vitess/examples/operator# k3s kubectl get po
NAME                               READY   STATUS    RESTARTS   AGE                                                                                                               
vitess-operator-784458658c-mzhzx   1/1     Running   0          59s 

# 初始化集群
<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="b5c7dadac1f5dcc59884828798868498878298878586">[email&#160;protected]</a>:~/vitess/examples/operator# k3s kubectl apply -f 101_initial_cluster.yaml
vitesscluster.planetscale.com/example created
secret/example-cluster-config created

<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="f2809d9d86b29b82dfc3c5c0dfc1c3dfc0c5dfc0c2c1">[email&#160;protected]</a>:~/vitess/examples/operator# k3s kubectl get pods
NAME                                             READY   STATUS    RESTARTS   AGE
vitess-operator-784458658c-mzhzx                 1/1     Running   0          3m38s
example-etcd-faf13de3-2                          1/1     Running   0          111s
example-etcd-faf13de3-1                          1/1     Running   0          111s
example-etcd-faf13de3-3                          1/1     Running   0          111s
example-zone1-vtctld-1d4dcad0-68484d7b88-428dc   1/1     Running   2          111s
example-zone1-vtgate-bc6cde92-c6499cf87-w86rz    1/1     Running   2          111s
example-vttablet-zone1-2469782763-bfadd780       3/3     Running   2          111s
example-vttablet-zone1-2548885007-46a852d0       3/3     Running   2          111s

</code></pre>
<p>为了方便连接 Vitess 这个 proxy，需要初始化一下端口转发的环境：</p>
<pre><code class="language-bash">./pf.sh &amp;
alias vtctlclient=&quot;vtctlclient -server=localhost:15999&quot;
alias mysql=&quot;mysql -h 127.0.0.1 -P 15306 -u user&quot;

</code></pre>
<p>加载数据库表结构：</p>
<pre><code class="language-bash">vtctlclient ApplySchema -sql=&quot;$(cat create_commerce_schema.sql)&quot; commerce
vtctlclient ApplyVSchema -vschema=&quot;$(cat vschema_commerce_initial.json)&quot; commerce

</code></pre>
<p>通过 MySQL 连接 Vitess Proxy 访问 MySQL Server：</p>
<pre><code class="language-bash">~/vitess/examples/operator$ mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 3
Server version: 5.7.9-Vitess MySQL Community Server (GPL)

Copyright (c) 2000, 2020, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql&gt; show databases;
+-----------+
| Databases |
+-----------+
| commerce  |
+-----------+
1 row in set (0.00 sec)

</code></pre>
<p>至此，我们的体验和安装一套本地的 MySQL Server 是一样的。这种透明的体验值得我们接下来持续挖掘更高级的特性。</p>
<p>下图说明了 Vitess 的组件架构，我们需要熟悉这些术语：</p>
<p><img src="assets/36be7e60-2cc7-11eb-90f6-fbd19bda6e6e" alt="18-1-vitess-arch33" /></p>
<p><strong>Topology</strong></p>
<p>拓扑服务是一个元数据存储对象，包含有关正在运行的服务器、分片方案和复制关系图的信息。拓扑由一致性的数据存储支持，默认支持 etcd2 插件。您可以使用 vtctl（命令行）和 vtctld（web）查看拓扑信息。</p>
<p><strong>VTGate</strong></p>
<p>VTGate 是一个轻型代理服务器，它将流量路由到正确的 VTTablet，并将合并的结果返回给客户端。应用程序向 VTGate 发起查询。客户端使用起来非常简单，它只需要能够找到 VTGate 实例就能使 Vitess。</p>
<p><strong>VTTablet</strong></p>
<p>VTTablet 是一个位于 MySQL 数据库前面的代理服务器，执行的任务试图最大化吞吐量，同时保护 MySQL 不受有害查询的影响。它的特性包括连接池、查询重写和重用重复数据。</p>
<p><strong>Keyspace</strong></p>
<p>关键空间是一个逻辑数据库。如果使用 Sharding，一个 keyspace 映射到多个 MySQL 数据库；如果不使用 Sharding，一个 keyspace 直接映射到一个 MySQL 数据库名。无论哪种情况，从应用程序的角度来看，一个关键空间都是作为一个单一的数据库出现的。</p>
<p>从一个关键空间读取数据就像从 MySQL 数据库读取数据一样。然而，根据读取操作的一致性要求，Vitess 可能会从主数据库或副本中获取数据。通过将每个查询路由到适当的数据库，Vitess 允许你的代码结构化，就像从一个 MySQL 数据库中读取一样。</p>
<h3>Vitess 高级特性介绍</h3>
<p>Sharding 是一种水平分区数据库的方法，用于在两个或多个数据库服务器上存储数据。下面我们讲解 Vitess 中的 Sharding 如何工作以及 Vitess 支持的 Sharding 类型。</p>
<p>Vitess 中的 keyspace 可以是分片的，也可以是非碎片化的，非分片化的 keyspace 可以直接映射到 MySQL 数据库。如果是分片的，keyspace 的行被分割到相同模式的不同数据库中。</p>
<p>例如，如果一个应用程序的 &quot;User&quot; keyspace 被分割成两个分片，那么每个分片包含了该应用程序大约一半用户的记录。同样，每个用户的信息也只存储在一个 Shard 中。</p>
<p>请注意，Sharding 与（MySQL）复制是正交的。一个 Vitess Shard 通常包含一个 MySQL 主程序和许多 MySQL 副本。主程序处理写操作，而副本则处理只读流量、批处理操作和其他任务。除了一些复制滞后外，Shard 内的每个 MySQL 实例都应该有相同的数据。</p>
<table>
<thead>
<tr>
<th align="left">需求</th>
<th align="left">动作</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">统一增加读容量</td>
<td align="left">增加副本或分片</td>
</tr>
<tr>
<td align="left">统一增加写容量</td>
<td align="left">分片 shards</td>
</tr>
<tr>
<td align="left">回收过剩的资源</td>
<td align="left">合并 shards 或 keyspaces</td>
</tr>
<tr>
<td align="left">增加地理多样性</td>
<td align="left">增加新的分区和副本</td>
</tr>
<tr>
<td align="left">热表处理</td>
<td align="left">对于只读热表，多加副本或分片；对于写表，直接分片</td>
</tr>
</tbody>
</table>
<p>应用新的 VSchema 会指示 Vitess 键空间是分片的，这可能会阻止一些复杂的查询。在进行这一步之前，最好先验证一下。如果你确实注意到某些查询开始失败，你总是可以通过恢复旧的 VSchema 来暂时恢复。确保在进入 Reshard 过程之前修复了所有的查询。</p>
<pre><code class="language-bash">vtctlclient ApplySchema -sql=&quot;$(cat create_commerce_seq.sql)&quot; commerce
vtctlclient ApplyVSchema -vschema=&quot;$(cat vschema_commerce_seq.json)&quot; commerce
vtctlclient ApplySchema -sql=&quot;$(cat create_customer_sharded.sql)&quot; customer
vtctlclient ApplyVSchema -vschema=&quot;$(cat vschema_customer_sharded.json)&quot; customer    

</code></pre>
<p>在这一点上，你已经最终确定了你的分片 VSchema，并审核了所有的查询，以确保它们仍然有效。现在是时候重新分片了。</p>
<p>重新 Sharding 的过程是通过将现有的 shard 分割成更小的 shard。这种类型的重新 Sharding 是最适合 Vitess 的。在某些情况下，您可能希望引入一个新的分片，并在最近创建的分片中添加新行。在 Vitess 中，可以通过拆分 Shard 的方式来实现这一点。</p>
<pre><code class="language-bash">kubectl apply -f 302_new_shards.yaml

killall kubectl
./pf.sh &amp;

# With Operator on Start the Reshard
vtctlclient Reshard customer.cust2cust '-' '-80,80-'

</code></pre>
<p>在 Reshard 完成后，我们可以使用 VDiff 来检查数据的完整性，确保我们的源和目标分片是一致的。</p>
<pre><code class="language-bash">vtctlclient VDiff customer.cust2cust
# 返回如下内容
Summary for customer: {ProcessedRows:5 MatchingRows:5 MismatchedRows:0 ExtraRowsSource:0 ExtraRowsTarget:0}
Summary for corder: {ProcessedRows:5 MatchingRows:5 MismatchedRows:0 ExtraRowsSource:0 ExtraRowsTarget:0}

</code></pre>
<p>手工切换读、写操作到新分片。确保数据库正常执行：</p>
<pre><code class="language-bash">vtctlclient SwitchReads -tablet_type=rdonly customer.cust2cust
vtctlclient SwitchReads -tablet_type=replica customer.cust2cust

vtctlclient SwitchWrites customer.cust2cust

mysql --table &lt; ../common/select_customer-80_data.sql
Using customer/-80
Customer
+-------------+--------------------+
| customer_id | email              |
+-------------+--------------------+
|           1 | <a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="2544494c464065414a48444c4b0b464a48">[email&#160;protected]</a>   |
|           2 | <a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="fc9e939ebc9893919d9592d29f9391">[email&#160;protected]</a>     |
|           3 | <a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="3a59525b4856535f7a5e55575b535414595557">[email&#160;protected]</a> |
|           5 | <a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="afcad9caefcbc0c2cec6c181ccc0c2">[email&#160;protected]</a>     |
+-------------+--------------------+
COrder
+----------+-------------+----------+-------+
| order_id | customer_id | sku      | price |
+----------+-------------+----------+-------+
|        1 |           1 | SKU-1001 |   100 |
|        2 |           2 | SKU-1002 |    30 |
|        3 |           3 | SKU-1002 |    30 |
|        5 |           5 | SKU-1002 |    30 |
+----------+-------------+----------+-------+

mysql --table &lt; ../common/select_customer80-_data.sql
Using customer/80-
Customer
+-------------+----------------+
| customer_id | email          |
+-------------+----------------+
|           4 | <a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="690d0807290d0604080007470a0604">[email&#160;protected]</a> |
+-------------+----------------+
COrder
+----------+-------------+----------+-------+
| order_id | customer_id | sku      | price |
+----------+-------------+----------+-------+
|        4 |           4 | SKU-1002 |    30 |
+----------+-------------+----------+-------+

</code></pre>
<h3>总结</h3>
<p>应用 Vitess Operator 之后，收获最大的就是完全不用操心 MySQL 复制集群的架构设计，由 Vitess Operator 来管理高可用和数据库的分片，把复杂的分布式部署的运维问题屏蔽了一大半。当然，作为运维人员需要注意的是，因为 Vitess 是一个 Proxy，它和 MySQL 原生接口的协议还是有一些不一样的地方，需要适配。因为京东在 618 大促中采用了 Vitess 技术来支撑数据库集群，让我们可以放心大胆地使用它。</p>
<h3>参考资料</h3>
<ul>
<li><a href="https://vitess.io/zh/docs/get-started/kubernetes/">https://vitess.io/zh/docs/get-started/kubernetes/</a></li>
</ul>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="20&#32;有状态应用的默认特性落地分析.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="22&#32;存储对象&#32;PV、PVC、Storage&#32;Classes&#32;的管理落地实践.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script data-cfasync="false" src="../../cdn-cgi/scripts/5c5dd728/cloudflare-static/email-decode.min.js"></script><script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b4346af797370ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
            document.getElementById("tip").innerHTML = "<a href='https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/Kubernetes%20%E5%AE%9E%E8%B7%B5%E5%85%A5%E9%97%A8%E6%8C%87%E5%8D%97/&quot;&#32;+&#32;cookie&#32;+&#32;&quot;'>跳转到上次进度</a>"
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
