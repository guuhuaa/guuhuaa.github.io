<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>18  原理实践：自己动手使用 Golang 开发 Docker（下）.md</title>
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

                    
                    <a href="00&#32;溯本求源，吃透&#32;Docker！.md">00 溯本求源，吃透 Docker！.md</a>

                </li>
                <li>

                    
                    <a href="01&#32;&#32;Docker&#32;安装：入门案例带你了解容器技术原理.md">01  Docker 安装：入门案例带你了解容器技术原理.md</a>

                </li>
                <li>

                    
                    <a href="02&#32;&#32;核心概念：镜像、容器、仓库，彻底掌握&#32;Docker&#32;架构核心设计理念.md">02  核心概念：镜像、容器、仓库，彻底掌握 Docker 架构核心设计理念.md</a>

                </li>
                <li>

                    
                    <a href="03&#32;&#32;镜像使用：Docker&#32;环境下如何配置你的镜像？.md">03  镜像使用：Docker 环境下如何配置你的镜像？.md</a>

                </li>
                <li>

                    
                    <a href="04&#32;&#32;容器操作：得心应手掌握&#32;Docker&#32;容器基本操作.md">04  容器操作：得心应手掌握 Docker 容器基本操作.md</a>

                </li>
                <li>

                    
                    <a href="05&#32;&#32;仓库访问：怎样搭建属于你的私有仓库？.md">05  仓库访问：怎样搭建属于你的私有仓库？.md</a>

                </li>
                <li>

                    
                    <a href="06&#32;&#32;最佳实践：如何在生产中编写最优&#32;Dockerfile？.md">06  最佳实践：如何在生产中编写最优 Dockerfile？.md</a>

                </li>
                <li>

                    
                    <a href="07&#32;&#32;Docker&#32;安全：基于内核的弱隔离系统如何保障安全性？.md">07  Docker 安全：基于内核的弱隔离系统如何保障安全性？.md</a>

                </li>
                <li>

                    
                    <a href="08&#32;&#32;容器监控：容器监控原理及&#32;cAdvisor&#32;的安装与使用.md">08  容器监控：容器监控原理及 cAdvisor 的安装与使用.md</a>

                </li>
                <li>

                    
                    <a href="09&#32;&#32;资源隔离：为什么构建容器需要&#32;Namespace&#32;？.md">09  资源隔离：为什么构建容器需要 Namespace ？.md</a>

                </li>
                <li>

                    
                    <a href="10&#32;&#32;资源限制：如何通过&#32;Cgroups&#32;机制实现资源限制？.md">10  资源限制：如何通过 Cgroups 机制实现资源限制？.md</a>

                </li>
                <li>

                    
                    <a href="11&#32;&#32;组件组成：剖析&#32;Docker&#32;组件作用及其底层工作原理.md">11  组件组成：剖析 Docker 组件作用及其底层工作原理.md</a>

                </li>
                <li>

                    
                    <a href="12&#32;&#32;网络模型：剖析&#32;Docker&#32;网络实现及&#32;Libnetwork&#32;底层原理.md">12  网络模型：剖析 Docker 网络实现及 Libnetwork 底层原理.md</a>

                </li>
                <li>

                    
                    <a href="13&#32;&#32;数据存储：剖析&#32;Docker&#32;卷与持久化数据存储的底层原理.md">13  数据存储：剖析 Docker 卷与持久化数据存储的底层原理.md</a>

                </li>
                <li>

                    
                    <a href="14&#32;&#32;文件存储驱动：AUFS&#32;文件系统原理及生产环境的最佳配置.md">14  文件存储驱动：AUFS 文件系统原理及生产环境的最佳配置.md</a>

                </li>
                <li>

                    
                    <a href="15&#32;&#32;文件存储驱动：Devicemapper&#32;文件系统原理及生产环境的最佳配置.md">15  文件存储驱动：Devicemapper 文件系统原理及生产环境的最佳配置.md</a>

                </li>
                <li>

                    
                    <a href="16&#32;&#32;文件存储驱动：OverlayFS&#32;文件系统原理及生产环境的最佳配置.md">16  文件存储驱动：OverlayFS 文件系统原理及生产环境的最佳配置.md</a>

                </li>
                <li>

                    
                    <a href="17&#32;&#32;原理实践：自己动手使用&#32;Golang&#32;开发&#32;Docker（上）.md">17  原理实践：自己动手使用 Golang 开发 Docker（上）.md</a>

                </li>
                <li>

                    <a class="current-tab" href="18&#32;&#32;原理实践：自己动手使用&#32;Golang&#32;开发&#32;Docker（下）.md">18  原理实践：自己动手使用 Golang 开发 Docker（下）.md</a>
                    

                </li>
                <li>

                    
                    <a href="19&#32;&#32;如何使用&#32;Docker&#32;Compose&#32;解决开发环境的依赖？.md">19  如何使用 Docker Compose 解决开发环境的依赖？.md</a>

                </li>
                <li>

                    
                    <a href="20&#32;&#32;如何在生产环境中使用&#32;Docker&#32;Swarm&#32;调度容器？.md">20  如何在生产环境中使用 Docker Swarm 调度容器？.md</a>

                </li>
                <li>

                    
                    <a href="21&#32;&#32;如何使&#32;Docker&#32;和&#32;Kubernetes&#32;结合发挥容器的最大价值？.md">21  如何使 Docker 和 Kubernetes 结合发挥容器的最大价值？.md</a>

                </li>
                <li>

                    
                    <a href="22&#32;&#32;多阶级构建：Docker&#32;下如何实现镜像多阶级构建？.md">22  多阶级构建：Docker 下如何实现镜像多阶级构建？.md</a>

                </li>
                <li>

                    
                    <a href="23&#32;&#32;DevOps：容器化后如何通过&#32;DevOps&#32;提高协作效能？.md">23  DevOps：容器化后如何通过 DevOps 提高协作效能？.md</a>

                </li>
                <li>

                    
                    <a href="24&#32;&#32;CICD：容器化后如何实现持续集成与交付？（上）.md">24  CICD：容器化后如何实现持续集成与交付？（上）.md</a>

                </li>
                <li>

                    
                    <a href="25&#32;&#32;CICD：容器化后如何实现持续集成与交付？（下）.md">25  CICD：容器化后如何实现持续集成与交付？（下）.md</a>

                </li>
                <li>

                    
                    <a href="26&#32;结束语&#32;&#32;展望未来：Docker&#32;的称霸之路.md">26 结束语  展望未来：Docker 的称霸之路.md</a>

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
                        <div><h1>18  原理实践：自己动手使用 Golang 开发 Docker（下）</h1>
