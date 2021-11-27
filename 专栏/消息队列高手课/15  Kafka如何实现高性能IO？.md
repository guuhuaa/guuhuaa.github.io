<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>15  Kafka如何实现高性能IO？.md</title>
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

                    
                    <a href="00&#32;开篇词&#32;&#32;优秀的程序员，你的技术栈中不能只有“增删改查”.md">00 开篇词  优秀的程序员，你的技术栈中不能只有“增删改查”.md</a>

                </li>
                <li>

                    
                    <a href="00&#32;预习&#32;&#32;怎样更好地学习这门课？.md">00 预习  怎样更好地学习这门课？.md</a>

                </li>
                <li>

                    
                    <a href="01&#32;&#32;为什么需要消息队列？.md">01  为什么需要消息队列？.md</a>

                </li>
                <li>

                    
                    <a href="02&#32;&#32;该如何选择消息队列？.md">02  该如何选择消息队列？.md</a>

                </li>
                <li>

                    
                    <a href="03&#32;&#32;消息模型：主题和队列有什么区别？.md">03  消息模型：主题和队列有什么区别？.md</a>

                </li>
                <li>

                    
                    <a href="04&#32;&#32;如何利用事务消息实现分布式事务？.md">04  如何利用事务消息实现分布式事务？.md</a>

                </li>
                <li>

                    
                    <a href="05&#32;&#32;如何确保消息不会丢失.md">05  如何确保消息不会丢失.md</a>

                </li>
                <li>

                    
                    <a href="06&#32;&#32;如何处理消费过程中的重复消息？.md">06  如何处理消费过程中的重复消息？.md</a>

                </li>
                <li>

                    
                    <a href="07&#32;&#32;消息积压了该如何处理？.md">07  消息积压了该如何处理？.md</a>

                </li>
                <li>

                    
                    <a href="08&#32;&#32;答疑解惑（一）&#32;&#32;网关如何接收服务端的秒杀结果？.md">08  答疑解惑（一）  网关如何接收服务端的秒杀结果？.md</a>

                </li>
                <li>

                    
                    <a href="09&#32;&#32;学习开源代码该如何入手？.md">09  学习开源代码该如何入手？.md</a>

                </li>
                <li>

                    
                    <a href="10&#32;&#32;如何使用异步设计提升系统性能？.md">10  如何使用异步设计提升系统性能？.md</a>

                </li>
                <li>

                    
                    <a href="11&#32;&#32;如何实现高性能的异步网络传输？.md">11  如何实现高性能的异步网络传输？.md</a>

                </li>
                <li>

                    
                    <a href="12&#32;&#32;序列化与反序列化：如何通过网络传输结构化的数据？.md">12  序列化与反序列化：如何通过网络传输结构化的数据？.md</a>

                </li>
                <li>

                    
                    <a href="13&#32;&#32;传输协议：应用程序之间对话的语言.md">13  传输协议：应用程序之间对话的语言.md</a>

                </li>
                <li>

                    
                    <a href="14&#32;&#32;内存管理：如何避免内存溢出和频繁的垃圾回收？.md">14  内存管理：如何避免内存溢出和频繁的垃圾回收？.md</a>

                </li>
                <li>

                    <a class="current-tab" href="15&#32;&#32;Kafka如何实现高性能IO？.md">15  Kafka如何实现高性能IO？.md</a>
                    

                </li>
                <li>

                    
                    <a href="16&#32;&#32;缓存策略：如何使用缓存来减少磁盘IO？.md">16  缓存策略：如何使用缓存来减少磁盘IO？.md</a>

                </li>
                <li>

                    
                    <a href="17&#32;&#32;如何正确使用锁保护共享数据，协调异步线程？.md">17  如何正确使用锁保护共享数据，协调异步线程？.md</a>

                </li>
                <li>

                    
                    <a href="18&#32;&#32;如何用硬件同步原语（CAS）替代锁？.md">18  如何用硬件同步原语（CAS）替代锁？.md</a>

                </li>
                <li>

                    
                    <a href="19&#32;&#32;数据压缩：时间换空间的游戏.md">19  数据压缩：时间换空间的游戏.md</a>

                </li>
                <li>

                    
                    <a href="20&#32;&#32;RocketMQ&#32;Producer源码分析：消息生产的实现过程.md">20  RocketMQ Producer源码分析：消息生产的实现过程.md</a>

                </li>
                <li>

                    
                    <a href="21&#32;&#32;Kafka&#32;Consumer源码分析：消息消费的实现过程.md">21  Kafka Consumer源码分析：消息消费的实现过程.md</a>

                </li>
                <li>

                    
                    <a href="22&#32;&#32;Kafka和RocketMQ的消息复制实现的差异点在哪？.md">22  Kafka和RocketMQ的消息复制实现的差异点在哪？.md</a>

                </li>
                <li>

                    
                    <a href="23&#32;&#32;RocketMQ客户端如何在集群中找到正确的节点？.md">23  RocketMQ客户端如何在集群中找到正确的节点？.md</a>

                </li>
                <li>

                    
                    <a href="24&#32;&#32;Kafka的协调服务ZooKeeper：实现分布式系统的“瑞士军刀”.md">24  Kafka的协调服务ZooKeeper：实现分布式系统的“瑞士军刀”.md</a>

                </li>
                <li>

                    
                    <a href="25&#32;&#32;RocketMQ与Kafka中如何实现事务？.md">25  RocketMQ与Kafka中如何实现事务？.md</a>

                </li>
                <li>

                    
                    <a href="26&#32;&#32;MQTT协议：如何支持海量的在线IoT设备.md">26  MQTT协议：如何支持海量的在线IoT设备.md</a>

                </li>
                <li>

                    
                    <a href="27&#32;&#32;Pulsar的存储计算分离设计：全新的消息队列设计思路.md">27  Pulsar的存储计算分离设计：全新的消息队列设计思路.md</a>

                </li>
                <li>

                    
                    <a href="28&#32;&#32;答疑解惑（二）：我的100元哪儿去了？.md">28  答疑解惑（二）：我的100元哪儿去了？.md</a>

                </li>
                <li>

                    
                    <a href="29&#32;&#32;流计算与消息（一）：通过Flink理解流计算的原理.md">29  流计算与消息（一）：通过Flink理解流计算的原理.md</a>

                </li>
                <li>

                    
                    <a href="30&#32;&#32;流计算与消息（二）：在流计算中使用Kafka链接计算任务.md">30  流计算与消息（二）：在流计算中使用Kafka链接计算任务.md</a>

                </li>
                <li>

                    
                    <a href="31&#32;&#32;动手实现一个简单的RPC框架（一）：原理和程序的结构.md">31  动手实现一个简单的RPC框架（一）：原理和程序的结构.md</a>

                </li>
                <li>

                    
                    <a href="32&#32;&#32;动手实现一个简单的RPC框架（二）：通信与序列化.md">32  动手实现一个简单的RPC框架（二）：通信与序列化.md</a>

                </li>
                <li>

                    
                    <a href="33&#32;&#32;动手实现一个简单的RPC框架（三）：客户端.md">33  动手实现一个简单的RPC框架（三）：客户端.md</a>

                </li>
                <li>

                    
                    <a href="34&#32;&#32;动手实现一个简单的RPC框架（四）：服务端.md">34  动手实现一个简单的RPC框架（四）：服务端.md</a>

                </li>
                <li>

                    
                    <a href="35&#32;&#32;答疑解惑（三）：主流消息队列都是如何存储消息的？.md">35  答疑解惑（三）：主流消息队列都是如何存储消息的？.md</a>

                </li>
                <li>

                    
                    <a href="加餐&#32;&#32;JMQ的Broker是如何异步处理消息的？.md">加餐  JMQ的Broker是如何异步处理消息的？.md</a>

                </li>
                <li>

                    
                    <a href="结束语&#32;&#32;程序员如何构建知识体系？.md">结束语  程序员如何构建知识体系？.md</a>

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
                        <div><h1>15  Kafka如何实现高性能IO？</h1>
