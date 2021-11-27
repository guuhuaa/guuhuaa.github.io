<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>16 我为什么与众不同 - TCP高级篇（拥塞模型）.md</title>
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

                    
                    <a href="01&#32;我应该站在谁的肩膀上&#32;-&#32;OSI&#32;vs&#32;TCPIP模型.md">01 我应该站在谁的肩膀上 - OSI vs TCPIP模型.md</a>

                </li>
                <li>

                    
                    <a href="https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/%E5%85%A8%E8%A7%A3%E7%BD%91%E7%BB%9C%E5%8D%8F%E8%AE%AE/02%20%E4%B8%87%E4%B8%88%E9%AB%98%E6%A5%BC%E5%B9%B3%E5%9C%B0%E8%B5%B7-%20%E7%89%A9%E7%90%86%E5%B1%82%20+%20%E6%95%B0%E6%8D%AE%E9%93%BE%E8%B7%AF%E5%B1%82.md">02 万丈高楼平地起- 物理层 + 数据链路层.md</a>

                </li>
                <li>

                    
                    <a href="03&#32;OSI的灵魂就是我&#32;-&#32;网络层.md">03 OSI的灵魂就是我 - 网络层.md</a>

                </li>
                <li>

                    
                    <a href="04&#32;要快还是要稳你说好了&#32;-&#32;传输层.md">04 要快还是要稳你说好了 - 传输层.md</a>

                </li>
                <li>

                    
                    <a href="05&#32;是时候展现真正的技术了&#32;-&#32;应用层.md">05 是时候展现真正的技术了 - 应用层.md</a>

                </li>
                <li>

                    
                    <a href="06&#32;重回小学课堂&#32;-&#32;二进制101.md">06 重回小学课堂 - 二进制101.md</a>

                </li>
                <li>

                    
                    <a href="https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/%E5%85%A8%E8%A7%A3%E7%BD%91%E7%BB%9C%E5%8D%8F%E8%AE%AE/07%201+1%20=%202%E5%90%97%EF%BC%9F%20-%20%E4%BA%8C%E8%BF%9B%E5%88%B6%E7%9A%84%E8%AE%A1%E7%AE%97.md">07 1+1 = 2吗？ - 二进制的计算.md</a>

                </li>
                <li>

                    
                    <a href="08&#32;16进制又是个什么鬼？&#32;-&#32;16进制的讲解.md">08 16进制又是个什么鬼？ - 16进制的讲解.md</a>

                </li>
                <li>

                    
                    <a href="09&#32;我想有个家&#32;-&#32;什么是IP地址.md">09 我想有个家 - 什么是IP地址.md</a>

                </li>
                <li>

                    
                    <a href="10&#32;我可是住二环的人&#32;-&#32;IP地址的组成和分类.md">10 我可是住二环的人 - IP地址的组成和分类.md</a>

                </li>
                <li>

                    
                    <a href="11&#32;我已经没地方住了吗&#32;-&#32;IPv6.md">11 我已经没地方住了吗 - IPv6.md</a>

                </li>
                <li>

                    
                    <a href="12&#32;向左还是向右&#32;-&#32;IP路由.md">12 向左还是向右 - IP路由.md</a>

                </li>
                <li>

                    
                    <a href="13&#32;我能给你安全感&#32;-&#32;TCP（一）.md">13 我能给你安全感 - TCP（一）.md</a>

                </li>
                <li>

                    
                    <a href="14&#32;我那不为人知的秘密是什么&#32;-&#32;TCP（二）.md">14 我那不为人知的秘密是什么 - TCP（二）.md</a>

                </li>
                <li>

                    
                    <a href="15&#32;不问收没收到，就问快不快&#32;-&#32;UDP.md">15 不问收没收到，就问快不快 - UDP.md</a>

                </li>
                <li>

                    <a class="current-tab" href="16&#32;我为什么与众不同&#32;-&#32;TCP高级篇（拥塞模型）.md">16 我为什么与众不同 - TCP高级篇（拥塞模型）.md</a>
                    

                </li>
                <li>

                    
                    <a href="17&#32;来，先看看我的家谱&#32;-&#32;HTTP的身世.md">17 来，先看看我的家谱 - HTTP的身世.md</a>

                </li>
                <li>

                    
                    <a href="18&#32;我都这么成功了，你却说我不行&#32;-&#32;HTTP&#32;的特点和缺点.md">18 我都这么成功了，你却说我不行 - HTTP 的特点和缺点.md</a>

                </li>
                <li>

                    
                    <a href="19&#32;我老了，让我儿子来吧&#32;-&#32;HTTP2.md">19 我老了，让我儿子来吧 - HTTP2.md</a>

                </li>
                <li>

                    
                    <a href="20&#32;稳重的大外甥&#32;-&#32;HTTPS.md">20 稳重的大外甥 - HTTPS.md</a>

                </li>
                <li>

                    
                    <a href="21&#32;HTTP的高级篇&#32;-&#32;HTTPClient（Java）.md">21 HTTP的高级篇 - HTTPClient（Java）.md</a>

                </li>
                <li>

                    
                    <a href="22&#32;想来我家，你自己查呀&#32;-&#32;DNS.md">22 想来我家，你自己查呀 - DNS.md</a>

                </li>
                <li>

                    
                    <a href="23&#32;来的早，不如来得巧&#32;-&#32;NAT.md">23 来的早，不如来得巧 - NAT.md</a>

                </li>
                <li>

                    
                    <a href="24&#32;辛苦的邮政&#32;-&#32;SMTP.md">24 辛苦的邮政 - SMTP.md</a>

                </li>
                <li>

                    
                    <a href="25&#32;你就是看不见我&#32;-&#32;VPN.md">25 你就是看不见我 - VPN.md</a>

                </li>
                <li>

                    
                    <a href="26&#32;黑客的好帮手&#32;-&#32;SSH.md">26 黑客的好帮手 - SSH.md</a>

                </li>
                <li>

                    
                    <a href="27&#32;你可以得到我的心，却得不到我的人&#32;-&#32;物理安全设备.md">27 你可以得到我的心，却得不到我的人 - 物理安全设备.md</a>

                </li>
                <li>

                    
                    <a href="28&#32;你怎么证明你就是你&#32;-&#32;身份验证和访问控制.md">28 你怎么证明你就是你 - 身份验证和访问控制.md</a>

                </li>
                <li>

                    
                    <a href="29&#32;我要怎么藏好我的考研资料&#32;-&#32;网络攻击（一）.md">29 我要怎么藏好我的考研资料 - 网络攻击（一）.md</a>

                </li>
                <li>

                    
                    <a href="30&#32;我要怎么藏好我的考研资料&#32;-&#32;网络攻击（二）.md">30 我要怎么藏好我的考研资料 - 网络攻击（二）.md</a>

                </li>
                <li>

                    
                    <a href="31&#32;如何保护我的考研资料&#32;-&#32;网络攻击防范.md">31 如何保护我的考研资料 - 网络攻击防范.md</a>

                </li>
                <li>

                    
                    <a href="32&#32;Linux网络安全&#32;-&#32;安全实战.md">32 Linux网络安全 - 安全实战.md</a>

                </li>
                <li>

                    
                    <a href="33&#32;结语.md">33 结语.md</a>

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
                        <div><h1>16 我为什么与众不同 - TCP高级篇（拥塞模型）</h1>
