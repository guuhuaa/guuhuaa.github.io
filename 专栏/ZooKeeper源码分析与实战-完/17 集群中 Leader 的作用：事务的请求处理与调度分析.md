<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>17 集群中 Leader 的作用：事务的请求处理与调度分析.md</title>
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

                    
                    <a href="00&#32;开篇词：选择&#32;ZooKeeper，一步到位掌握分布式开发.md">00 开篇词：选择 ZooKeeper，一步到位掌握分布式开发.md</a>

                </li>
                <li>

                    
                    <a href="01&#32;ZooKeeper&#32;数据模型：节点的特性与应用.md">01 ZooKeeper 数据模型：节点的特性与应用.md</a>

                </li>
                <li>

                    
                    <a href="02&#32;发布订阅模式：如何使用&#32;Watch&#32;机制实现分布式通知.md">02 发布订阅模式：如何使用 Watch 机制实现分布式通知.md</a>

                </li>
                <li>

                    
                    <a href="03&#32;ACL&#32;权限控制：如何避免未经授权的访问？.md">03 ACL 权限控制：如何避免未经授权的访问？.md</a>

                </li>
                <li>

                    
                    <a href="04&#32;ZooKeeper&#32;如何进行序列化？.md">04 ZooKeeper 如何进行序列化？.md</a>

                </li>
                <li>

                    
                    <a href="05&#32;深入分析&#32;Jute&#32;的底层实现原理.md">05 深入分析 Jute 的底层实现原理.md</a>

                </li>
                <li>

                    
                    <a href="06&#32;ZooKeeper&#32;的网络通信协议详解.md">06 ZooKeeper 的网络通信协议详解.md</a>

                </li>
                <li>

                    
                    <a href="07&#32;单机模式：服务器如何从初始化到对外提供服务？.md">07 单机模式：服务器如何从初始化到对外提供服务？.md</a>

                </li>
                <li>

                    
                    <a href="08&#32;集群模式：服务器如何从初始化到对外提供服务？.md">08 集群模式：服务器如何从初始化到对外提供服务？.md</a>

                </li>
                <li>

                    
                    <a href="09&#32;创建会话：避开日常开发的那些“坑”.md">09 创建会话：避开日常开发的那些“坑”.md</a>

                </li>
                <li>

                    
                    <a href="10&#32;ClientCnxn：客户端核心工作类工作原理解析.md">10 ClientCnxn：客户端核心工作类工作原理解析.md</a>

                </li>
                <li>

                    
                    <a href="11&#32;分桶策略：如何实现高效的会话管理？.md">11 分桶策略：如何实现高效的会话管理？.md</a>

                </li>
                <li>

                    
                    <a href="12&#32;服务端是如何处理一次会话请求的？.md">12 服务端是如何处理一次会话请求的？.md</a>

                </li>
                <li>

                    
                    <a href="13&#32;Curator：如何降低&#32;ZooKeeper&#32;使用的复杂性？.md">13 Curator：如何降低 ZooKeeper 使用的复杂性？.md</a>

                </li>
                <li>

                    
                    <a href="14&#32;Leader&#32;选举：如何保证分布式数据的一致性？.md">14 Leader 选举：如何保证分布式数据的一致性？.md</a>

                </li>
                <li>

                    
                    <a href="15&#32;ZooKeeper&#32;究竟是怎么选中&#32;Leader&#32;的？.md">15 ZooKeeper 究竟是怎么选中 Leader 的？.md</a>

                </li>
                <li>

                    
                    <a href="16&#32;ZooKeeper&#32;集群中&#32;Leader&#32;与&#32;Follower&#32;的数据同步策略.md">16 ZooKeeper 集群中 Leader 与 Follower 的数据同步策略.md</a>

                </li>
                <li>

                    <a class="current-tab" href="17&#32;集群中&#32;Leader&#32;的作用：事务的请求处理与调度分析.md">17 集群中 Leader 的作用：事务的请求处理与调度分析.md</a>
                    

                </li>
                <li>

                    
                    <a href="18&#32;集群中&#32;Follow&#32;的作用：非事务请求的处理与&#32;Leader&#32;的选举分析.md">18 集群中 Follow 的作用：非事务请求的处理与 Leader 的选举分析.md</a>

                </li>
                <li>

                    
                    <a href="19&#32;Observer&#32;的作用与&#32;Follow&#32;有哪些不同？.md">19 Observer 的作用与 Follow 有哪些不同？.md</a>

                </li>
                <li>

                    
                    <a href="20&#32;一个运行中的&#32;ZooKeeper&#32;服务会产生哪些数据和文件？.md">20 一个运行中的 ZooKeeper 服务会产生哪些数据和文件？.md</a>

                </li>
                <li>

                    
                    <a href="21&#32;ZooKeeper&#32;分布式锁：实现和原理解析.md">21 ZooKeeper 分布式锁：实现和原理解析.md</a>

                </li>
                <li>

                    
                    <a href="22&#32;基于&#32;ZooKeeper&#32;命名服务的应用：分布式&#32;ID&#32;生成器.md">22 基于 ZooKeeper 命名服务的应用：分布式 ID 生成器.md</a>

                </li>
                <li>

                    
                    <a href="23&#32;使用&#32;ZooKeeper&#32;实现负载均衡服务器功能.md">23 使用 ZooKeeper 实现负载均衡服务器功能.md</a>

                </li>
                <li>

                    
                    <a href="24&#32;ZooKeeper&#32;在&#32;Kafka&#32;和&#32;Dubbo&#32;中的工业级实现案例分析.md">24 ZooKeeper 在 Kafka 和 Dubbo 中的工业级实现案例分析.md</a>

                </li>
                <li>

                    
                    <a href="25&#32;如何搭建一个高可用的&#32;ZooKeeper&#32;生产环境？.md">25 如何搭建一个高可用的 ZooKeeper 生产环境？.md</a>

                </li>
                <li>

                    
                    <a href="26&#32;JConsole&#32;与四字母命令：如何监控服务器上&#32;ZooKeeper&#32;的运行状态？.md">26 JConsole 与四字母命令：如何监控服务器上 ZooKeeper 的运行状态？.md</a>

                </li>
                <li>

                    
                    <a href="27&#32;crontab&#32;与&#32;PurgeTxnLog：线上系统日志清理的最佳时间和方式.md">27 crontab 与 PurgeTxnLog：线上系统日志清理的最佳时间和方式.md</a>

                </li>
                <li>

                    
                    <a href="28&#32;彻底掌握二阶段提交三阶段提交算法原理.md">28 彻底掌握二阶段提交三阶段提交算法原理.md</a>

                </li>
                <li>

                    
                    <a href="29&#32;ZAB&#32;协议算法：崩溃恢复和消息广播.md">29 ZAB 协议算法：崩溃恢复和消息广播.md</a>

                </li>
                <li>

                    
                    <a href="30&#32;ZAB&#32;与&#32;Paxos&#32;算法的联系与区别.md">30 ZAB 与 Paxos 算法的联系与区别.md</a>

                </li>
                <li>

                    
                    <a href="31&#32;ZooKeeper&#32;中二阶段提交算法的实现分析.md">31 ZooKeeper 中二阶段提交算法的实现分析.md</a>

                </li>
                <li>

                    
                    <a href="32&#32;ZooKeeper&#32;数据存储底层实现解析.md">32 ZooKeeper 数据存储底层实现解析.md</a>

                </li>
                <li>

                    
                    <a href="33&#32;结束语&#32;&#32;分布技术发展与&#32;ZooKeeper&#32;应用前景.md">33 结束语  分布技术发展与 ZooKeeper 应用前景.md</a>

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
                        <div><h1>17 集群中 Leader 的作用：事务的请求处理与调度分析</h1>