<p>上一课时我们安装了 Golang，学习了一些容器必备的基础知识，并且自己动手编译了一个 gocker，实现了 Namespace 的隔离。今天我将带你深入剖析 gocker 的源码和实现原理，并且带你实现 cgroups 的资源限制。</p>
<h3>gocker 源码剖析</h3>
<p>打开 gocker 的源码，我们可以看到 gocker 的实现主要有两个 go 文件：一个是 main.go，一个是 run.go。这两个文件起了什么作用呢？</p>
<p>我们首先来看下 main.go 文件：</p>
<pre><code>$ cat main.go

package main

import (

    &quot;log&quot;

    &quot;os&quot;

    &quot;github.com/urfave/cli/v2&quot;

    &quot;github.com/wilhelmguo/gocker/runc&quot;

)

func main() {

    app := cli.NewApp()

    app.Name = &quot;gocker&quot;

    app.Usage = &quot;gocker 是 golang 编写的精简版 Docker，目的是学习 Docker 的运行原理。&quot;

    app.Commands = []*cli.Command{

        runc.InitCommand,

        runc.RunCommand,

    }

    if err := app.Run(os.Args); err != nil {

        log.Fatal(err)

    }

}
</code></pre>
<p>main.go 文件中引用了一个第三方工具库 github.com/urfave/cli，该工具库提供了一个编写命令行的工具，可以帮助我们快速构建命令行应用程序，Docker 默认的容器运行时 runC 也引用了该工具库。
main 函数是 gocker 执行的入口文件，main 定义了 gocker 的名称和简单介绍，同时调用了 InitCommand 和 RunCommand 实现了<code>gocker init</code>和<code>gocker run</code>这两个命令的初始化。</p>
<p>下面我们查看一下 run.go 的文件内容，run.go 文件中定义了 InitCommand 和 RunCommand 的详细实现以及容器启动的过程，文件内容如下。</p>
<pre><code>$ cat runc/run.go

package runc

import (

    &quot;errors&quot;

    &quot;fmt&quot;

    &quot;io/ioutil&quot;

    &quot;log&quot;

    &quot;os&quot;

    &quot;os/exec&quot;

    &quot;path/filepath&quot;

    &quot;strings&quot;

    &quot;syscall&quot;

    &quot;github.com/urfave/cli/v2&quot;

)