<p>首先我们可以肯定的是TCP协议是可靠的。这就是我们前面讲的TCP知识。它是可靠地从网络上的一个端点到另一端点获取数据，但是它不希望使两者之间的网络不堪重负。TCP不想非常快的就开始发送数据，这样会导致拥塞和数据包丢失。同样，TCP也不想“欺负”其他的网络，把其他所有协议都淘汰掉，优先考虑自己的流量。因此，通过TCP拥塞控制，TCP能够确定网络上的拥塞并相应地调整其传输速率。</p>
<p>这可能与你想象的有一点不同。通常，我们开始传输该文件，并且我们想象的是，发送速度逐渐提高，并逐渐接近带宽。我们能够用吞吐量完全填满网络，并且该文件能够尽快通过链接传输。就像下图一样</p>
<p><img src="assets/20210206132405382.png" alt="在这里插入图片描述" /></p>
<p>但是理想很丰满，现实很骨感。下图是在Wireshark的吞吐量图。</p>
<p><img src="assets/20210206132427623.png" alt="在这里插入图片描述" /></p>
<p>从图上可以看到吞吐量的变化。最初会上升，然后略有下降。它会先恢复一段时间，然后再次下降，然后随着时间的推移缓慢重建。因此现实是，TCP不会完全填充网络，当我们将文件从一个端点传输到另一个端点时。会有很多事情来控制。造成这种情况的原因是，TCP被设计为在端点之间具有不可预测的网络的情况下非常智能，现实也确实如此。今天，我们正在处理无线，高延迟，高损耗，多路径，高拥塞的情况。因此，这两个端点需要确定它们之间网络中正在发生的事情，并尽其最大可能地填充它，并以最有效的方式将数据从A点移动到B点。而TCP正是通过拥塞机制来进行控制的。这也是为什么它很重要的原因。</p>
<h3>拥塞窗口</h3>
<p>让我们想象一下，在客户端，我们有一个大小限制为65535的TCP接收窗口。那么，无论中间的网络大小如何，发送方都只能一次将65535放到网络中传输。现在，如果我们不传输大量数据或处于非常低的延迟环境中（例如端点之间为1毫秒），则接收窗口可能是足够的。但是，如果我们试图通过高延迟的链接来传送大量数据，窗口接收的数据量也不会减少。但是无论哪种方式，发送者都受到接收窗口的限制。这是拥塞窗口起作用的地方。</p>
<p>让我们想象一下，客户端的接收窗口现在大大增加到1GB。那么使用的是1GB的接收窗口。客户端很自信的堆服务器说：“嘿，服务器，给我你所有的东西，我能处理。你最多可以发送1GB的未确认数据。但是在这里发件人需要做出决定，也就是思考一下。在引起拥塞问题之前，它将在网络上发送多少，是1GB吗还是512MB还是10Kb？该服务器知道还有其他TCP连接和使用。它知道并非所有链接都相同。因此，该服务器不知道中间是哪种网络。我们有穿越海洋的T1连接吗？这两个端点之间是否有卫星连接？还是说客户端只是一个交换机端口？所以最开始的时候，服务器不知道一次发送多少，并且它不希望引起流量问题并引起争用和拥塞，这将导致数据包丢失。因此，该服务器可以传输的数据量是拥塞窗口或接收窗口的最小值。哪个值较小，就使用哪个值。我们的这个例子，接收器有很大很大的接收窗口。除非我们之间有一个非常非常牢固的网络，否则我们不可能在拥塞窗口实现这一目标。这里变得有些意思了。TCP接收窗口的大小会在TCP的头中。还记得上一节讲的TCP Header中有一个Window Size吗？</p>
<p><img src="assets/20210206132443225.png" alt="在这里插入图片描述" /></p>
<p>因此，当工作站发送确认甚至数据包时，它总是会告诉你必须使用多少窗口大小。在上面照片中，可以看到实际的真实窗口大小值为262，但由于我们使用的是窗口缩放，所以实际上是一个更大的值。在这里我们可以看到对方可以一次发送33536。这个不是问题，因为我们在接收缓冲区中可以拥有的数据量。我们永远不会在包头中看到它。实际上，挖掘并找出实际值是什么，几乎是不可能的。原因之一是因为这个数字一直在变。TCP总是增加拥塞窗口或减少拥塞窗口，这取决于它从网络之间确定的结果。因此，我们能做的最好的就是查看该拥塞窗口，并确定这是吞吐量缓慢问题的根本原因吗？</p>
<h3>拥塞算法</h3>
<p>我们知道了拥塞控制机制是什么，让我们一起来看一些算法及其工作原理。TCP拥塞控制机制决定发送方如何使用网络上的带宽。还可以决定该设备遇到丢失或高延迟时将退后并恢复的速度。现在让我们来看一些拥塞控制算法的名字？也许你以前听说过其中一些。比如vegas，Reno，NewReno，CUBIC等等。有很多不同的算法。随着时间的流逝和网络的变化，我们发现它们已经经过调整和优化，可以在不同类型的网络上更好地运行。例如，当网络具有更高的带宽和更高的延迟（跨过海洋下面的40GB连接通道）时，我们开始意识到需要对TCP发送算法进行更改，可能需要使它们更具“攻击性”，而不必仅仅因为丢失一个数据包就减缓传输的速度。同样，一些常见的拥塞控制算法，取决于操作系统，使用的TCP版本，安装的补丁程序，这些都会对使用哪种算法产生影响。我们来更深入地了解一下这些算法为何不同。</p>
<p>聊这些算法之前，你自己先想一下都需要考虑什么？第一个想到的核心组成部分是不是初始窗口大小（这个是不是很重要，小了，会慢，大了，会丢失）。初始窗口就是发送方在传输文件时立即发出的完整MSS(Maximum segment size）数据包的大小。假设我们的服务器使用的是非常保守的拥塞控制机制，它一次只发送两个全尺寸数据包。在发送更多数据之前，它会等待这些数据包的确认返回，返回后，将可以继续发送更多内容。初始窗口大小的决定，网络上发出了多少个数据包，这些都取决于拥塞控制机制的使用。</p>
<p><img src="assets/20210206132459970.png" alt="在这里插入图片描述" /></p>
<p>比如在NewReno的某些实现中，开始的窗口大小是四个MSS大小的数据包，这是初始窗口设置。在许多CUBIC算法的实现中，使用10个MSS作为初始窗口。初始窗口是拥塞算法的核心，这表示的是最开始发送多少数据包。</p>
<p>拥塞机制的另一个核心组件是慢启动。什么意思呢？就是我们的服务器，它发送两个完整的MSS到客户端，然后从客户端收到确认，整个过程很顺畅。然后再测量一下在发送数据和接收确认之间的等待时间，服务器会认为整个流程没有问题。之后服务器会将下次发送的MSS数量翻倍，，它将在下一次发送四个MSS，然后等待这些确认返回。重复上面流程，如果还是很顺畅，会继续的将发出的数据包数量加倍。这是一种常见的机制，你会在Reno和NewReno等一些较旧的算法中看到这种机制。</p>
<p><img src="assets/20210206132520678.png" alt="在这里插入图片描述" /></p>
<h5>慢启动</h5>
<p>我们来详细看一下慢启动的过程。</p>
<p><img src="assets/20210206132535571.png" alt="在这里插入图片描述" /></p>
<p>在我们的图表中，我们可以看到，时间是底部X轴表示往返时间，Y轴表示发送包的数量。发送站通过发送两个完整的MSS来启动。它等待第一次网络往返的确认返回，然后将拥塞窗口加倍，接下来将为第二次往返发送四个MSS。如果这些都出去了，那么认为没有任何问题，那么我们将再次加倍，第三次网络往返传输将获得8个MSS。如果所有这些都被成功接收，并且我们收到了很好的回覆，继续再次加倍。现在，在某个时候，根据算法以及该算法能够从网络中确定的延迟时间，该算法将设置一个慢启动阈值（图中的1），这意味着你可以将网络上现有的MSS数量加倍直到碰到这一点。在这种情况下，我们说该数量为16。在那之后，我们从慢启动机制更改为避免拥塞机制。这就是说，对于每个网络往返，我们将只添加一个，而不是将网络上的MSS数量加倍。因此，对于第五次网络往返，我们将有17个MSS（也就是16 + 1）。对于第6次网络往返，我们将有18个MSS（17 + 1），这将缓慢增加拥塞窗口，直到遇到丢包或拥塞为止（图中的2）。当我们遇到超时或发送数据包却没有收到响应时会发生什么？这时候，大多数拥塞控制算法所采用的是让步。（在较早的日子里，这个数字实际上会回到一半）。将拥堵窗口缩小一半（图3），然后从慢启动重新开始，直到再次达到慢启动阈值。但是，随着时间的流逝，网络连接的带宽不断提高，在某些情况下，延迟也有所增加，这种倍增的后退策略有点激进了。就像我们在这里看到的那样，仅由于遇到单个数据包丢失，我们就损失一半的吞吐量。</p>
<p><img src="assets/20210206132552652.png" alt="在这里插入图片描述" /> 因此，为了解决此问题，使用了另一个核心组件那就是-快速恢复。快速恢复可以帮助我们做的是，我们从拥挤窗口中的那个高点退回，但并不是一半的腰斩。而是退后一点然后再慢慢重建。</p>
<p>我们前面提到了，使用哪种拥塞控制算法取决了很多事情？初始窗口，最初发出了多少个MSS？是否使用慢启动机制，还是快速启动？慢启动阈值如何设置？什么时候开始避免拥堵？是否使用快速恢复？还是如果遇到一些损失，会重新回到慢速启动？我们是否只会在看到数据包丢失的情况下才后退，还是等待时间的变化会导致我们放慢速度？所有这些都取决于你所使用的TCP算法，并且它们都是不同的。让我们来看一些常见的拥塞算法及其独特之处。</p>
<ul>
<li>NewReno是你可能听说过的一种，在2000年代，它非常流行，许多不同的系统都在使用它。现在NewReno还在使用，但是在长肥网络（LFN，long fat network）上它的性能很差（比如海底隧道这种网络）。如果你通过跨海洋的10GB连接发送文件，但效果不佳，则可能需要进行调查是否使用了NewReno。</li>
<li>CTCP - 这是Windows Server 2003和Windows 7上的默认拥塞控制机制。</li>
<li>CUBIC - 是在Windows 10和MacBooks上默认使用的。原因之一是因为它在长肥网络中效果非常好。它可以快速建立其拥塞窗口，并且不会非常迅速地退后。如果看到丢失的数据包，它不会退缩到一半。</li>
<li>Westwood - 你不是经常能看到这种机制，它是专为处理有损网络而设计的。</li>
<li>最后是BBR - 这是Google专门开发的；它可以在大多数服务器中使用，并且你还可以在Linux操作系统上进行实验。</li>
</ul>
<h4>拥塞检测机制</h4>
<p>TCP如何知道出现问题并相应的退出其拥塞窗口？决定拥塞算法退避的主要方法有两种</p>
<ol>
<li>第一种是丢包。因此，在这里我们可以看到服务器发送了两个数据包，并且得到了很好的确认。然后发出四个数据包，其中一个数据包丢失。这就是说，我试过发出四个，但是效果不好，既然这样我就坚持每次网络往返都使用2MSS。</li>
<li>另一种拥塞检测机制是测量延时。服务器发送了几个数据包。就好像短跑比赛一样，这时候按下启动秒表。当看到这些数据包的确认返回时，便可以停止该秒表并测量延迟。该等待时间（延迟）不应该有显着变化。通常，仅当某处的链接出现拥塞时，它才会发生变化。让我们再想象一下，该服务器发送了几个数据包，但是这次要花费更多的时间才能从客户端取回确认。说明什么问题？是不是说明发生了拥堵。</li>
</ol>
<p>拥塞机制可以算是TCP比较高级一点的知识，希望你能对TCP的知识有了一个更深层次的理解。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="15&#32;不问收没收到，就问快不快&#32;-&#32;UDP.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="17&#32;来，先看看我的家谱&#32;-&#32;HTTP的身世.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b434f8cf91c645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
            document.getElementById("tip").innerHTML = "<a href='https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/%E5%85%A8%E8%A7%A3%E7%BD%91%E7%BB%9C%E5%8D%8F%E8%AE%AE/&quot;&#32;+&#32;cookie&#32;+&#32;&quot;'>跳转到上次进度</a>"
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
