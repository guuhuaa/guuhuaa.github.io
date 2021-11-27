<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>18  如何用硬件同步原语（CAS）替代锁？.md</title>
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

                    
                    <a href="15&#32;&#32;Kafka如何实现高性能IO？.md">15  Kafka如何实现高性能IO？.md</a>

                </li>
                <li>

                    
                    <a href="16&#32;&#32;缓存策略：如何使用缓存来减少磁盘IO？.md">16  缓存策略：如何使用缓存来减少磁盘IO？.md</a>

                </li>
                <li>

                    
                    <a href="17&#32;&#32;如何正确使用锁保护共享数据，协调异步线程？.md">17  如何正确使用锁保护共享数据，协调异步线程？.md</a>

                </li>
                <li>

                    <a class="current-tab" href="18&#32;&#32;如何用硬件同步原语（CAS）替代锁？.md">18  如何用硬件同步原语（CAS）替代锁？.md</a>
                    

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
                        <div><h1>18  如何用硬件同步原语（CAS）替代锁？</h1>
<p>你好，我是李玥。上节课，我们一起学习了如何使用锁来保护共享资源，你也了解到，使用锁是有一定性能损失的，并且，如果发生了过多的锁等待，将会非常影响程序的性能。</p>
<p>在一些特定的情况下，我们可以使用硬件同步原语来替代锁，可以保证和锁一样的数据安全性，同时具有更好的性能。</p>
<p>在今年的 NSDI（NSDI 是 USENIX 组织开办的关于网络系统设计的著名学术会议）上，伯克利大学发表了一篇论文《<a href="https://www.usenix.org/conference/nsdi19/presentation/khandelwal">Confluo: Distributed Monitoring and Diagnosis Stack for High-speed Networks</a>》，这个论文中提到的 Confluo，也是一个类似于消息队列的流数据存储，它的吞吐量号称是 Kafka 的 4～10 倍。对于这个实验结论我个人不是很认同，因为它设计的实验条件对 Kafka 来说不太公平。但不可否认的是，Confluo 它的这个设计思路是一个创新，并且实际上它的性能也非常好。</p>
<p>Confluo 是如何做到这么高的吞吐量的呢？这里面非常重要的一个创新的设计就是，它使用硬件同步原语来代替锁，在一个日志上（你可以理解为消息队列中的一个队列或者分区），保证严格顺序的前提下，实现了多线程并发写入。</p>
<p>今天，我们就来学习一下，如何用硬件同步原语（CAS）替代锁？</p>
<h2>什么是硬件同步原语？</h2>
<p>为什么硬件同步原语可以替代锁呢？要理解这个问题，你要首先知道硬件同步原语是什么。</p>
<p>硬件同步原语（Atomic Hardware Primitives）是由计算机硬件提供的一组原子操作，我们比较常用的原语主要是 CAS 和 FAA 这两种。</p>
<p>CAS（Compare and Swap），它的字面意思是：先比较，再交换。我们看一下 CAS 实现的伪代码：</p>
<pre><code>&lt;&lt; atomic &gt;&gt;
function cas(p : pointer to int, old : int, new : int) returns bool {
    if *p ≠ old {
        return false
    }
    *p ← new
    return true
}
</code></pre>
<p>它的输入参数一共有三个，分别是：</p>
<ul>
<li>p: 要修改的变量的指针。</li>
<li>old: 旧值。</li>
<li>new: 新值。</li>
</ul>
<p>返回的是一个布尔值，标识是否赋值成功。</p>
<p>通过这个伪代码，你就可以看出 CAS 原语的逻辑，非常简单，就是先比较一下变量 p 当前的值是不是等于 old，如果等于，那就把变量 p 赋值为 new，并返回 true，否则就不改变变量 p，并返回 false。</p>
<p>这是 CAS 这个原语的语义，接下来我们看一下 FAA 原语（Fetch and Add）：</p>
<pre><code>&lt;&lt; atomic &gt;&gt;
function faa(p : pointer to int, inc : int) returns int {
    int value &lt;- *location
    *p &lt;- value + inc
    return value
}
</code></pre>
<p>FAA 原语的语义是，先获取变量 p 当前的值 value，然后给变量 p 增加 inc，最后返回变量 p 之前的值 value。</p>
<p>讲到这儿估计你会问，这两个原语到底有什么特殊的呢？</p>
<p>上面的这两段伪代码，如果我们用编程语言来实现，肯定是无法保证原子性的。而原语的特殊之处就是，它们都是由计算机硬件，具体说就是 CPU 提供的实现，可以保证操作的原子性。</p>
<p>我们知道，<strong>原子操作具有不可分割性，也就不存在并发的问题</strong>。所以在某些情况下，原语可以用来替代锁，实现一些即安全又高效的并发操作。</p>
<p>CAS 和 FAA 在各种编程语言中，都有相应的实现，可以来直接使用，无论你是使用哪种编程语言，它们底层的实现是一样的，效果也是一样的。</p>
<p>接下来，还是拿我们熟悉的账户服务来举例说明一下，看看如何使用 CAS 原语来替代锁，实现同样的安全性。</p>
<h2>CAS 版本的账户服务</h2>
<p>假设我们有一个共享变量 balance，它保存的是当前账户余额，然后我们模拟多个线程并发转账的情况，看一下如何使用 CAS 原语来保证数据的安全性。</p>
<p>这次我们使用 Go 语言来实现这个转账服务。先看一下使用锁实现的版本：</p>
<pre><code>package main
 