var RunCommand = &amp;cli.Command{

    Name: &quot;run&quot;,

    Usage: `启动一个隔离的容器

            gocker run -it [command]`,

    Flags: []cli.Flag{

        &amp;cli.BoolFlag{

            Name:  &quot;it&quot;,

            Usage: &quot;是否启用命令行交互模式&quot;,

        },

        &amp;cli.StringFlag{

            Name:  &quot;rootfs&quot;,

            Usage: &quot;容器根目录&quot;,

        },

    },

    Action: func(context *cli.Context) error {

        if context.Args().Len() &lt; 1 {

            return errors.New(&quot;参数不全，请检查！&quot;)

        }

        read, write, err := os.Pipe()

        if err != nil {

            return err

        }

        tty := context.Bool(&quot;it&quot;)

        rootfs := context.String(&quot;rootfs&quot;)

        cmd := exec.Command(&quot;/proc/self/exe&quot;, &quot;init&quot;)

        cmd.SysProcAttr = &amp;syscall.SysProcAttr{

            Cloneflags: syscall.CLONE_NEWNS |

                syscall.CLONE_NEWUTS |

                syscall.CLONE_NEWIPC |

                syscall.CLONE_NEWPID |

                syscall.CLONE_NEWNET,

        }

        if tty {

            cmd.Stdin = os.Stdin

            cmd.Stdout = os.Stdout

            cmd.Stderr = os.Stderr

        }

        cmd.ExtraFiles = []*os.File{read}

        cmd.Dir = rootfs

        if err := cmd.Start(); err != nil {

            log.Println(&quot;command start error&quot;, err)

            return err

        }

        write.WriteString(strings.Join(context.Args().Slice(), &quot; &quot;))

        write.Close()

        cmd.Wait()

        return nil

    },

}

var InitCommand = &amp;cli.Command{

    Name:  &quot;init&quot;,

    Usage: &quot;初始化容器进程，请勿直接调用！&quot;,

    Action: func(context *cli.Context) error {

        pwd, err := os.Getwd()

        if err != nil {

            log.Printf(&quot;Get current path error %v&quot;, err)

            return err

        }

        log.Println(&quot;Current path is &quot;, pwd)

        cmdArray := readCommandArray()

        if cmdArray == nil || len(cmdArray) == 0 {

            return fmt.Errorf(&quot;Command is empty&quot;)

        }

        log.Println(&quot;CmdArray is &quot;, cmdArray)

        err = pivotRoot(pwd)

        if err != nil {

            log.Printf(&quot;pivotRoot error %v&quot;, err)

            return err

        }

        //mount proc

        defaultMountFlags := syscall.MS_NOEXEC | syscall.MS_NOSUID | syscall.MS_NODEV

        syscall.Mount(&quot;proc&quot;, &quot;/proc&quot;, &quot;proc&quot;, uintptr(defaultMountFlags), &quot;&quot;)

        // 配置hostname

        if err := syscall.Sethostname([]byte(&quot;lagoudocker&quot;)); err != nil {

            fmt.Printf(&quot;Error setting hostname - %s\n&quot;, err)

            return err

        }

        path, err := exec.LookPath(cmdArray[0])

        if err != nil {

            log.Printf(&quot;Exec loop path error %v&quot;, err)

            return err

        }

        // export PATH=$PATH:/bin

        if err := syscall.Exec(path, cmdArray[0:], os.Environ()); err != nil {

            log.Println(err.Error())

        }

        return nil

    },

}

func pivotRoot(root string) error {

    // 确保新 root 和老 root 不在同一目录

    // MS_BIND：执行bind挂载，使文件或者子目录树在文件系统内的另一个点上可视。

    // MS_REC： 创建递归绑定挂载，递归更改传播类型

    if err := syscall.Mount(root, root, &quot;bind&quot;, syscall.MS_BIND|syscall.MS_REC, &quot;&quot;); err != nil {

        return fmt.Errorf(&quot;Mount rootfs to itself error: %v&quot;, err)

    }

    // 创建 .pivot_root 文件夹，用于存储 old_root

    pivotDir := filepath.Join(root, &quot;.pivot_root&quot;)

    if err := os.Mkdir(pivotDir, 0777); err != nil {

        return err

    }

    // 调用 Golang 封装的 PivotRoot

    if err := syscall.PivotRoot(root, pivotDir); err != nil {

        return fmt.Errorf(&quot;pivot_root %v&quot;, err)

    }

    // 修改工作目录

    if err := syscall.Chdir(&quot;/&quot;); err != nil {

        return fmt.Errorf(&quot;chdir / %v&quot;, err)

    }

    pivotDir = filepath.Join(&quot;/&quot;, &quot;.pivot_root&quot;)

    // 卸载 .pivot_root

    if err := syscall.Unmount(pivotDir, syscall.MNT_DETACH); err != nil {

        return fmt.Errorf(&quot;unmount pivot_root dir %v&quot;, err)

    }

    // 删除临时文件夹 .pivot_root

    return os.Remove(pivotDir)

}