<p>本课时主要学习 Leader 在集群中的作用以及实现原理，在前面的课程中我们一直围绕 ZooKeeper 集群的功能来研究其底层实现原理，今天这节课我们还是围绕这个主题来进一步探究 Leader 服务器在 ZooKeeper 中的作用，即处理事务性的会话请求以及管理 ZooKeeper 集群中的其他角色服务器。而在接收到来自客户端的事务性会话请求后，ZooKeeper 集群内部又</p>
<p>是如何判断会话的请求类型，以及转发处理事务性请求的呢？带着这些问题我们继续本节课的学习。</p>
<h3>事务性请求处理</h3>
<p>在 ZooKeeper 集群接收到来自客户端的会话请求操作后，首先会判断该条请求是否是事务性的会话请求。对于事务性的会话请求，ZooKeeper 集群服务端会将该请求统一转发给 Leader 服务器进行操作。通过前面我们讲过的，Leader 服务器内部执行该条事务性的会话请求后，再将数据同步给其他角色服务器，从而保证事务性会话请求的执行顺序，进而保证整个 ZooKeeper 集群的数据一致性。</p>
<p>在 ZooKeeper 集群的内部实现中，是通过什么方法保证所有 ZooKeeper 集群接收到的事务性会话请求都能交给 Leader 服务器进行处理的呢？下面我们就带着这个问题继续学习。</p>
<p>在 ZooKeeper 集群内部，集群中除 Leader 服务器外的其他角色服务器接收到来自客户端的事务性会话请求后，必须将该条会话请求转发给 Leader 服务器进行处理。 ZooKeeper 集群中的 Follow 和 Observer 服务器，都会检查当前接收到的会话请求是否是事务性的请求，如果是事务性的请求，那么就将该请求以 REQUEST 消息类型转发给 Leader 服务器。</p>
<p>在 ZooKeeper集群中的服务器接收到该条消息后，会对该条消息进行解析。分析出该条消息所包含的原始客户端会话请求。之后将该条消息提交到自己的 Leader 服务器请求处理链中，开始进行事务性的会话请求操作。如果不是事务性请求，ZooKeeper 集群则交由 Follow 和 Observer 角色服务器处理该条会话请求，如查询数据节点信息。</p>
<h3>Leader 事务处理分析</h3>
<p>上面我们介绍了 ZooKeeper 集群在处理事务性会话请求时的内部原理。接下来我们就以客户端发起的创建节点请求 setData 为例，具体看看 ZooKeeper 集群的底层处理过程。</p>
<p>在 ZooKeeper 集群接收到来自客户端的一个 setData 会话请求后，其内部的处理逻辑基本可以分成四个部分。如下图所示，分别是预处理阶段、事务处理阶段、事务执行阶段、响应客户端。</p>
<p><img src="assets/CgqCHl78TTKAVHIcAABFlvJZKxw198.png" alt="image.png" /></p>
<h4>预处理阶段：</h4>
<p>在预处理阶段，主要工作是通过网络 I/O 接收来自客户端的会话请求。判断该条会话请求的类型是否是事务性的会话请求，之后将该请求提交给</p>
<p>PrepRequestProcessor 处理器进行处理。封装请求事务头并检查会话是否过期，最后反序列化事务请求信息创建 setDataRequest 请求，在 setDataRequest 记录中包含了要创建数据的节点的路径、数据节点的内容信息以及数据节点的版本信息。最后将该请求存放在 outstandingChanges 队列中等待之后的处理。</p>
<p><img src="assets/CgqCHl78TUKAfJjuAAB5F0dP0Yk087.png" alt="1.png" /></p>
<h4>事务处理阶段：</h4>
<p>在事务处理阶段，ZooKeeper 集群内部会将该条会话请求提交给 ProposalRequestProcessor 处理器进行处理。本阶段内部又分为提交、同步、统计三个步骤。其具体的处理过程我们在之前的课程中已经介绍过了，这里不再赘述。</p>
<p><img src="assets/CgqCHl78TVGAK4VLAACDtg8BUbg363.png" alt="2.png" /></p>
<h4>事务执行阶段：</h4>
<p>在经过预处理阶段和事务会话的投票发起等操作后，一个事务性的会话请求都已经准备好了，接下来就是在 ZooKeeper 的数据库中执行该条会话的数据变更操作。</p>
<p>在处理数据变更的过程中，ZooKeeper 内部会将该请求会话的事务头和事务体信息直接交给内存数据库 ZKDatabase 进行事务性的持久化操作。之后返回 ProcessTxnResult 对象表明操作结果是否成功。</p>
<p><img src="assets/CgqCHl78TWOAcPwoAABCnE5qDAc777.png" alt="3.png" /></p>
<h4>响应客户端：</h4>
<p>在 ZooKeeper 集群处理完客户端 setData 方法发送的数据节点创建请求后，会将处理结果发送给客户端。而在响应客户端的过程中，ZooKeeper 内部首先会创建一个 setDataResponse 响应体类型，该对象主要包括当前会话请求所创建的数据节点，以及其最新状态字段信息 stat。之后创建请求响应头信息，响应头作为客户端请求响应的重要信息，客户端在接收到 ZooKeeper 集群的响应后，通过解析响应头信息中的事务 ZXID 和请求结果标识符 err 来判断该条会话请求是否成功执行。</p>
<p><img src="assets/CgqCHl78TXCAM65nAAB2mZDf_jw385.png" alt="4.png" /></p>
<h3>事务处理底层实现</h3>
<p>介绍完 ZooKeeper 集群处理事务性会话请求的理论方法和内部过程后。接下来我们从代码层面来进一步分析 ZooKeeper 在处理事务性请求时的底层核心代码实现。</p>
<p>首先，ZooKeeper 集群在收到客户端发送的事务性会话请求后，会对该请求进行预处理。在代码层面，ZooKeeper 通过调用 PrepRequestProcessor 类来实现预处理阶段的全部逻辑。可以这样理解：<strong>在处理客户端会话请求的时候，首先调用的就是 PrepRequestProcessor 类</strong>。而在 PrepRequestProcessor 内部，是通过 pRequest 方法判断客户端发送的会话请求类型。如果是诸如 setData 数据节点创建等事务性的会话请求，就调用 pRequest2Txn 方法进一步处理。</p>
<pre><code>protected void pRequest(Request request){

...

  switch (request.type) {

  case OpCode.setData:

    SetDataRequest setDataRequest = new SetDataRequest();                

    pRequest2Txn(request.type, zks.getNextZxid(), request, setDataRequest, true);

    break;

   }

}
</code></pre>
<p>而在 pRequest2Txn 方法的内部，就实现了预处理阶段的主要逻辑。如下面的代码所示，首先通过 checkSession 方法检查该条会话请求是否有效（比如会话是否过期等），之后调用 checkACL 检查发起会话操作的客户端在 ZooKeeper 服务端是否具有相关操作的权限。最后将该条会话创建的相关信息，诸如 path 节点路径、data 节点数据信息、version 节点版本信息等字段封装成
setDataRequest 类型并传入到 setTxn 方法中，最后加入处理链中进行处理。</p>
<pre><code>case OpCode.setData:

    zks.sessionTracker.checkSession(request.sessionId, request.getOwner());

    SetDataRequest setDataRequest = (SetDataRequest)record;

    if(deserialize)

        ByteBufferInputStream.byteBuffer2Record(request.request, setDataRequest);

    path = setDataRequest.getPath();

    validatePath(path, request.sessionId);

    nodeRecord = getRecordForPath(path);

    checkACL(zks, request.cnxn, nodeRecord.acl, ZooDefs.Perms.WRITE, request.authInfo, path, null);

    int newVersion = checkAndIncVersion(nodeRecord.stat.getVersion(), setDataRequest.getVersion(), path);

    request.setTxn(new SetDataTxn(path, setDataRequest.getData(), newVersion));

    nodeRecord = nodeRecord.duplicate(request.getHdr().getZxid());

    nodeRecord.stat.setVersion(newVersion);

    addChangeRecord(nodeRecord);
