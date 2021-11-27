<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>16 常用的缓存组件Redis是如何运行的？.md</title>
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

                    
                    <a href="00&#32;开篇寄语：缓存，你真的用对了吗？.md">00 开篇寄语：缓存，你真的用对了吗？.md</a>

                </li>
                <li>

                    
                    <a href="01&#32;业务数据访问性能太低怎么办？.md">01 业务数据访问性能太低怎么办？.md</a>

                </li>
                <li>

                    
                    <a href="02&#32;如何根据业务来选择缓存模式和组件？.md">02 如何根据业务来选择缓存模式和组件？.md</a>

                </li>
                <li>

                    
                    <a href="03&#32;设计缓存架构时需要考量哪些因素？.md">03 设计缓存架构时需要考量哪些因素？.md</a>

                </li>
                <li>

                    
                    <a href="04&#32;缓存失效、穿透和雪崩问题怎么处理？.md">04 缓存失效、穿透和雪崩问题怎么处理？.md</a>

                </li>
                <li>

                    
                    <a href="05&#32;缓存数据不一致和并发竞争怎么处理？.md">05 缓存数据不一致和并发竞争怎么处理？.md</a>

                </li>
                <li>

                    
                    <a href="06&#32;Hot&#32;Key和Big&#32;Key引发的问题怎么应对？.md">06 Hot Key和Big Key引发的问题怎么应对？.md</a>

                </li>
                <li>

                    
                    <a href="07&#32;MC为何是应用最广泛的缓存组件？.md">07 MC为何是应用最广泛的缓存组件？.md</a>

                </li>
                <li>

                    
                    <a href="08&#32;MC系统架构是如何布局的？.md">08 MC系统架构是如何布局的？.md</a>

                </li>
                <li>

                    
                    <a href="09&#32;MC是如何使用多线程和状态机来处理请求命令的？.md">09 MC是如何使用多线程和状态机来处理请求命令的？.md</a>

                </li>
                <li>

                    
                    <a href="10&#32;MC是怎么定位key的.md">10 MC是怎么定位key的.md</a>

                </li>
                <li>

                    
                    <a href="11&#32;MC如何淘汰冷key和失效key.md">11 MC如何淘汰冷key和失效key.md</a>

                </li>
                <li>

                    
                    <a href="12&#32;为何MC能长期维持高性能读写？.md">12 为何MC能长期维持高性能读写？.md</a>

                </li>
                <li>

                    
                    <a href="13&#32;如何完整学习MC协议及优化client访问？.md">13 如何完整学习MC协议及优化client访问？.md</a>

                </li>
                <li>

                    
                    <a href="14&#32;大数据时代，MC如何应对新的常见问题？.md">14 大数据时代，MC如何应对新的常见问题？.md</a>

                </li>
                <li>

                    
                    <a href="15&#32;如何深入理解、应用及扩展&#32;Twemproxy？.md">15 如何深入理解、应用及扩展 Twemproxy？.md</a>

                </li>
                <li>

                    <a class="current-tab" href="16&#32;常用的缓存组件Redis是如何运行的？.md">16 常用的缓存组件Redis是如何运行的？.md</a>
                    

                </li>
                <li>

                    
                    <a href="17&#32;如何理解、选择并使用Redis的核心数据类型？.md">17 如何理解、选择并使用Redis的核心数据类型？.md</a>

                </li>
                <li>

                    
                    <a href="18&#32;Redis协议的请求和响应有哪些“套路”可循？.md">18 Redis协议的请求和响应有哪些“套路”可循？.md</a>

                </li>
                <li>

                    
                    <a href="19&#32;Redis系统架构中各个处理模块是干什么的？.md">19 Redis系统架构中各个处理模块是干什么的？.md</a>

                </li>
                <li>

                    
                    <a href="20&#32;Redis如何处理文件事件和时间事件？.md">20 Redis如何处理文件事件和时间事件？.md</a>

                </li>
                <li>

                    
                    <a href="21&#32;Redis读取请求数据后，如何进行协议解析和处理.md">21 Redis读取请求数据后，如何进行协议解析和处理.md</a>

                </li>
                <li>

                    
                    <a href="22&#32;怎么认识和应用Redis内部数据结构？.md">22 怎么认识和应用Redis内部数据结构？.md</a>

                </li>
                <li>

                    
                    <a href="23&#32;Redis是如何淘汰key的？.md">23 Redis是如何淘汰key的？.md</a>

                </li>
                <li>

                    
                    <a href="24&#32;Redis崩溃后，如何进行数据恢复的？.md">24 Redis崩溃后，如何进行数据恢复的？.md</a>

                </li>
                <li>

                    
                    <a href="25&#32;&#32;Redis是如何处理容易超时的系统调用的？.md">25  Redis是如何处理容易超时的系统调用的？.md</a>

                </li>
                <li>

                    
                    <a href="26&#32;如何大幅成倍提升Redis处理性能？.md">26 如何大幅成倍提升Redis处理性能？.md</a>

                </li>
                <li>

                    
                    <a href="27&#32;Redis是如何进行主从复制的？.md">27 Redis是如何进行主从复制的？.md</a>

                </li>
                <li>

                    
                    <a href="28&#32;如何构建一个高性能、易扩展的Redis集群？.md">28 如何构建一个高性能、易扩展的Redis集群？.md</a>

                </li>
                <li>

                    
                    <a href="29&#32;从容应对亿级QPS访问，Redis还缺少什么？.md">29 从容应对亿级QPS访问，Redis还缺少什么？.md</a>

                </li>
                <li>

                    
                    <a href="30&#32;面对海量数据，为什么无法设计出完美的分布式缓存体系？.md">30 面对海量数据，为什么无法设计出完美的分布式缓存体系？.md</a>

                </li>
                <li>

                    
                    <a href="31&#32;如何设计足够可靠的分布式缓存体系，以满足大中型移动互联网系统的需要？.md">31 如何设计足够可靠的分布式缓存体系，以满足大中型移动互联网系统的需要？.md</a>

                </li>
                <li>

                    
                    <a href="32&#32;一个典型的分布式缓存系统是什么样的？.md">32 一个典型的分布式缓存系统是什么样的？.md</a>

                </li>
                <li>

                    
                    <a href="33&#32;如何为秒杀系统设计缓存体系？.md">33 如何为秒杀系统设计缓存体系？.md</a>

                </li>
                <li>

                    
                    <a href="34&#32;如何为海量计数场景设计缓存体系？.md">34 如何为海量计数场景设计缓存体系？.md</a>

                </li>
                <li>

                    
                    <a href="35&#32;如何为社交feed场景设计缓存体系？.md">35 如何为社交feed场景设计缓存体系？.md</a>

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
                        <div><h1>16 常用的缓存组件Redis是如何运行的？</h1>