<p>你好，我是李玥。</p>
<p>Apache Kafka 是一个高性能的消息队列，在众多消息队列产品中，Kafka 的性能绝对是处于第一梯队的。我曾经在一台配置比较好的服务器上，对 Kafka 做过极限的性能压测，Kafka 单个节点的极限处理能力接近每秒钟 2000 万条消息，吞吐量达到每秒钟 600MB。</p>
<p>你可能会问，Kafka 是如何做到这么高的性能的？</p>
<p>我们在专栏“进阶篇”的前几节课，讲的知识点一直围绕着同一个主题：怎么开发一个高性能的网络应用程序。其中提到了像全异步化的线程模型、高性能的异步网络传输、自定义的私有传输协议和序列化、反序列化等等，这些方法和优化技巧，你都可以在 Kafka 的源代码中找到对应的实现。</p>
<p>在性能优化方面，除了这些通用的性能优化手段之外，Kafka 还有哪些“独门绝技”呢？</p>
<p>这节课，我来为你一一揭晓这些绝技。</p>
<h2>使用批量消息提升服务端处理能力</h2>
<p>我们知道，批量处理是一种非常有效的提升系统吞吐量的方法。在 Kafka 内部，消息都是以“批”为单位处理的。一批消息从发送端到接收端，是如何在 Kafka 中流转的呢？</p>
<p>我们先来看发送端，也就是 Producer 这一端。</p>
<p>在 Kafka 的客户端 SDK（软件开发工具包）中，Kafka 的 Producer 只提供了单条发送的 send() 方法，并没有提供任何批量发送的接口。原因是，Kafka 根本就没有提供单条发送的功能，是的，你没有看错，虽然它提供的 API 每次只能发送一条消息，但实际上，Kafka 的客户端 SDK 在实现消息发送逻辑的时候，采用了异步批量发送的机制。</p>
<p>当你调用 send() 方法发送一条消息之后，无论你是同步发送还是异步发送，Kafka 都不会立即就把这条消息发送出去。它会先把这条消息，存放在内存中缓存起来，然后选择合适的时机把缓存中的所有消息组成一批，一次性发给 Broker。简单地说，就是攒一波一起发。</p>
<p>在 Kafka 的服务端，也就是 Broker 这一端，又是如何处理这一批一批的消息呢？</p>
<p>在服务端，Kafka 不会把一批消息再还原成多条消息，再一条一条地处理，这样太慢了。Kafka 这块儿处理的非常聪明，每批消息都会被当做一个“批消息”来处理。也就是说，在 Broker 整个处理流程中，无论是写入磁盘、从磁盘读出来、还是复制到其他副本这些流程中，<strong>批消息都不会被解开，一直是作为一条“批消息”来进行处理的。</strong></p>
<p>在消费时，消息同样是以批为单位进行传递的，Consumer 从 Broker 拉到一批消息后，在客户端把批消息解开，再一条一条交给用户代码处理。</p>
<p>比如说，你在客户端发送 30 条消息，在业务程序看来，是发送了 30 条消息，而对于 Kafka 的 Broker 来说，它其实就是处理了 1 条包含 30 条消息的“批消息”而已。显然处理 1 次请求要比处理 30 次请求要快得多。</p>
<p>构建批消息和解开批消息分别在发送端和消费端的客户端完成，不仅减轻了 Broker 的压力，最重要的是减少了 Broker 处理请求的次数，提升了总体的处理能力。</p>
<p>这就是 Kafka 用批量消息提升性能的方法。</p>
<p>我们知道，相比于网络传输和内存，磁盘 IO 的速度是比较慢的。对于消息队列的服务端来说，性能的瓶颈主要在磁盘 IO 这一块。接下来我们看一下，Kafka 在磁盘 IO 这块儿做了哪些优化。</p>
<h2>使用顺序读写提升磁盘 IO 性能</h2>
<p>对于磁盘来说，它有一个特性，就是顺序读写的性能要远远好于随机读写。在 SSD（固态硬盘）上，顺序读写的性能要比随机读写快几倍，如果是机械硬盘，这个差距会达到几十倍。为什么呢？</p>
<p>操作系统每次从磁盘读写数据的时候，需要先寻址，也就是先要找到数据在磁盘上的物理位置，然后再进行数据读写。如果是机械硬盘，这个寻址需要比较长的时间，因为它要移动磁头，这是个机械运动，机械硬盘工作的时候会发出咔咔的声音，就是移动磁头发出的声音。</p>
<p>顺序读写相比随机读写省去了大部分的寻址时间，它只要寻址一次，就可以连续地读写下去，所以说，性能要比随机读写要好很多。</p>
<p>Kafka 就是充分利用了磁盘的这个特性。它的存储设计非常简单，对于每个分区，它把从 Producer 收到的消息，顺序地写入对应的 log 文件中，一个文件写满了，就开启一个新的文件这样顺序写下去。消费的时候，也是从某个全局的位置开始，也就是某一个 log 文件中的某个位置开始，顺序地把消息读出来。</p>
<p>这样一个简单的设计，充分利用了顺序读写这个特性，极大提升了 Kafka 在使用磁盘时的 IO 性能。</p>
<p>接下来我们说一下 Kafka 是如何实现缓存的。</p>
<h2>利用 PageCache 加速消息读写</h2>
<p>在 Kafka 中，它会利用 PageCache 加速消息读写。PageCache 是现代操作系统都具有的一项基本特性。通俗地说，PageCache 就是操作系统在内存中给磁盘上的文件建立的缓存。无论我们使用什么语言编写的程序，在调用系统的 API 读写文件的时候，并不会直接去读写磁盘上的文件，应用程序实际操作的都是 PageCache，也就是文件在内存中缓存的副本。</p>
<p>应用程序在写入文件的时候，操作系统会先把数据写入到内存中的 PageCache，然后再一批一批地写到磁盘上。读取文件的时候，也是从 PageCache 中来读取数据，这时候会出现两种可能情况。</p>
<p>一种是 PageCache 中有数据，那就直接读取，这样就节省了从磁盘上读取数据的时间；另一种情况是，PageCache 中没有数据，这时候操作系统会引发一个缺页中断，应用程序的读取线程会被阻塞，操作系统把数据从文件中复制到 PageCache 中，然后应用程序再从 PageCache 中继续把数据读出来，这时会真正读一次磁盘上的文件，这个读的过程就会比较慢。</p>
<p>用户的应用程序在使用完某块 PageCache 后，操作系统并不会立刻就清除这个 PageCache，而是尽可能地利用空闲的物理内存保存这些 PageCache，除非系统内存不够用，操作系统才会清理掉一部分 PageCache。清理的策略一般是 LRU 或它的变种算法，这个算法我们不展开讲，它保留 PageCache 的逻辑是：优先保留最近一段时间最常使用的那些 PageCache。</p>
<p>Kafka 在读写消息文件的时候，充分利用了 PageCache 的特性。一般来说，消息刚刚写入到服务端就会被消费，按照 LRU 的“优先清除最近最少使用的页”这种策略，读取的时候，对于这种刚刚写入的 PageCache，命中的几率会非常高。</p>
<p>也就是说，大部分情况下，消费读消息都会命中 PageCache，带来的好处有两个：一个是读取的速度会非常快，另外一个是，给写入消息让出磁盘的 IO 资源，间接也提升了写入的性能。</p>
<h2>ZeroCopy：零拷贝技术</h2>
<p>Kafka 的服务端在消费过程中，还使用了一种“零拷贝”的操作系统特性来进一步提升消费的性能。</p>
<p>我们知道，在服务端，处理消费的大致逻辑是这样的：</p>
<ul>
<li>首先，从文件中找到消息数据，读到内存中；</li>
<li>然后，把消息通过网络发给客户端。</li>
</ul>
<p>这个过程中，数据实际上做了 2 次或者 3 次复制：</p>
<ol>
<li>从文件复制数据到 PageCache 中，如果命中 PageCache，这一步可以省掉；</li>
<li>从 PageCache 复制到应用程序的内存空间中，也就是我们可以操作的对象所在的内存；</li>
<li>从应用程序的内存空间复制到 Socket 的缓冲区，这个过程就是我们调用网络应用框架的 API 发送数据的过程。</li>
</ol>
<p>Kafka 使用零拷贝技术可以把这个复制次数减少一次，上面的 2、3 步骤两次复制合并成一次复制。直接从 PageCache 中把数据复制到 Socket 缓冲区中，这样不仅减少一次数据复制，更重要的是，由于不用把数据复制到用户内存空间，DMA 控制器可以直接完成数据复制，不需要 CPU 参与，速度更快。</p>
<p>下面是这个零拷贝对应的系统调用：</p>
<pre><code>#include &lt;sys/socket.h&gt;
ssize_t sendfile(int out_fd, int in_fd, off_t *offset, size_t count);
</code></pre>
<p>它的前两个参数分别是目的端和源端的文件描述符，后面两个参数是源端的偏移量和复制数据的长度，返回值是实际复制数据的长度。</p>
<p>如果你遇到这种从文件读出数据后再通过网络发送出去的场景，并且这个过程中你不需要对这些数据进行处理，那一定要使用这个零拷贝的方法，可以有效地提升性能。</p>
<h2>小结</h2>
<p>这节课，我们总结了 Kafka 的高性能设计中的几个关键的技术点：</p>
<ul>
<li>使用批量处理的方式来提升系统吞吐能力。</li>
<li>基于磁盘文件高性能顺序读写的特性来设计的存储结构。</li>
<li>利用操作系统的 PageCache 来缓存数据，减少 IO 并提升读性能。</li>
<li>使用零拷贝技术加速消费流程。</li>
</ul>
<p>以上这些，就是 Kafka 之所以能做到如此高性能的关键技术点。你可以看到，要真正实现一个高性能的消息队列，是非常不容易的，你需要熟练掌握非常多的编程语言和操作系统的底层技术。</p>
<p>这些优化的方法和技术，同样可以用在其他适合的场景和应用程序中。我希望你能充分理解这几项优化技术的原理，知道它们在什么情况下适用，什么情况下不适用。这样，当你遇到合适场景的时候，再深入去学习它的细节用法，最终就能把它真正地用到你开发的程序中。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="14&#32;&#32;内存管理：如何避免内存溢出和频繁的垃圾回收？.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="16&#32;&#32;缓存策略：如何使用缓存来减少磁盘IO？.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b4356564bfe645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
            document.getElementById("tip").innerHTML = "<a href='https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/%E6%B6%88%E6%81%AF%E9%98%9F%E5%88%97%E9%AB%98%E6%89%8B%E8%AF%BE/&quot;&#32;+&#32;cookie&#32;+&#32;&quot;'>跳转到上次进度</a>"
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