func readCommandArray() []string {

    pipe := os.NewFile(uintptr(3), &quot;pipe&quot;)

    msg, err := ioutil.ReadAll(pipe)

    if err != nil {

        log.Printf(&quot;init read pipe error %v&quot;, err)

        return nil

    }

    msgStr := string(msg)

    return strings.Split(msgStr, &quot; &quot;)

}
</code></pre>
<p>看到这么多代码你是不是有点懵？别担心，我帮你一一解读。</p>
<p>上面文件中有两个比较重要的变量 InitCommand 和 RunCommand，它们的作用如下：</p>
<ul>
<li>RunCommand 是当我们执行 gocker run 命令时调用的函数，是实现 gocker run 的入口；</li>
<li>InitCommand 是当我们执行 gocker run 时自动调用 gocker init 来初始化容器的一些环境。</li>
</ul>
<h4>RunCommand （容器启动的入口）</h4>
<p>我们先从 RunCommand 来分析：</p>
<pre><code>var RunCommand = &amp;cli.Command{

    // 定义一个启动命令，这里定义的是 run 命令，当执行 gocker run 时会调用该函数

    Name: &quot;run&quot;,

    // 使用说明

    Usage: `启动一个隔离的容器

            gocker run -it [command]`,

    // 执行 gocker run 命令可以传递的参数

    Flags: []cli.Flag{

        &amp;cli.BoolFlag{

            Name:  &quot;it&quot;,

            Usage: &quot;是否启用命令行交互模式&quot;,

        },

        &amp;cli.StringFlag{

            Name:  &quot;rootfs&quot;,

            Usage: &quot;容器根目录&quot;,

        },

    },

    // gocker run 命令的执行函数

    Action: func(context *cli.Context) error {

        // 校验参数 

        if context.Args().Len() &lt; 1 {

            return errors.New(&quot;参数不全，请检查！&quot;)

        }

        read, write, err := os.Pipe()

        if err != nil {

            return err

        }

        // 获取传入的参数的值

        tty := context.Bool(&quot;it&quot;)

        rootfs := context.String(&quot;rootfs&quot;)

        // 这里执行 /proc/self/exe init 相当于执行 gocker init

        cmd := exec.Command(&quot;/proc/self/exe&quot;, &quot;init&quot;)

        // 定义新创建哪些命名空间

        cmd.SysProcAttr = &amp;syscall.SysProcAttr{

            Cloneflags: syscall.CLONE_NEWNS |

                syscall.CLONE_NEWUTS |

                syscall.CLONE_NEWIPC |

                syscall.CLONE_NEWPID |

                syscall.CLONE_NEWNET,

        }

        // 把容器的标准输出重定向到主机的标准输出

        if tty {

            cmd.Stdin = os.Stdin

            cmd.Stdout = os.Stdout

            cmd.Stderr = os.Stderr

        }

        cmd.ExtraFiles = []*os.File{read}

        cmd.Dir = rootfs

        // 启动容器

        if err := cmd.Start(); err != nil {

            log.Println(&quot;command start error&quot;, err)

            return err

        }

        write.WriteString(strings.Join(context.Args().Slice(), &quot; &quot;))

        write.Close()

        // 等待容器退出

        cmd.Wait()

        return nil

        }
</code></pre>
<p>RunCommand 变量实际上是一个 Command 结构体，这个结构体包含了四个变量。</p>
<ol>
<li>Name：定义一个启动命令，这里定义的是 run 命令，当执行 gocker run 时会调用该函数。</li>
<li>Usage：<code>gocker run</code>命令的使用说明。</li>
<li>Flags：执行<code>gocker run</code>命令可以传递的参数。</li>
<li>Action： 该变量是真正的 gocker run 命令的入口， 主要做了以下事情：
<ul>
<li>校验 gocker run 传递的参数；</li>
<li>构造一个 Pipe，把 gocker 的启动参数写入，方便在 init 进程中获取；</li>
<li>定义 /proc/self/exe init 调用，相当于调用 gocker init ；</li>
<li>创建五种命名空间用于资源隔离，分别为 Mount Namespace、UTS Namespace、IPC Namespace、PID Namespace 和 Net Namespace；</li>
<li>调用 cmd.Start 函数，开始执行容器启动步骤，首先创建出来一个 namespace （上一步定义的五种namespace）隔离的进程，然后调用 /proc/self/exe，也就是调用 gocker init，执行 InitCommand 中定义的容器初始化步骤。</li>
</ul>
</li>
</ol>
<p>那么 InitCommand 究竟做了什么呢？</p>
<h4>InitCommand（准备容器环境）</h4>
<p>下面我们看下 InitCommand 中的内容：</p>
<pre><code>var InitCommand = &amp;cli.Command{

    Name:  &quot;init&quot;,

    Usage: &quot;初始化容器进程，请勿直接调用！&quot;,

    Action: func(context *cli.Context) error {

        // 获取当前执行目录

        pwd, err := os.Getwd()

        if err != nil {

            log.Printf(&quot;Get current path error %v&quot;, err)

            return err

        }

        log.Println(&quot;Current path is &quot;, pwd)

        // 获取用户传递的启动参数

        cmdArray := readCommandArray()

        if cmdArray == nil || len(cmdArray) == 0 {

            return fmt.Errorf(&quot;Command is empty&quot;)

        }

        log.Println(&quot;CmdArray is &quot;, cmdArray)

        // pivotRoot 的作用类似于 chroot，可以把我们准备的镜像目录设置为容器的根目录。

        err = pivotRoot(pwd)

        if err != nil {

            log.Printf(&quot;pivotRoot error %v&quot;, err)

            return err

        }

        // 挂载容器自己的 proc 目录，实现 ps 只能看到容器自己的进程

        defaultMountFlags := syscall.MS_NOEXEC | syscall.MS_NOSUID | syscall.MS_NODEV

        syscall.Mount(&quot;proc&quot;, &quot;/proc&quot;, &quot;proc&quot;, uintptr(defaultMountFlags), &quot;&quot;)

        // 配置主机名为 lagoudocker

        if err := syscall.Sethostname([]byte(&quot;lagoudocker&quot;)); err != nil {

            fmt.Printf(&quot;Error setting hostname - %s\n&quot;, err)

            return err

        }

        path, err := exec.LookPath(cmdArray[0])

        if err != nil {

            log.Printf(&quot;Exec loop path error %v&quot;, err)

            return err

        }

        // syscall.Exec 相当于 shell 中的 exec 实现，这里用 用户传递的主命令来替换 init 进程，从而实现容器的 1 号进程为用户传递的主进程

        if err := syscall.Exec(path, cmdArray[0:], os.Environ()); err != nil {

            log.Println(err.Error())

        }

        return nil

    },

}
</code></pre>
<p>通过代码你能看出 InitCommand 都做了哪些容器启动前的准备工作吗？</p>
<p>InitCommand 主要做了以下几件事情：</p>
<ol>
<li>获取当前运行目录；</li>
<li>从 RunCommand 中获取用户传递的容器启动参数；</li>
<li>修改当前进程运行的根目录为用户传递的 rootfs 目录；</li>
<li>挂载容器自己的 proc 目录，使得容器中执行 ps 命令只能看到自己命名空间下的进程；</li>
<li>设置容器的主机名称为 lagoudocker；</li>
<li>执行 syscall.Exec 实现使用用户传递的启动命令替换当前 init 进程。</li>
</ol>
<p>这里有两个比较关键的技术点 pivotRoot 和 syscall.Exec。</p>
<ul>
<li>pivotRoot：pivotRoot 是一个系统调用，主要功能是改变当前进程的根目录，它可以把当前进程的根目录移动到我们传递的 rootfs 目录下，从而使得我们不仅能够看到指定目录，还可以看到它的子目录信息。</li>
<li>syscall.Exec：syscall.Exec 是一个系统调用，这个系统调用可以实现执行指定的命令，但是并不创建新的进程，而是在当前的进程空间执行，替换掉正在执行的进程，复用同一个进程号。通过这种机制，才实现了我们在容器中看到的 1 号进程是我们传递的命令，而不是 init 进程。</li>
</ul>
<p>最后，总结下容器的完整创建流程:</p>
<p>1.使用以下命令创建容器</p>
<pre><code>gocker run -it -rootfs=/tmp/busybox /bin/sh
</code></pre>
<p>2.RunCommand 解析请求的参数（-it -rootfs=/tmp/busybox）和主进程启动命令（/bin/sh）；</p>
<p>3.创建 namespace 隔离的容器进程；</p>
<p>4.启动容器进程；</p>
<p>5.容器内的进程执行 /proc/self/exe 调用自己实现容器的初始化，修改当前进程运行的根目录，挂载 proc 文件系统，修改主机名，最后使用 sh 进程替换当前容器的进程，使得容器的主进程为 sh 进程。</p>
<p>目前我们的容器虽然实现了使用 Namespace 隔离各种资源，但是容器内的进程仍然可以任意地使用主机的 CPU 、内存等资源。而这可能导致主机的资源竞争，下面我们使用cgroups来实现对 CPU 和内存的限制。</p>
<h3>为 gocker 添加 cgroups 限制</h3>
<p>[在第 10 讲中]，我们手动操作 cgroups 实现了对容器资源的限制，下面我把这部分手动操作转化为代码。</p>
<h4>编写资源限制源码</h4>
<p>首先我们定义 cgroups 的挂载目录和我们要创建的目录，定义如下：</p>
<pre><code>const gockerCgroupPath = &quot;gocker&quot;

const cgroupsRoot = &quot;/sys/fs/cgroup&quot;
</code></pre>
<p>然后定义Cgroups结构体，分别定义 CPU 和 Memory 字段，用于存储用户端传递的 CPU 和 Memory 限制值：</p>
<pre><code>type Cgroups struct {

    // 单位 核

    CPU int

    // 单位 兆

    Memory int

}
</code></pre>
<p>接着定义 Cgroups 对象的一些操作方法，这样方便我们对当前容器的 cgroups 进程操作。方法定义如下。</p>
<ul>
<li>Apply：把容器的 pid 写入到对应子系统下的 tasks 文件中，使得 cgroups 限制对容器进程生效。</li>
<li>Destroy：容器退出时删除对应的 cgroups 文件。</li>
<li>SetCPULimit：将 CPU 限制值写入到 cpu.cfs_quota_us 文件中。</li>
<li>SetMemoryLimit：将内存限制值写入 memory.limit_in_bytes 文件中。</li>
</ul>
<pre><code>func (c *Cgroups) Apply(pid int) error {

    if c.CPU != 0 {

        cpuCgroupPath, err := getCgroupPath(&quot;cpu&quot;, true)

        if err != nil {

            return err

        }

        err = ioutil.WriteFile(path.Join(cpuCgroupPath, &quot;tasks&quot;), []byte(strconv.Itoa(pid)), 0644)

        if err != nil {

            return fmt.Errorf(&quot;set cgroup cpu fail %v&quot;, err)

        }

    }

    if c.Memory != 0 {

        memoryCgroupPath, err := getCgroupPath(&quot;memory&quot;, true)

        if err != nil {

            return err

        }

        err = ioutil.WriteFile(path.Join(memoryCgroupPath, &quot;tasks&quot;), []byte(strconv.Itoa(pid)), 0644)

        if err != nil {

            return fmt.Errorf(&quot;set cgroup memory fail %v&quot;, err)

        }

    }

    return nil

}

// 释放cgroup

func (c *Cgroups) Destroy() error {

    if c.CPU != 0 {

        cpuCgroupPath, err := getCgroupPath(&quot;cpu&quot;, false)

        if err != nil {

            return err

        }

        return os.RemoveAll(cpuCgroupPath)

    }

    if c.Memory != 0 {

        memoryCgroupPath, err := getCgroupPath(&quot;memory&quot;, false)

        if err != nil {

            return err

        }

        return os.RemoveAll(memoryCgroupPath)

    }

    return nil

}

func (c *Cgroups) SetCPULimit(cpu int) error {

    cpuCgroupPath, err := getCgroupPath(&quot;cpu&quot;, true)

    if err != nil {

        return err

    }

    if err := ioutil.WriteFile(path.Join(cpuCgroupPath, &quot;cpu.cfs_quota_us&quot;), []byte(strconv.Itoa(cpu*100000)), 0644); err != nil {

        return fmt.Errorf(&quot;set cpu limit fail %v&quot;, err)

    }

    return nil

}

func (c *Cgroups) SetMemoryLimit(memory int) error {

    memoryCgroupPath, err := getCgroupPath(&quot;memory&quot;, true)

    if err != nil {

        return err

    }

    if err := ioutil.WriteFile(path.Join(memoryCgroupPath, &quot;memory.limit_in_bytes&quot;), []byte(strconv.Itoa(memory*1024*1024)), 0644); err != nil {

        return fmt.Errorf(&quot;set memory limit fail %v&quot;, err)

    }

    return nil

}
</code></pre>
<p>最后在 run 命令的 Action 函数中，添加 cgroups 初始化逻辑，将 CPU 和内存的限制值写入到 cgroups 文件中，并且将当前进程的 pid 也写入到 cgroups 的 tasks 文件中，使得 CPU 和内存的限制对于当前容器进程生效。</p>
<pre><code>        cgroup := cgroups.NewCgroups()

        defer cgroup.Destroy()

        cpus := context.Int(&quot;cpus&quot;)

        if cpus != 0 {

            cgroup.SetCPULimit(cpus)

        }

        m := context.Int(&quot;m&quot;)

        if m != 0 {

            cgroup.SetMemoryLimit(m)

        }

        cgroup.Apply(cmd.Process.Pid)
</code></pre>
<p>到此，我们成功实现了一个带有资源限制的 gocker 容器。下面进入 gocker 的目录，并且编译一下 gocker：</p>
<pre><code>$ cd gocker

$ git checkout lesson-18

$ go install
</code></pre>
<p>执行完 go install 后， Golang 会自动帮助我们编译当前项目下的代码，编译后的二进制文件存放在 $GOPATH/bin 目录下，由于我们之前在 $HOME/.bashrc 文件下把 $GOPATH/bin 放入了系统 PATH 中，所以此时你可以直接使用 gocker 命令了。</p>
<h4>启动带有资源限制的容器</h4>
<p>接下来我们使用 gocker 来启动一个带有 CPU 限制的容器：</p>
<pre><code># gocker run -it -cpus=1 -rootfs=/tmp/busybox /bin/sh

2020/09/19 23:46:27 Current path is  /tmp/busybox

2020/09/19 23:46:27 CmdArray is  [/bin/sh]

/ #
</code></pre>
<p>然后我们新打开一个命令行窗口，查看一下 cgroups 相关的文件是否被创建：</p>
<pre><code># cd /sys/fs/cgroup/cpu

# ls -l

总用量 0

-rw-r--r--  1 root root 0 9月  19 21:34 cgroup.clone_children

--w--w--w-  1 root root 0 9月  19 21:34 cgroup.event_control

-rw-r--r--  1 root root 0 9月  19 21:34 cgroup.procs

-r--r--r--  1 root root 0 9月  19 21:34 cgroup.sane_behavior

-r--r--r--  1 root root 0 9月  19 21:34 cpuacct.stat

-rw-r--r--  1 root root 0 9月  19 21:34 cpuacct.usage

-r--r--r--  1 root root 0 9月  19 21:34 cpuacct.usage_percpu

-rw-r--r--  1 root root 0 9月  19 21:34 cpu.cfs_period_us

-rw-r--r--  1 root root 0 9月  19 21:34 cpu.cfs_quota_us

-rw-r--r--  1 root root 0 9月  19 21:34 cpu.rt_period_us

-rw-r--r--  1 root root 0 9月  19 21:34 cpu.rt_runtime_us

-rw-r--r--  1 root root 0 9月  19 21:34 cpu.shares

-r--r--r--  1 root root 0 9月  19 21:34 cpu.stat

drwxr-xr-x  2 root root 0 9月  22 20:48 gocker

-rw-r--r--  1 root root 0 9月  19 21:34 notify_on_release

-rw-r--r--  1 root root 0 9月  19 21:34 release_agent

drwxr-xr-x 70 root root 0 9月  22 20:24 system.slice

-rw-r--r--  1 root root 0 9月  19 21:34 tasks

drwxr-xr-x  2 root root 0 9月  19 21:34 user.slice
</code></pre>
<p>可以看到我们启动容器后， gocker 在 cpu 子系统下，已经成功创建 gocker 目录。然后我们查看一下 gocker 目录下的内容：</p>
<pre><code># ls -l gocker/

总用量 0

-rw-r--r-- 1 root root 0 9月  22 20:48 cgroup.clone_children

--w--w--w- 1 root root 0 9月  22 20:48 cgroup.event_control

-rw-r--r-- 1 root root 0 9月  22 20:48 cgroup.procs

-r--r--r-- 1 root root 0 9月  22 20:48 cpuacct.stat

-rw-r--r-- 1 root root 0 9月  22 20:48 cpuacct.usage

-r--r--r-- 1 root root 0 9月  22 20:48 cpuacct.usage_percpu

-rw-r--r-- 1 root root 0 9月  22 20:48 cpu.cfs_period_us

-rw-r--r-- 1 root root 0 9月  22 20:48 cpu.cfs_quota_us

-rw-r--r-- 1 root root 0 9月  22 20:48 cpu.rt_period_us

-rw-r--r-- 1 root root 0 9月  22 20:48 cpu.rt_runtime_us

-rw-r--r-- 1 root root 0 9月  22 20:48 cpu.shares

-r--r--r-- 1 root root 0 9月  22 20:48 cpu.stat

-rw-r--r-- 1 root root 0 9月  22 20:48 notify_on_release

-rw-r--r-- 1 root root 0 9月  22 20:48 tasks
</code></pre>
<p>可以看到 cgroups 已经帮我们初始化好了 cpu 子系统的文件，然后我们查看一下 cpu.cfs_quota_us 的内容：</p>
<pre><code># cat gocker/cpu.cfs_quota_us

100000
</code></pre>
<p>可以看到我们容器的 CPU资源已经被限制为 1 核。下面我们来验证一下 CPU 限制是否生效。
首先我们在容器窗口使用以下命令制造一个死循环，来提升 cpu 使用率：</p>
<pre><code># while true;do echo;done;
</code></pre>
<p>然后在主机的窗口使用 top 查看一下cpu 使用率：</p>
<pre><code>top - 20:57:50 up 2 days, 23:23,  2 users,  load average: 1.08, 0.27, 0.14

Tasks: 113 total,   4 running, 109 sleeping,   0 stopped,   0 zombie

%Cpu(s): 23.5 us, 26.9 sy,  0.0 ni, 49.2 id,  0.0 wa,  0.0 hi,  0.3 si,  0.0 st

KiB Mem :  3880512 total,  1573052 free,   408696 used,  1898764 buff/cache

KiB Swap:        0 total,        0 free,        0 used.  3141076 avail Mem

  PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND

30766 root      20   0    1312    260    212 R  99.3  0.0   0:30.90 sh
</code></pre>
<p>通过 top 的输出可以看到我们的容器 cpu 使用率被限制到了 100% 以内，即 1 个核。</p>
<p>到此，我们的容器不仅有了 Namespace 隔离，同时也有了 cgroups 的资源限制。</p>
<h3>结语</h3>
<p>上一课时和本课时，我们一起安装了 golang，并且使用 golang 实现了一个精简版的 Docker，它具有基本的 namespace 隔离，并且还使用 cgroups 对容器进行了资源限制。</p>
<p>这两个课时的关键技术我帮你总结如下。</p>
<ol>
<li>Linux 的 /proc 目录是一种“文件系统”，它存放于内存中，是一个虚拟的文件系统，/proc 目录存放了当前内核运行状态的一系列特殊的文件，你可以通过这些文件查看当前的进程信息。</li>
<li>/proc/self/exe 是一个特殊的连接，执行该文件等同于执行当前程序的二进制文件</li>
<li>pivotRoot 是一个系统调用，主要功能是改变当前进程的根目录，它可以把当前进程的根目录移动到我们传递的 rootfs 目录下</li>
<li>syscall.Exec 是一个系统调用，这个系统调用可以实现新的进程直接替换正在执行的老的进程，并且复用老进程的 ID。</li>
</ol>
<p>另外，容器的实现当然离不开 Linux 的 namespace 和 cgroups 这两项关键技术，有了 Linux 的这些关键技术才使得我们的容器可以顺利实现，可以说 Linux 是容器技术的基石。而容器的编写，我们不仅可以使用 Go 语言，也可以使用其他编程语言，甚至只使用 shell 命令也可以实现一个容器。</p>
<p>那么，你可以使用 shell 命令实现一个精简版的 Docker 吗？思考后，不妨试着写一下。</p>
<p>下一课时，我将教你使用 Docker Compose 解决开发环境的依赖。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="17&#32;&#32;原理实践：自己动手使用&#32;Golang&#32;开发&#32;Docker（上）.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="19&#32;&#32;如何使用&#32;Docker&#32;Compose&#32;解决开发环境的依赖？.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b435a1eff47645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
            document.getElementById("tip").innerHTML = "<a href='https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/%E7%94%B1%E6%B5%85%E5%85%A5%E6%B7%B1%E5%90%83%E9%80%8F%20Docker-%E5%AE%8C/&quot;&#32;+&#32;cookie&#32;+&#32;&quot;'>跳转到上次进度</a>"
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