<p>你好，我是你的缓存课老师陈波，欢迎进入第 16 课时“Redis 基本原理”的学习。</p>
<h6>Redis 基本原理</h6>
<h6>Redis 简介</h6>
<p>Redis 是一款基于 ANSI C 语言编写的，BSD 许可的，日志型 key-value 存储组件，它的所有数据结构都存在内存中，可以用作缓存、数据库和消息中间件。</p>
<p>Redis 是 Remote dictionary server 即远程字典服务的缩写，一个 Redis 实例可以有多个存储数据的字典，客户端可以通过 select 来选择字典即 DB 进行数据存储。</p>
<h6>Redis 特性</h6>
<p>同为 key-value 存储组件，Memcached 只能支持二进制字节块这一种数据类型。而 Redis 的数据类型却丰富的多，它具有 8 种核心数据类型，每种数据类型都有一系列操作指令对应。Redis 性能很高，单线程压测可以达到 10~11w 的 QPS。</p>
<p>虽然 Redis 所有数据的读写操作，都在内存中进行，但也可以将所有数据进行落盘做持久化。Redis 提供了 2 种持久化方式。</p>
<ul>
<li>快照方式，将某时刻所有数据都写入硬盘的 RDB 文件；</li>
<li>追加文件方式，即将所有写命令都以追加的方式写入硬盘的 AOF 文件中。</li>
</ul>
<p>线上 Redis 一般会同时使用两种方式，通过开启 appendonly 及关联配置项，将写命令及时追加到 AOF 文件，同时在每日流量低峰时，通过 bgsave 保存当时所有内存数据快照。</p>
<p>对于互联网系统的线上流量，读操作远远大于写操作。以微博为例，读请求占总体流量的 90%左右。大量的读请求，通常会远超 Redis 的可承载范围。此时，可以使用 Redis 的复制特性，让一个 Redis 实例作为 master，然后通过复制挂载多个不断同步更新的副本，即多个 slave。通过读写分离，把所有写操作落在 Redis 的 master，所有读操作随机落在 Redis 的多个 slave 中，从而大幅提升 Redis 的读写能力。</p>
<p>Lua 是一个高效、简洁、易扩展的脚本语言，可以方便的嵌入其他语言中使用。Redis 自 2.6 版本开始支持 Lua。通过支持 client 端自定义的 Lua 脚本，Redis 可以减少网络开销，提升处理性能，还可以把脚本中的多个操作作为一个整体来操作，实现原子性更新。</p>
<p>Redis 还支持事务，在 multi 指令后，指定多个操作，然后通过 exec 指令一次性执行，中途如果出现异常，则不执行所有命令操作，否则，按顺序一次性执行所有操作，执行过程中不会执行任何其他指令。</p>
<p>Redis 还支持 Cluster 特性，可以通过自动或手动方式，将所有 key 按哈希分散到不同节点，在容量不足时，还可以通过 Redis 的迁移指令，把其中一部分 key 迁移到其他节点。</p>
<p><img src="assets/CgotOV2lPF-AZ1LCAAEXirWDhew753.png" alt="img" /></p>
<p>对于 Redis 的特性，可以通过这张思维导图，做个初步了解。在后面的课程中，我会逐一进行详细讲解。</p>
<p>作为缓存组件，Redis 的最大优势是支持丰富的数据类型。目前，Redis 支持 8 种核心数据类型，包括 string、list、set、sorted set、hash、bitmap、geo、hyperloglog。</p>
<p>Redis 的所有内存数据结构都存在全局的 dict 字典中，dict 类似 Memcached 的 hashtable。Redis 的 dict 也有 2 个哈希表，插入新 key 时，一般用 0 号哈希表，随着 key 的插入或删除，当 0 号哈希表的 keys 数大于哈希表桶数，或 kyes 数小于哈希桶的 1/10 时，就对 hash 表进行扩缩。dict 中，哈希表解决冲突的方式，与 Memcached 相同，也是使用桶内单链表，来指向多个 hash 相同的 key/value 数据。</p>
<h6>Redis 高性能</h6>
<p>Redis 一般被看作单进程/单线程组件，因为 Redis 的网络 IO 和命令处理，都在核心进程中由单线程处理。Redis 基于 Epoll 事件模型开发，可以进行非阻塞网络 IO，同时由于单线程命令处理，整个处理过程不存在竞争，不需要加锁，没有上下文切换开销，所有数据操作都是在内存中操作，所以 Redis 的性能很高，单个实例即可以达到 10w 级的 QPS。核心线程除了负责网络 IO 及命令处理外，还负责写数据到缓冲，以方便将最新写操作同步到 AOF、slave。</p>
<p>除了主进程，Redis 还会 fork 一个子进程，来进行重负荷任务的处理。Redis fork 子进程主要有 3 种场景。</p>
<ul>
<li>收到 bgrewriteaof 命令时，Redis 调用 fork，构建一个子进程，子进程往临时 AOF文件中，写入重建数据库状态的所有命令，当写入完毕，子进程则通知父进程，父进程把新增的写操作也追加到临时 AOF 文件，然后将临时文件替换老的 AOF 文件，并重命名。</li>
<li>收到 bgsave 命令时，Redis 构建子进程，子进程将内存中的所有数据通过快照做一次持久化落地，写入到 RDB 中。</li>
<li>当需要进行全量复制时，master 也会启动一个子进程，子进程将数据库快照保存到 RDB 文件，在写完 RDB 快照文件后，master 就会把 RDB 发给 slave，同时将后续新的写指令都同步给 slave。</li>
</ul>
<p><img src="assets/CgotOV2lPF-AZtVrAABZ5Cio_aE709.png" alt="img" /></p>
<p>主进程中，除了主线程处理网络 IO 和命令操作外，还有 3 个辅助 BIO 线程。这 3 个 BIO 线程分别负责处理，文件关闭、AOF 缓冲数据刷新到磁盘，以及清理对象这三个任务队列。</p>
<p>Redis 在启动时，会同时启动这三个 BIO 线程，然后 BIO 线程休眠等待任务。当需要执行相关类型的后台任务时，就会构建一个 bio_job 结构，记录任务参数，然后将 bio_job 追加到任务队列尾部。然后唤醒 BIO 线程，即可进行任务执行。</p>
<h6>Redis 持久化</h6>
<p>Redis 的持久化是通过 RDB 和 AOF 文件进行的。RDB 只记录某个时间点的快照，可以通过设置指定时间内修改 keys 数的阀值，超过则自动构建 RDB 内容快照，不过线上运维，一般会选择在业务低峰期定期进行。RDB 存储的是构建时刻的数据快照，内存数据一旦落地，不会理会后续的变更。而 AOF，记录是构建整个数据库内容的命令，它会随着新的写操作不断进行追加操作。由于不断追加，AOF 会记录数据大量的中间状态，AOF 文件会变得非常大，此时，可以通过 bgrewriteaof 指令，对 AOF 进行重写，只保留数据的最后内容，来大大缩减 AOF 的内容。</p>
<p><img src="assets/CgoB5l2lPF-AAIcAAAAhBE0bnp4350.png" alt="img" /></p>
<p>为了提升系统的可扩展性，提升读操作的支撑能力，Redis 支持 master-slave 的复制功能。当 Redis 的 slave 部署并设置完毕后，slave 会和 master 建立连接，进行全量同步。</p>
<p>第一次建立连接，或者长时间断开连接后，缺失的指令超过 master 复制缓冲区的大小，都需要先进行一次全量同步。全量同步时，master 会启动一个子进程，将数据库快照保存到文件中，然后将这个快照文件发给 slave，同时将快照之后的写指令也同步给 slave。</p>
<p>全量同步完成后，如果 slave 短时间中断，然后重连复制，缺少的写指令长度小于 master 的复制缓冲大小，master 就会把 slave 缺失的内容全部发送给 slave，进行增量复制。</p>
<p>Redis 的 master 可以挂载多个 slave，同时 slave 还可以继续挂载 slave，通过这种方式，可以有效减轻 master 的压力，同时在 master 挂掉后，可以在 slave 通过 slaveof no one 指令，使当前 slave 停止与 master 的同步，转而成为新的 master。</p>
<h6>Redis 集群管理</h6>
<p>Redis 的集群管理有 3 种方式。</p>
<ul>
<li>client 分片访问，client 对 key 做 hash，然后按取模或一致性 hash，把 key 的读写分散到不同的 Redis 实例上。</li>
<li>在 Redis 前加一个 proxy，把路由策略、后端 Redis 状态维护的工作都放到 proxy 中进行，client 直接访问 proxy，后端 Redis 变更，只需修改 proxy 配置即可。</li>
<li>直接使用 Redis cluster。Redis 创建之初，使用方直接给 Redis 的节点分配 slot，后续访问时，对 key 做 hash 找到对应的 slot，然后访问 slot 所在的 Redis 实例。在需要扩容缩容时，可以在线通过 cluster setslot 指令，以及 migrate 指令，将 slot 下所有 key 迁移到目标节点，即可实现扩缩容的目的。</li>
</ul>
<p>至此，Redis 的基本原理就讲完了，相信你对 Redis 应该有了一个大概的了解。接下来，我将开始逐一深入分析 Redis 的各个技术细节。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="15&#32;如何深入理解、应用及扩展&#32;Twemproxy？.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="17&#32;如何理解、选择并使用Redis的核心数据类型？.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b433d310b2c70ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
            document.getElementById("tip").innerHTML = "<a href='https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/300%E5%88%86%E9%92%9F%E5%90%83%E9%80%8F%E5%88%86%E5%B8%83%E5%BC%8F%E7%BC%93%E5%AD%98-%E5%AE%8C/&quot;&#32;+&#32;cookie&#32;+&#32;&quot;'>跳转到上次进度</a>"
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