</code></pre>
<h3>结束</h3>
<p>在本课时中，我们主要学习了 ZooKeeper 集群中 Leader 服务器是如何处理事务性的会话请求的，并且在处理完事务性的会话请求后，是如何通知其他角色服务器进行同步操作的。</p>
<p>可以说在 ZooKeeper 集群处理事务性的请过程中，Follow 和 Observer 服务器主要负责接收客户端的会话请求，并转发给 Leader 服务器。而真正处理该条会话请求的是 Leader 服务器。</p>
<p>这就会引发一个问题：当一个业务场景在查询操作多而创建删除等事务性操作少的情况下，ZooKeeper 集群的性能表现的就会很好。而如果是在极端情况下，ZooKeeper 集群只有事务性的会话请求而没有查询操作，那么 Follow 和 Observer 服务器就只能充当一个请求转发服务器的角色， 所有的会话的处理压力都在 Leader 服务器。在处理性能上整个集群服务器的瓶颈取决于 Leader 服务器的性能。ZooKeeper 集群的作用只能保证在 Leader 节点崩溃的时候，重新选举出 Leader 服务器保证系统的稳定性。这也是 ZooKeeper 设计的一个缺点。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="16&#32;ZooKeeper&#32;集群中&#32;Leader&#32;与&#32;Follower&#32;的数据同步策略.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="18&#32;集群中&#32;Follow&#32;的作用：非事务请求的处理与&#32;Leader&#32;的选举分析.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b434ee93ad470ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
            document.getElementById("tip").innerHTML = "<a href='https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/ZooKeeper%E6%BA%90%E7%A0%81%E5%88%86%E6%9E%90%E4%B8%8E%E5%AE%9E%E6%88%98-%E5%AE%8C/&quot;&#32;+&#32;cookie&#32;+&#32;&quot;'>跳转到上次进度</a>"
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