import (
	&quot;fmt&quot;
	&quot;sync&quot;
)
 
func main() {
	// 账户初始值为 0 元
	var balance int32
	balance = int32(0)
	done := make(chan bool)
	// 执行 10000 次转账，每次转入 1 元
	count := 10000
 
	var lock sync.Mutex
 
	for i := 0; i &lt; count; i++ {
		// 这里模拟异步并发转账
		go transfer(&amp;balance, 1, done, &amp;lock)
	}
	// 等待所有转账都完成
	for i := 0; i &lt; count; i++ {
		&lt;-done
	}
	// 打印账户余额
	fmt.Printf(&quot;balance = %d \n&quot;, balance)
}
// 转账服务
func transfer(balance *int32, amount int, done chan bool, lock *sync.Mutex) {
	lock.Lock()
	*balance = *balance + int32(amount)
	lock.Unlock()
	done &lt;- true
}
</code></pre>
<p>这个例子中，我们让账户的初始值为 0，然后启动多个协程来并发执行 10000 次转账，每次往账户中转入 1 元，全部转账执行完成后，账户中的余额应该正好是 10000 元。</p>
<p>如果你没接触过 Go 语言，不了解协程也没关系，你可以简单地把它理解为进程或者线程都可以，这里我们只是希望能异步并发执行转账，我们并不关心这几种“程”他们之间细微的差别。</p>
<p>这个使用锁的版本，反复多次执行，每次 balance 的结果都正好是 10000，那这段代码的安全性是没问题的。接下来我们看一下，使用 CAS 原语的版本。</p>
<pre><code>func transferCas(balance *int32, amount int, done chan bool) {
	for {
		old := atomic.LoadInt32(balance)
		new := old + int32(amount)
		if atomic.CompareAndSwapInt32(balance, old, new) {
			break
		}
	}
	done &lt;- true
}
</code></pre>
<p>这个 CAS 版本的转账服务和上面使用锁的版本，程序的总体结构是一样的，主要的区别就在于，“异步给账户余额 +1”这一小块儿代码的实现。</p>
<p>那在使用锁的版本中，需要先获取锁，然后变更账户的值，最后释放锁，完成一次转账。我们可以看一下使用 CAS 原语的实现：</p>
<p>首先，它用 for 来做了一个没有退出条件的循环。在这个循环的内部，反复地调用 CAS 原语，来尝试给账户的余额 +1。先取得账户当前的余额，暂时存放在变量 old 中，再计算转账之后的余额，保存在变量 new 中，然后调用 CAS 原语来尝试给变量 balance 赋值。我们刚刚讲过，CAS 原语它的赋值操作是有前置条件的，只有变量 balance 的值等于 old 时，才会将 balance 赋值为 new。</p>
<p>我们在 for 循环中执行了 3 条语句，在并发的环境中执行，这里面会有两种可能情况：</p>
<p>一种情况是，执行到第 3 条 CAS 原语时，没有其他线程同时改变了账户余额，那我们是可以安全变更账户余额的，这个时候执行 CAS 的返回值一定是 true，转账成功，就可以退出循环了。并且，CAS 这一条语句，它是一个原子操作，赋值的安全性是可以保证的。</p>
<p>另外一种情况，那就是在这个过程中，有其他线程改变了账户余额，这个时候是无法保证数据安全的，不能再进行赋值。执行 CAS 原语时，由于无法通过比较的步骤，所以不会执行赋值操作。本次尝试转账失败，当前线程并没有对账户余额做任何变更。由于返回值为 false，不会退出循环，所以会继续重试，直到转账成功退出循环。</p>
<p>这样，每一次转账操作，都可以通过若干次重试，在保证安全性的前提下，完成并发转账操作。</p>
<p>其实，对于这个例子，还有更简单、性能更好的方式：那就是，直接使用 FAA 原语。</p>
<pre><code>func transferFaa(balance *int32, amount int, done chan bool) {
	atomic.AddInt32(balance, int32(amount))
	done &lt;- true
}
</code></pre>
<p>FAA 原语它的操作是，获取变量当前的值，然后把它做一个加法，并且保证这个操作的原子性，一行代码就可以搞定了。看到这儿，你可能会想，那 CAS 原语还有什么意义呢？</p>
<p>在这个例子里面，肯定是使用 FAA 原语更合适，但是我们上面介绍的，使用 CAS 原语的方法，它的适用范围更加广泛一些。类似于这样的逻辑：先读取数据，做计算，然后更新数据，无论这个计算是什么样的，都可以使用 CAS 原语来保护数据安全，但是 FAA 原语，这个计算的逻辑只能局限于简单的加减法。所以，我们上面讲的这种使用 CAS 原语的方法并不是没有意义的。</p>
<p>另外，你需要知道的是，这种使用 CAS 原语反复重试赋值的方法，它是比较耗费 CPU 资源的，因为在 for 循环中，如果赋值不成功，是会立即进入下一次循环没有等待的。如果线程之间的碰撞非常频繁，经常性的反复重试，这个重试的线程会占用大量的 CPU 时间，随之系统的整体性能就会下降。</p>
<p>缓解这个问题的一个方法是使用 Yield()， 大部分编程语言都支持 Yield() 这个系统调用，Yield() 的作用是，告诉操作系统，让出当前线程占用的 CPU 给其他线程使用。每次循环结束前调用一下 Yield() 方法，可以在一定程度上减少 CPU 的使用率，缓解这个问题。你也可以在每次循环结束之后，Sleep() 一小段时间，但是这样做的代价是，性能会严重下降。</p>
<p>所以，这种方法它只适合于线程之间碰撞不太频繁，也就是说绝大部分情况下，执行 CAS 原语不需要重试这样的场景。</p>
<h2>小结</h2>
<p>这节课我们一起学习了 CAS 和 FAA 这两个原语。这些原语，是由 CPU 提供的原子操作，在并发环境中，单独使用这些原语不用担心数据安全问题。在特定的场景中，CAS 原语可以替代锁，在保证安全性的同时，提供比锁更好的性能。</p>
<p>接下来，我们用转账服务这个例子，分别演示了 CAS 和 FAA 这两个原语是如何替代锁来使用的。对于类似：“先读取数据，做计算，然后再更新数据”这样的业务逻辑，可以使用 CAS 原语 + 反复重试的方式来保证数据安全，前提是，线程之间的碰撞不能太频繁，否则太多重试会消耗大量的 CPU 资源，反而得不偿失。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="17&#32;&#32;如何正确使用锁保护共享数据，协调异步线程？.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="19&#32;&#32;数据压缩：时间换空间的游戏.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b4356669bb3645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
