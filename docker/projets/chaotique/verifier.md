<h2>:mag: Vulnerabilities of <code>fagnerfgb/chaotique:v1</code></h2>

<details open="true"><summary>:package: Image Reference</strong> <code>fagnerfgb/chaotique:v1</code></summary>
<table>
<tr><td>digest</td><td><code>sha256:75a639331ec25e0196a2ad3864cb15829bd313ac67e9f313c3ca505e6dfa9f10</code></td><tr><tr><td>vulnerabilities</td><td><img alt="critical: 9" src="https://img.shields.io/badge/critical-9-8b1924"/> <img alt="high: 39" src="https://img.shields.io/badge/high-39-e25d68"/> <img alt="medium: 60" src="https://img.shields.io/badge/medium-60-fbb552"/> <img alt="low: 109" src="https://img.shields.io/badge/low-109-fce1a9"/> <img alt="unspecified: 10" src="https://img.shields.io/badge/unspecified-10-lightgrey"/></td></tr>
<tr><td>platform</td><td>linux/amd64</td></tr>
<tr><td>size</td><td>452 MB</td></tr>
<tr><td>packages</td><td>843</td></tr>
</table>
</details></table>
</details>

<table>
<tr><td valign="top">
<details><summary><img alt="critical: 2" src="https://img.shields.io/badge/C-2-8b1924"/> <img alt="high: 1" src="https://img.shields.io/badge/H-1-e25d68"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 0" src="https://img.shields.io/badge/L-0-lightgrey"/> <!-- unspecified: 0 --><strong>expat</strong> <code>2.5.0-1</code> (deb)</summary>

<small><code>pkg:deb/debian/expat@2.5.0-1?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2024-45492?s=debian&n=expat&ns=debian&t=deb&osn=debian&osv=12&vr=%3C2.5.0-1%2Bdeb12u1"><img alt="critical : CVE--2024--45492" src="https://img.shields.io/badge/CVE--2024--45492-lightgrey?label=critical%20&labelColor=8b1924"/></a> 

<table>
<tr><td>Affected range</td><td><code><2.5.0-1+deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><code>2.5.0-1+deb12u1</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.091%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>41st percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

An issue was discovered in libexpat before 2.6.3. nextScaffoldPart in xmlparse.c can have an integer overflow for m_groupSize on 32-bit platforms (where UINT_MAX equals SIZE_MAX).

---
- expat 2.6.2-2 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1080152)
https://github.com/libexpat/libexpat/pull/892
https://github.com/libexpat/libexpat/issues/889
https://github.com/libexpat/libexpat/commit/29ef43a0bab633b41e71dd6d900fff5f6b3ad5e4 (R_2_6_3)

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2024-45491?s=debian&n=expat&ns=debian&t=deb&osn=debian&osv=12&vr=%3C2.5.0-1%2Bdeb12u1"><img alt="critical : CVE--2024--45491" src="https://img.shields.io/badge/CVE--2024--45491-lightgrey?label=critical%20&labelColor=8b1924"/></a> 

<table>
<tr><td>Affected range</td><td><code><2.5.0-1+deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><code>2.5.0-1+deb12u1</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.091%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>41st percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

An issue was discovered in libexpat before 2.6.3. dtdCopy in xmlparse.c can have an integer overflow for nDefaultAtts on 32-bit platforms (where UINT_MAX equals SIZE_MAX).

---
- expat 2.6.2-2 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1080150)
https://github.com/libexpat/libexpat/pull/891
https://github.com/libexpat/libexpat/issues/888
https://github.com/libexpat/libexpat/commit/b8a7dca4670973347892cfc452b24d9001dcd6f5 (R_2_6_3)

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2024-45490?s=debian&n=expat&ns=debian&t=deb&osn=debian&osv=12&vr=%3C2.5.0-1%2Bdeb12u1"><img alt="high : CVE--2024--45490" src="https://img.shields.io/badge/CVE--2024--45490-lightgrey?label=high%20&labelColor=e25d68"/></a> 

<table>
<tr><td>Affected range</td><td><code><2.5.0-1+deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><code>2.5.0-1+deb12u1</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.046%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>19th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

An issue was discovered in libexpat before 2.6.3. xmlparse.c does not reject a negative length for XML_ParseBuffer.

---
- expat 2.6.2-2 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1080149)
https://github.com/libexpat/libexpat/pull/890
https://github.com/libexpat/libexpat/issues/887
https://github.com/libexpat/libexpat/commit/e5d6bf015ee531df0a8751baa618d25b2de73a7c (R_2_6_3)

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 1" src="https://img.shields.io/badge/C-1-8b1924"/> <img alt="high: 4" src="https://img.shields.io/badge/H-4-e25d68"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 5" src="https://img.shields.io/badge/L-5-fce1a9"/> <!-- unspecified: 0 --><strong>git</strong> <code>1:2.39.2-1.1</code> (deb)</summary>

<small><code>pkg:deb/debian/git@1:2.39.2-1.1?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2024-32002?s=debian&n=git&ns=debian&t=deb&osn=debian&osv=12&vr=%3C1%3A2.39.5-0%2Bdeb12u1"><img alt="critical : CVE--2024--32002" src="https://img.shields.io/badge/CVE--2024--32002-lightgrey?label=critical%20&labelColor=8b1924"/></a> 

<table>
<tr><td>Affected range</td><td><code><1:2.39.5-0+deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><code>1:2.39.5-0+deb12u1</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.152%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>52nd percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

Git is a revision control system. Prior to versions 2.45.1, 2.44.1, 2.43.4, 2.42.2, 2.41.1, 2.40.2, and 2.39.4, repositories with submodules can be crafted in a way that exploits a bug in Git whereby it can be fooled into writing files not into the submodule's worktree but into a `.git/` directory. This allows writing a hook that will be executed while the clone operation is still running, giving the user no opportunity to inspect the code that is being executed. The problem has been patched in versions 2.45.1, 2.44.1, 2.43.4, 2.42.2, 2.41.1, 2.40.2, and 2.39.4. If symbolic link support is disabled in Git (e.g. via `git config --global core.symlinks false`), the described attack won't work. As always, it is best to avoid cloning repositories from untrusted sources.

---
- git 1:2.45.1-1 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1071160)
https://github.com/git/git/security/advisories/GHSA-8h77-4q3w-gfgv
Additional useful test: https://github.com/git/git/commit/b20c10fd9b035f46e48112d2cd33d7cb740012b6
Requisite: https://github.com/git/git/commit/906fc557b70b2b2995785c9b37e212d2f86b469e
Fixed by: https://github.com/git/git/commit/97065761333fd62db1912d81b489db938d8c991d

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2024-32004?s=debian&n=git&ns=debian&t=deb&osn=debian&osv=12&vr=%3C1%3A2.39.5-0%2Bdeb12u1"><img alt="high : CVE--2024--32004" src="https://img.shields.io/badge/CVE--2024--32004-lightgrey?label=high%20&labelColor=e25d68"/></a> 

<table>
<tr><td>Affected range</td><td><code><1:2.39.5-0+deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><code>1:2.39.5-0+deb12u1</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.044%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>13th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

Git is a revision control system. Prior to versions 2.45.1, 2.44.1, 2.43.4, 2.42.2, 2.41.1, 2.40.2, and 2.39.4, an attacker can prepare a local repository in such a way that, when cloned, will execute arbitrary code during the operation. The problem has been patched in versions 2.45.1, 2.44.1, 2.43.4, 2.42.2, 2.41.1, 2.40.2, and 2.39.4. As a workaround, avoid cloning repositories from untrusted sources.

---
- git 1:2.45.1-1 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1071160)
https://github.com/git/git/security/advisories/GHSA-xfc6-vwr8-r389
https://github.com/git/git/commit/f4aa8c8bb11dae6e769cd930565173808cbb69c8
https://github.com/git/git/commit/7b70e9efb18c2cc3f219af399bd384c5801ba1d7
Regression: https://lore.kernel.org/git/924426.1716570031@dash.ant.isi.edu/T/#u
fcgiwrap (autopkgtest-only issue) and ikiwiki-hosting were broken
by the "detect dubious ownership" commit and fixed in >= bookworm.
The "detect dubious ownership" commit was not backported to <= bullseye.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2023-25652?s=debian&n=git&ns=debian&t=deb&osn=debian&osv=12&vr=%3C1%3A2.39.5-0%2Bdeb12u1"><img alt="high : CVE--2023--25652" src="https://img.shields.io/badge/CVE--2023--25652-lightgrey?label=high%20&labelColor=e25d68"/></a> 

<table>
<tr><td>Affected range</td><td><code><1:2.39.5-0+deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><code>1:2.39.5-0+deb12u1</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.576%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>78th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

Git is a revision control system. Prior to versions 2.30.9, 2.31.8, 2.32.7, 2.33.8, 2.34.8, 2.35.8, 2.36.6, 2.37.7, 2.38.5, 2.39.3, and 2.40.1, by feeding specially crafted input to `git apply --reject`, a path outside the working tree can be overwritten with partially controlled contents (corresponding to the rejected hunk(s) from the given patch). A fix is available in versions 2.30.9, 2.31.8, 2.32.7, 2.33.8, 2.34.8, 2.35.8, 2.36.6, 2.37.7, 2.38.5, 2.39.3, and 2.40.1. As a workaround, avoid using `git apply` with `--reject` when applying patches from an untrusted source. Use `git apply --stat` to inspect a patch before applying; avoid applying one that create a conflict where a link corresponding to the `*.rej` file exists.

---
- git 1:2.40.1-1 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1034835)
https://lore.kernel.org/lkml/xmqqa5yv3n93.fsf@gitster.g/
https://github.com/git/git/commit/9db05711c98efc14f414d4c87135a34c13586e0b (v2.30.9)

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2024-32465?s=debian&n=git&ns=debian&t=deb&osn=debian&osv=12&vr=%3C1%3A2.39.5-0%2Bdeb12u1"><img alt="high : CVE--2024--32465" src="https://img.shields.io/badge/CVE--2024--32465-lightgrey?label=high%20&labelColor=e25d68"/></a> 

<table>
<tr><td>Affected range</td><td><code><1:2.39.5-0+deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><code>1:2.39.5-0+deb12u1</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.044%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>13th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

Git is a revision control system. The Git project recommends to avoid working in untrusted repositories, and instead to clone it first with `git clone --no-local` to obtain a clean copy. Git has specific protections to make that a safe operation even with an untrusted source repository, but vulnerabilities allow those protections to be bypassed. In the context of cloning local repositories owned by other users, this vulnerability has been covered in CVE-2024-32004. But there are circumstances where the fixes for CVE-2024-32004 are not enough: For example, when obtaining a `.zip` file containing a full copy of a Git repository, it should not be trusted by default to be safe, as e.g. hooks could be configured to run within the context of that repository. The problem has been patched in versions 2.45.1, 2.44.1, 2.43.4, 2.42.2, 2.41.1, 2.40.2, and 2.39.4. As a workaround, avoid using Git in repositories that have been obtained via archives from untrusted sources.

---
- git 1:2.45.1-1 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1071160)
https://github.com/git/git/security/advisories/GHSA-vm9j-46j9-qvq4
Prerequsite for test: https://github.com/git/git/commit/5c5a4a1c05932378d259b1fdd9526cab971656a2
Fixed by: https://github.com/git/git/commit/7b70e9efb18c2cc3f219af399bd384c5801ba1d7

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2023-29007?s=debian&n=git&ns=debian&t=deb&osn=debian&osv=12&vr=%3C1%3A2.39.5-0%2Bdeb12u1"><img alt="high : CVE--2023--29007" src="https://img.shields.io/badge/CVE--2023--29007-lightgrey?label=high%20&labelColor=e25d68"/></a> 

<table>
<tr><td>Affected range</td><td><code><1:2.39.5-0+deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><code>1:2.39.5-0+deb12u1</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.831%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>82nd percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

Git is a revision control system. Prior to versions 2.30.9, 2.31.8, 2.32.7, 2.33.8, 2.34.8, 2.35.8, 2.36.6, 2.37.7, 2.38.5, 2.39.3, and 2.40.1, a specially crafted `.gitmodules` file with submodule URLs that are longer than 1024 characters can used to exploit a bug in `config.c::git_config_copy_or_rename_section_in_file()`. This bug can be used to inject arbitrary configuration into a user's `$GIT_DIR/config` when attempting to remove the configuration section associated with that submodule. When the attacker injects configuration values which specify executables to run (such as `core.pager`, `core.editor`, `core.sshCommand`, etc.) this can lead to a remote code execution. A fix A fix is available in versions 2.30.9, 2.31.8, 2.32.7, 2.33.8, 2.34.8, 2.35.8, 2.36.6, 2.37.7, 2.38.5, 2.39.3, and 2.40.1. As a workaround, avoid running `git submodule deinit` on untrusted repositories or without prior inspection of any submodule sections in `$GIT_DIR/config`.

---
- git 1:2.40.1-1 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1034835)
https://lore.kernel.org/lkml/xmqqa5yv3n93.fsf@gitster.g/
https://github.com/git/git/commit/29198213c9163c1d552ee2bdbf78d2b09ccc98b8 (v2.30.9)
https://github.com/git/git/commit/a5bb10fd5e74101e7c07da93e7c32bbe60f6173a (v2.30.9)
https://github.com/git/git/commit/e91cfe6085c4a61372d1f800b473b73b8d225d0d (v2.30.9)
https://github.com/git/git/commit/3bb3d6bac5f2b496dfa2862dc1a84cbfa9b4449a (v2.30.9)

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2024-32021?s=debian&n=git&ns=debian&t=deb&osn=debian&osv=12&vr=%3C1%3A2.39.5-0%2Bdeb12u1"><img alt="low : CVE--2024--32021" src="https://img.shields.io/badge/CVE--2024--32021-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code><1:2.39.5-0+deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><code>1:2.39.5-0+deb12u1</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.045%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>18th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

Git is a revision control system. Prior to versions 2.45.1, 2.44.1, 2.43.4, 2.42.2, 2.41.1, 2.40.2, and 2.39.4, when cloning a local source repository that contains symlinks via the filesystem, Git may create hardlinks to arbitrary user-readable files on the same filesystem as the target repository in the `objects/` directory. Cloning a local repository over the filesystem may creating hardlinks to arbitrary user-owned files on the same filesystem in the target Git repository's `objects/` directory. When cloning a repository over the filesystem (without explicitly specifying the `file://` protocol or `--no-local`), the optimizations for local cloning will be used, which include attempting to hard link the object files instead of copying them. While the code includes checks against symbolic links in the source repository, which were added during the fix for CVE-2022-39253, these checks can still be raced because the hard link operation ultimately follows symlinks. If the object on the filesystem appears as a file during the check, and then a symlink during the operation, this will allow the adversary to bypass the check and create hardlinks in the destination objects directory to arbitrary, user-readable files. The problem has been patched in versions 2.45.1, 2.44.1, 2.43.4, 2.42.2, 2.41.1, 2.40.2, and 2.39.4.

---
- git 1:2.45.1-1 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1071160)
https://github.com/git/git/security/advisories/GHSA-mvxm-9j2h-qjx7

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2024-32020?s=debian&n=git&ns=debian&t=deb&osn=debian&osv=12&vr=%3C1%3A2.39.5-0%2Bdeb12u1"><img alt="low : CVE--2024--32020" src="https://img.shields.io/badge/CVE--2024--32020-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code><1:2.39.5-0+deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><code>1:2.39.5-0+deb12u1</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.045%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>18th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

Git is a revision control system. Prior to versions 2.45.1, 2.44.1, 2.43.4, 2.42.2, 2.41.1, 2.40.2, and 2.39.4, local clones may end up hardlinking files into the target repository's object database when source and target repository reside on the same disk. If the source repository is owned by a different user, then those hardlinked files may be rewritten at any point in time by the untrusted user. Cloning local repositories will cause Git to either copy or hardlink files of the source repository into the target repository. This significantly speeds up such local clones compared to doing a "proper" clone and saves both disk space and compute time. When cloning a repository located on the same disk that is owned by a different user than the current user we also end up creating such hardlinks. These files will continue to be owned and controlled by the potentially-untrusted user and can be rewritten by them at will in the future. The problem has been patched in versions 2.45.1, 2.44.1, 2.43.4, 2.42.2, 2.41.1, 2.40.2, and 2.39.4.

---
- git 1:2.45.1-1 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1071160)
[bullseye] - git <ignored> (regression problem deemed too problematic)
https://github.com/git/git/security/advisories/GHSA-5rfh-556j-fhgj
https://github.com/git/git/commit/1204e1a824c34071019fe106348eaa6d88f9528d
https://github.com/git/git/commit/9e65df5eab274bf74c7b570107aacd1303a1e703
Regression: https://lore.kernel.org/git/924426.1716570031@dash.ant.isi.edu/T/#u
Bullseye discussion here: https://lists.debian.org/debian-lts/2024/05/msg00017.html
and here: https://lists.debian.org/debian-lts/2024/10/msg00015.html

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2023-25815?s=debian&n=git&ns=debian&t=deb&osn=debian&osv=12&vr=%3C1%3A2.39.5-0%2Bdeb12u1"><img alt="low : CVE--2023--25815" src="https://img.shields.io/badge/CVE--2023--25815-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code><1:2.39.5-0+deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><code>1:2.39.5-0+deb12u1</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.049%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>21st percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

In Git for Windows, the Windows port of Git, no localized messages are shipped with the installer. As a consequence, Git is expected not to localize messages at all, and skips the gettext initialization. However, due to a change in MINGW-packages, the `gettext()` function's implicit initialization no longer uses the runtime prefix but uses the hard-coded path `C:\mingw64\share\locale` to look for localized messages. And since any authenticated user has the permission to create folders in `C:\` (and since `C:\mingw64` does not typically exist), it is possible for low-privilege users to place fake messages in that location where `git.exe` will pick them up in version 2.40.1.  This vulnerability is relatively hard to exploit and requires social engineering. For example, a legitimate message at the end of a clone could be maliciously modified to ask the user to direct their web browser to a malicious website, and the user might think that the message comes from Git and is legitimate. It does require local write access by the attacker, though, which makes this attack vector less likely. Version 2.40.1 contains a patch for this issue. Some workarounds are available. Do not work on a Windows machine with shared accounts, or alternatively create a `C:\mingw64` folder and leave it empty. Users who have administrative rights may remove the permission to create folders in `C:\`.

---
- git 1:2.40.1-1 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1034835)
https://lore.kernel.org/lkml/xmqqa5yv3n93.fsf@gitster.g/
https://github.com/git/git/commit/c4137be0f5a6edf9a9044e6e43ecf4468c7a4046 (v2.30.9)

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2024-52006?s=debian&n=git&ns=debian&t=deb&osn=debian&osv=12&vr=%3C1%3A2.39.5-0%2Bdeb12u2"><img alt="low : CVE--2024--52006" src="https://img.shields.io/badge/CVE--2024--52006-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code><1:2.39.5-0+deb12u2</code></td></tr>
<tr><td>Fixed version</td><td><code>1:2.39.5-0+deb12u2</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.045%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>18th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

Git is a fast, scalable, distributed revision control system with an unusually rich command set that provides both high-level operations and full access to internals. Git defines a line-based protocol that is used to exchange information between Git and Git credential helpers. Some ecosystems (most notably, .NET and node.js) interpret single Carriage Return characters as newlines, which renders the protections against CVE-2020-5260 incomplete for credential helpers that treat Carriage Returns in this way. This issue has been addressed in commit `b01b9b8` which is included in release versions v2.48.1, v2.47.2, v2.46.3, v2.45.3, v2.44.3, v2.43.6, v2.42.4, v2.41.3, and v2.40.4. Users are advised to upgrade. Users unable to upgrade should avoid cloning from untrusted URLs, especially recursive clones.

---
- git 1:2.47.2-0.1 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1093042)
https://www.openwall.com/lists/oss-security/2025/01/14/4
Fixed by: https://github.com/git/git/commit/b01b9b81d36759cdcd07305e78765199e1bc2060 (v2.40.4)

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2024-50349?s=debian&n=git&ns=debian&t=deb&osn=debian&osv=12&vr=%3C1%3A2.39.5-0%2Bdeb12u2"><img alt="low : CVE--2024--50349" src="https://img.shields.io/badge/CVE--2024--50349-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code><1:2.39.5-0+deb12u2</code></td></tr>
<tr><td>Fixed version</td><td><code>1:2.39.5-0+deb12u2</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.045%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>18th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

Git is a fast, scalable, distributed revision control system with an unusually rich command set that provides both high-level operations and full access to internals. When Git asks for credentials via a terminal prompt (i.e. without using any credential helper), it prints out the host name for which the user is expected to provide a username and/or a password. At this stage, any URL-encoded parts have been decoded already, and are printed verbatim. This allows attackers to craft URLs that contain ANSI escape sequences that the terminal interpret to confuse users e.g. into providing passwords for trusted Git hosting sites when in fact they are then sent to untrusted sites that are under the attacker's control. This issue has been patch via commits `7725b81` and `c903985` which are included in release versions v2.48.1, v2.47.2, v2.46.3, v2.45.3, v2.44.3, v2.43.6, v2.42.4, v2.41.3, and v2.40.4. Users are advised to upgrade. Users unable to upgrade should avoid cloning from untrusted URLs, especially recursive clones.

---
- git 1:2.47.2-0.1 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1093042)
https://www.openwall.com/lists/oss-security/2025/01/14/4
Fixed by: https://github.com/git/git/commit/c903985bf7e772e2d08275c1a95c8a55ab011577 (v2.40.4)
Fixed by: https://github.com/git/git/commit/7725b8100ffbbff2750ee4d61a0fcc1f53a086e8 (v2.40.4)

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 1" src="https://img.shields.io/badge/C-1-8b1924"/> <img alt="high: 1" src="https://img.shields.io/badge/H-1-e25d68"/> <img alt="medium: 5" src="https://img.shields.io/badge/M-5-fbb552"/> <img alt="low: 6" src="https://img.shields.io/badge/L-6-fce1a9"/> <img alt="unspecified: 1" src="https://img.shields.io/badge/U-1-lightgrey"/><strong>openssl</strong> <code>3.0.9-1</code> (deb)</summary>

<small><code>pkg:deb/debian/openssl@3.0.9-1?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2024-5535?s=debian&n=openssl&ns=debian&t=deb&osn=debian&osv=12&vr=%3C3.0.15-1%7Edeb12u1"><img alt="critical : CVE--2024--5535" src="https://img.shields.io/badge/CVE--2024--5535-lightgrey?label=critical%20&labelColor=8b1924"/></a> 

<table>
<tr><td>Affected range</td><td><code><3.0.15-1~deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><code>3.0.15-1~deb12u1</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.044%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>16th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

Issue summary: Calling the OpenSSL API function SSL_select_next_proto with an empty supported client protocols buffer may cause a crash or memory contents to be sent to the peer.  Impact summary: A buffer overread can have a range of potential consequences such as unexpected application beahviour or a crash. In particular this issue could result in up to 255 bytes of arbitrary private data from memory being sent to the peer leading to a loss of confidentiality. However, only applications that directly call the SSL_select_next_proto function with a 0 length list of supported client protocols are affected by this issue. This would normally never be a valid scenario and is typically not under attacker control but may occur by accident in the case of a configuration or programming error in the calling application.  The OpenSSL API function SSL_select_next_proto is typically used by TLS applications that support ALPN (Application Layer Protocol Negotiation) or NPN (Next Protocol Negotiation). NPN is older, was never standardised and is deprecated in favour of ALPN. We believe that ALPN is significantly more widely deployed than NPN. The SSL_select_next_proto function accepts a list of protocols from the server and a list of protocols from the client and returns the first protocol that appears in the server list that also appears in the client list. In the case of no overlap between the two lists it returns the first item in the client list. In either case it will signal whether an overlap between the two lists was found. In the case where SSL_select_next_proto is called with a zero length client list it fails to notice this condition and returns the memory immediately following the client list pointer (and reports that there was no overlap in the lists).  This function is typically called from a server side application callback for ALPN or a client side application callback for NPN. In the case of ALPN the list of protocols supplied by the client is guaranteed by libssl to never be zero in length. The list of server protocols comes from the application and should never normally be expected to be of zero length. In this case if the SSL_select_next_proto function has been called as expected (with the list supplied by the client passed in the client/client_len parameters), then the application will not be vulnerable to this issue. If the application has accidentally been configured with a zero length server list, and has accidentally passed that zero length server list in the client/client_len parameters, and has additionally failed to correctly handle a "no overlap" response (which would normally result in a handshake failure in ALPN) then it will be vulnerable to this problem.  In the case of NPN, the protocol permits the client to opportunistically select a protocol when there is no overlap. OpenSSL returns the first client protocol in the no overlap case in support of this. The list of client protocols comes from the application and should never normally be expected to be of zero length. However if the SSL_select_next_proto function is accidentally called with a client_len of 0 then an invalid memory pointer will be returned instead. If the application uses this output as the opportunistic protocol then the loss of confidentiality will occur.  This issue has been assessed as Low severity because applications are most likely to be vulnerable if they are using NPN instead of ALPN - but NPN is not widely used. It also requires an application configuration or programming error. Finally, this issue would not typically be under attacker control making active exploitation unlikely.  The FIPS modules in 3.3, 3.2, 3.1 and 3.0 are not affected by this issue.  Due to the low severity of this issue we are not issuing new releases of OpenSSL at this time. The fix will be included in the next releases when they become available.

---
- openssl 3.3.2-1 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1074487)
[bookworm] - openssl 3.0.15-1~deb12u1
https://www.openssl.org/news/secadv/20240627.txt
https://github.com/openssl/openssl/commit/2ebbe2d7ca8551c4cb5fbb391ab9af411708090e
https://github.com/openssl/openssl/commit/c6e1ea223510bb7104bf0c41c0c45eda5a16b718
https://github.com/openssl/openssl/commit/fc8ff75814767d6c55ea78d05adc72cd346d0f0a
https://github.com/openssl/openssl/commit/a210f580f450bbd08fac85f06e27107b8c580f9b
https://github.com/openssl/openssl/commit/0d883f6309b6905d29ffded6d703ded39385579c
https://github.com/openssl/openssl/commit/9925c97a8e8c9887765a0979c35b516bc8c3af85
https://github.com/openssl/openssl/commit/e10a3a84bf73a3e6024c338b51f2fb4e78a3dee9
https://github.com/openssl/openssl/commit/238fa464d6e38aa2c92af70ef9580c74cff512e4
https://github.com/openssl/openssl/commit/de71058567b84c6e14b758a383e1862eb3efb921
https://github.com/openssl/openssl/commit/214c724e00d594c3eecf4b740ee7af772f0ee04a

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2024-4741?s=debian&n=openssl&ns=debian&t=deb&osn=debian&osv=12&vr=%3C3.0.14-1%7Edeb12u1"><img alt="high : CVE--2024--4741" src="https://img.shields.io/badge/CVE--2024--4741-lightgrey?label=high%20&labelColor=e25d68"/></a> 

<table>
<tr><td>Affected range</td><td><code><3.0.14-1~deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><code>3.0.14-1~deb12u1</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.044%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>13th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

Issue summary: Calling the OpenSSL API function SSL_free_buffers may cause memory to be accessed that was previously freed in some situations  Impact summary: A use after free can have a range of potential consequences such as the corruption of valid data, crashes or execution of arbitrary code. However, only applications that directly call the SSL_free_buffers function are affected by this issue. Applications that do not call this function are not vulnerable. Our investigations indicate that this function is rarely used by applications.  The SSL_free_buffers function is used to free the internal OpenSSL buffer used when processing an incoming record from the network. The call is only expected to succeed if the buffer is not currently in use. However, two scenarios have been identified where the buffer is freed even when still in use.  The first scenario occurs where a record header has been received from the network and processed by OpenSSL, but the full record body has not yet arrived. In this case calling SSL_free_buffers will succeed even though a record has only been partially processed and the buffer is still in use.  The second scenario occurs where a full record containing application data has been received and processed by OpenSSL but the application has only read part of this data. Again a call to SSL_free_buffers will succeed even though the buffer is still in use.  While these scenarios could occur accidentally during normal operation a malicious attacker could attempt to engineer a stituation where this occurs. We are not aware of this issue being actively exploited.  The FIPS modules in 3.3, 3.2, 3.1 and 3.0 are not affected by this issue.

---
- openssl 3.2.2-1 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1072113)
[bookworm] - openssl 3.0.14-1~deb12u1
[buster] - openssl <postponed> (Minor issue, fix along with next update round)
https://www.openssl.org/news/secadv/20240528.txt
https://github.com/openssl/openssl/commit/c1bd38a003fa19fd0d8ade85e1bbc20d8ae59dab (master)
https://github.com/openssl/openssl/commit/c88c3de51020c37e8706bf7a682a162593053aac (openssl-3.2)
https://github.com/openssl/openssl/commit/b3f0eb0a295f58f16ba43ba99dad70d4ee5c437d (openssl-3.0)

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2024-0727?s=debian&n=openssl&ns=debian&t=deb&osn=debian&osv=12&vr=%3C3.0.13-1%7Edeb12u1"><img alt="medium : CVE--2024--0727" src="https://img.shields.io/badge/CVE--2024--0727-lightgrey?label=medium%20&labelColor=fbb552"/></a> 

<table>
<tr><td>Affected range</td><td><code><3.0.13-1~deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><code>3.0.13-1~deb12u1</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.228%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>61st percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

Issue summary: Processing a maliciously formatted PKCS12 file may lead OpenSSL to crash leading to a potential Denial of Service attack  Impact summary: Applications loading files in the PKCS12 format from untrusted sources might terminate abruptly.  A file in PKCS12 format can contain certificates and keys and may come from an untrusted source. The PKCS12 specification allows certain fields to be NULL, but OpenSSL does not correctly check for this case. This can lead to a NULL pointer dereference that results in OpenSSL crashing. If an application processes PKCS12 files from an untrusted source using the OpenSSL APIs then that application will be vulnerable to this issue.  OpenSSL APIs that are vulnerable to this are: PKCS12_parse(), PKCS12_unpack_p7data(), PKCS12_unpack_p7encdata(), PKCS12_unpack_authsafes() and PKCS12_newpass().  We have also fixed a similar issue in SMIME_write_PKCS7(). However since this function is related to writing data we do not consider it security significant.  The FIPS modules in 3.2, 3.1 and 3.0 are not affected by this issue.

---
- openssl 3.1.5-1 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1061582)
[bookworm] - openssl 3.0.13-1~deb12u1
[buster] - openssl <postponed> (Minor issue, DoS, Low severity)
https://www.openssl.org/news/secadv/20240125.txt
https://github.com/openssl/openssl/commit/041962b429ebe748c8b6b7922980dfb6decfef26 (master)
https://github.com/openssl/openssl/commit/8a85df7c60ba1372ee98acc5982e902d75f52130 (master)
https://github.com/openssl/openssl/commit/d135eeab8a5dbf72b3da5240bab9ddb7678dbd2c (openssl-3.1.5)
https://github.com/openssl/openssl/commit/febb086d0fc1ea12181f4d833aa9b8fdf2133b3b (openssl-3.1.5)

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2023-5678?s=debian&n=openssl&ns=debian&t=deb&osn=debian&osv=12&vr=%3C3.0.13-1%7Edeb12u1"><img alt="medium : CVE--2023--5678" src="https://img.shields.io/badge/CVE--2023--5678-lightgrey?label=medium%20&labelColor=fbb552"/></a> 

<table>
<tr><td>Affected range</td><td><code><3.0.13-1~deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><code>3.0.13-1~deb12u1</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.140%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>51st percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

Issue summary: Generating excessively long X9.42 DH keys or checking excessively long X9.42 DH keys or parameters may be very slow.  Impact summary: Applications that use the functions DH_generate_key() to generate an X9.42 DH key may experience long delays.  Likewise, applications that use DH_check_pub_key(), DH_check_pub_key_ex() or EVP_PKEY_public_check() to check an X9.42 DH key or X9.42 DH parameters may experience long delays. Where the key or parameters that are being checked have been obtained from an untrusted source this may lead to a Denial of Service.  While DH_check() performs all the necessary checks (as of CVE-2023-3817), DH_check_pub_key() doesn't make any of these checks, and is therefore vulnerable for excessively large P and Q parameters.  Likewise, while DH_generate_key() performs a check for an excessively large P, it doesn't check for an excessively large Q.  An application that calls DH_generate_key() or DH_check_pub_key() and supplies a key or parameters obtained from an untrusted source could be vulnerable to a Denial of Service attack.  DH_generate_key() and DH_check_pub_key() are also called by a number of other OpenSSL functions.  An application calling any of those other functions may similarly be affected.  The other functions affected by this are DH_check_pub_key_ex(), EVP_PKEY_public_check(), and EVP_PKEY_generate().  Also vulnerable are the OpenSSL pkey command line application when using the "-pubcheck" option, as well as the OpenSSL genpkey command line application.  The OpenSSL SSL/TLS implementation is not affected by this issue.  The OpenSSL 3.0 and 3.1 FIPS providers are not affected by this issue.

---
- openssl 3.0.12-2 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1055473)
[bookworm] - openssl 3.0.13-1~deb12u1
[buster] - openssl <postponed> (Minor issue; can be fixed along with future update)
https://www.openssl.org/news/secadv/20231106.txt
https://git.openssl.org/gitweb/?p=openssl.git;a=commitdiff;h=db925ae2e65d0d925adef429afc37f75bd1c2017 (for 3.0.y)
https://git.openssl.org/gitweb/?p=openssl.git;a=commitdiff;h=710fee740904b6290fef0dd5536fbcedbc38ff0c (for 1.1.1y)

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2023-3817?s=debian&n=openssl&ns=debian&t=deb&osn=debian&osv=12&vr=%3C3.0.10-1%7Edeb12u1"><img alt="medium : CVE--2023--3817" src="https://img.shields.io/badge/CVE--2023--3817-lightgrey?label=medium%20&labelColor=fbb552"/></a> 

<table>
<tr><td>Affected range</td><td><code><3.0.10-1~deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><code>3.0.10-1~deb12u1</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.263%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>66th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

Issue summary: Checking excessively long DH keys or parameters may be very slow.  Impact summary: Applications that use the functions DH_check(), DH_check_ex() or EVP_PKEY_param_check() to check a DH key or DH parameters may experience long delays. Where the key or parameters that are being checked have been obtained from an untrusted source this may lead to a Denial of Service.  The function DH_check() performs various checks on DH parameters. After fixing CVE-2023-3446 it was discovered that a large q parameter value can also trigger an overly long computation during some of these checks. A correct q value, if present, cannot be larger than the modulus p parameter, thus it is unnecessary to perform these checks if q is larger than p.  An application that calls DH_check() and supplies a key or parameters obtained from an untrusted source could be vulnerable to a Denial of Service attack.  The function DH_check() is itself called by a number of other OpenSSL functions. An application calling any of those other functions may similarly be affected. The other functions affected by this are DH_check_ex() and EVP_PKEY_param_check().  Also vulnerable are the OpenSSL dhparam and pkeyparam command line applications when using the "-check" option.  The OpenSSL SSL/TLS implementation is not affected by this issue.  The OpenSSL 3.0 and 3.1 FIPS providers are not affected by this issue.

---
- openssl 3.0.10-1
[bookworm] - openssl 3.0.10-1~deb12u1
[bullseye] - openssl 1.1.1v-0~deb11u1
https://www.openssl.org/news/secadv/20230731.txt
https://www.openwall.com/lists/oss-security/2023/07/31/1
https://git.openssl.org/gitweb/?p=openssl.git;a=commitdiff;h=1c16253f3c3a8d1e25918c3f404aae6a5b0893de (master)
https://git.openssl.org/gitweb/?p=openssl.git;a=commitdiff;h=6a1eb62c29db6cb5eec707f9338aee00f44e26f5 (openssl-3.1.2)
https://git.openssl.org/gitweb/?p=openssl.git;a=commitdiff;h=9002fd07327a91f35ba6c1307e71fa6fd4409b7f (openssl-3.0.10)
https://git.openssl.org/gitweb/?p=openssl.git;a=commitdiff;h=91ddeba0f2269b017dc06c46c993a788974b1aa5 (OpenSSL_1_1_1v)

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2023-3446?s=debian&n=openssl&ns=debian&t=deb&osn=debian&osv=12&vr=%3C3.0.10-1%7Edeb12u1"><img alt="medium : CVE--2023--3446" src="https://img.shields.io/badge/CVE--2023--3446-lightgrey?label=medium%20&labelColor=fbb552"/></a> 

<table>
<tr><td>Affected range</td><td><code><3.0.10-1~deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><code>3.0.10-1~deb12u1</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.266%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>68th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

Issue summary: Checking excessively long DH keys or parameters may be very slow.  Impact summary: Applications that use the functions DH_check(), DH_check_ex() or EVP_PKEY_param_check() to check a DH key or DH parameters may experience long delays. Where the key or parameters that are being checked have been obtained from an untrusted source this may lead to a Denial of Service.  The function DH_check() performs various checks on DH parameters. One of those checks confirms that the modulus ('p' parameter) is not too large. Trying to use a very large modulus is slow and OpenSSL will not normally use a modulus which is over 10,000 bits in length.  However the DH_check() function checks numerous aspects of the key or parameters that have been supplied. Some of those checks use the supplied modulus value even if it has already been found to be too large.  An application that calls DH_check() and supplies a key or parameters obtained from an untrusted source could be vulernable to a Denial of Service attack.  The function DH_check() is itself called by a number of other OpenSSL functions. An application calling any of those other functions may similarly be affected. The other functions affected by this are DH_check_ex() and EVP_PKEY_param_check().  Also vulnerable are the OpenSSL dhparam and pkeyparam command line applications when using the '-check' option.  The OpenSSL SSL/TLS implementation is not affected by this issue. The OpenSSL 3.0 and 3.1 FIPS providers are not affected by this issue.

---
- openssl 3.0.10-1 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1041817)
[bookworm] - openssl 3.0.10-1~deb12u1
[bullseye] - openssl 1.1.1v-0~deb11u1
https://www.openssl.org/news/secadv/20230719.txt
https://github.com/openssl/openssl/commit/9e0094e2aa1b3428a12d5095132f133c078d3c3d (master)
https://github.com/openssl/openssl/commit/1fa20cf2f506113c761777127a38bce5068740eb (openssl-3.0.10)
https://github.com/openssl/openssl/commit/8780a896543a654e757db1b9396383f9d8095528 (OpenSSL_1_1_1v)

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2024-9143?s=debian&n=openssl&ns=debian&t=deb&osn=debian&osv=12&vr=%3C3.0.15-1%7Edeb12u1"><img alt="medium : CVE--2024--9143" src="https://img.shields.io/badge/CVE--2024--9143-lightgrey?label=medium%20&labelColor=fbb552"/></a> 

<table>
<tr><td>Affected range</td><td><code><3.0.15-1~deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><code>3.0.15-1~deb12u1</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.044%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>13th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

Issue summary: Use of the low-level GF(2^m) elliptic curve APIs with untrusted explicit values for the field polynomial can lead to out-of-bounds memory reads or writes.  Impact summary: Out of bound memory writes can lead to an application crash or even a possibility of a remote code execution, however, in all the protocols involving Elliptic Curve Cryptography that we're aware of, either only "named curves" are supported, or, if explicit curve parameters are supported, they specify an X9.62 encoding of binary (GF(2^m)) curves that can't represent problematic input values. Thus the likelihood of existence of a vulnerable application is low.  In particular, the X9.62 encoding is used for ECC keys in X.509 certificates, so problematic inputs cannot occur in the context of processing X.509 certificates.  Any problematic use-cases would have to be using an "exotic" curve encoding.  The affected APIs include: EC_GROUP_new_curve_GF2m(), EC_GROUP_new_from_params(), and various supporting BN_GF2m_*() functions.  Applications working with "exotic" explicit binary (GF(2^m)) curve parameters, that make it possible to represent invalid field polynomials with a zero constant term, via the above or similar APIs, may terminate abruptly as a result of reading or writing outside of array bounds.  Remote code execution cannot easily be ruled out.  The FIPS modules in 3.3, 3.2, 3.1 and 3.0 are not affected by this issue.

---
[experimental] - openssl 3.4.0-1
- openssl 3.3.2-2 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1085378)
[bookworm] - openssl 3.0.15-1~deb12u1
https://openssl-library.org/news/secadv/20241016.txt
https://github.com/openssl/openssl/commit/c0d3e4d32d2805f49bec30547f225bc4d092e1f4 (openssl-3.3)
https://github.com/openssl/openssl/commit/72ae83ad214d2eef262461365a1975707f862712 (openssl-3.0)

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2024-6119?s=debian&n=openssl&ns=debian&t=deb&osn=debian&osv=12&vr=%3C3.0.14-1%7Edeb12u2"><img alt="low : CVE--2024--6119" src="https://img.shields.io/badge/CVE--2024--6119-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code><3.0.14-1~deb12u2</code></td></tr>
<tr><td>Fixed version</td><td><code>3.0.14-1~deb12u2</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.045%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>18th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

Issue summary: Applications performing certificate name checks (e.g., TLS clients checking server certificates) may attempt to read an invalid memory address resulting in abnormal termination of the application process.  Impact summary: Abnormal termination of an application can a cause a denial of service.  Applications performing certificate name checks (e.g., TLS clients checking server certificates) may attempt to read an invalid memory address when comparing the expected name with an `otherName` subject alternative name of an X.509 certificate. This may result in an exception that terminates the application program.  Note that basic certificate chain validation (signatures, dates, ...) is not affected, the denial of service can occur only when the application also specifies an expected DNS name, Email address or IP address.  TLS servers rarely solicit client certificates, and even when they do, they generally don't perform a name check against a reference identifier (expected identity), but rather extract the presented identity after checking the certificate chain.  So TLS servers are generally not affected and the severity of the issue is Moderate.  The FIPS modules in 3.3, 3.2, 3.1 and 3.0 are not affected by this issue.

---
- openssl 3.3.2-1
[bullseye] - openssl <not-affected> (Vulnerable code not present)
https://openssl-library.org/news/secadv/20240903.txt
https://github.com/openssl/openssl/commit/06d1dc3fa96a2ba5a3e22735a033012aadc9f0d6 (openssl-3.0.15)

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2024-4603?s=debian&n=openssl&ns=debian&t=deb&osn=debian&osv=12&vr=%3C3.0.14-1%7Edeb12u1"><img alt="low : CVE--2024--4603" src="https://img.shields.io/badge/CVE--2024--4603-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code><3.0.14-1~deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><code>3.0.14-1~deb12u1</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.045%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>18th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

Issue summary: Checking excessively long DSA keys or parameters may be very slow.  Impact summary: Applications that use the functions EVP_PKEY_param_check() or EVP_PKEY_public_check() to check a DSA public key or DSA parameters may experience long delays. Where the key or parameters that are being checked have been obtained from an untrusted source this may lead to a Denial of Service.  The functions EVP_PKEY_param_check() or EVP_PKEY_public_check() perform various checks on DSA parameters. Some of those computations take a long time if the modulus (`p` parameter) is too large.  Trying to use a very large modulus is slow and OpenSSL will not allow using public keys with a modulus which is over 10,000 bits in length for signature verification. However the key and parameter check functions do not limit the modulus size when performing the checks.  An application that calls EVP_PKEY_param_check() or EVP_PKEY_public_check() and supplies a key or parameters obtained from an untrusted source could be vulnerable to a Denial of Service attack.  These functions are not called by OpenSSL itself on untrusted DSA keys so only applications that directly call these functions may be vulnerable.  Also vulnerable are the OpenSSL pkey and pkeyparam command line applications when using the `-check` option.  The OpenSSL SSL/TLS implementation is not affected by this issue.  The OpenSSL 3.0 and 3.1 FIPS providers are affected by this issue.

---
- openssl 3.2.2-1 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1071972)
[bookworm] - openssl 3.0.14-1~deb12u1
[bullseye] - openssl <not-affected> (Vulnerable code not present)
[buster] - openssl <not-affected> (Vulnerable code not present)
https://www.openssl.org/news/secadv/20240516.txt
https://github.com/openssl/openssl/commit/da343d0605c826ef197aceedc67e8e04f065f740 (openssl-3.2)
https://github.com/openssl/openssl/commit/9c39b3858091c152f52513c066ff2c5a47969f0d (openssl-3.1)
https://github.com/openssl/openssl/commit/3559e868e58005d15c6013a0c1fd832e51c73397 (openssl-3.0)

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2023-6237?s=debian&n=openssl&ns=debian&t=deb&osn=debian&osv=12&vr=%3C3.0.13-1%7Edeb12u1"><img alt="low : CVE--2023--6237" src="https://img.shields.io/badge/CVE--2023--6237-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code><3.0.13-1~deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><code>3.0.13-1~deb12u1</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.045%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>18th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

Issue summary: Checking excessively long invalid RSA public keys may take a long time.  Impact summary: Applications that use the function EVP_PKEY_public_check() to check RSA public keys may experience long delays. Where the key that is being checked has been obtained from an untrusted source this may lead to a Denial of Service.  When function EVP_PKEY_public_check() is called on RSA public keys, a computation is done to confirm that the RSA modulus, n, is composite. For valid RSA keys, n is a product of two or more large primes and this computation completes quickly. However, if n is an overly large prime, then this computation would take a long time.  An application that calls EVP_PKEY_public_check() and supplies an RSA key obtained from an untrusted source could be vulnerable to a Denial of Service attack.  The function EVP_PKEY_public_check() is not called from other OpenSSL functions however it is called from the OpenSSL pkey command line application. For that reason that application is also vulnerable if used with the '-pubin' and '-check' options on untrusted data.  The OpenSSL SSL/TLS implementation is not affected by this issue.  The OpenSSL 3.0 and 3.1 FIPS providers are affected by this issue.

---
- openssl 3.1.5-1 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1060858)
[bookworm] - openssl 3.0.13-1~deb12u1
[bullseye] - openssl <not-affected> (Only affects 3.x)
[buster] - openssl <not-affected> (Only affects 3.x)
https://www.openssl.org/news/secadv/20240115.txt
https://github.com/openssl/openssl/commit/e09fc1d746a4fd15bb5c3d7bbbab950aadd005db
https://git.openssl.org/gitweb/?p=openssl.git;a=commitdiff;h=a830f551557d3d66a84bbb18a5b889c640c36294 (openssl-3.1)
https://git.openssl.org/gitweb/?p=openssl.git;a=commitdiff;h=18c02492138d1eb8b6548cb26e7b625fb2414a2a (openssl-3.0)

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2023-6129?s=debian&n=openssl&ns=debian&t=deb&osn=debian&osv=12&vr=%3C3.0.13-1%7Edeb12u1"><img alt="low : CVE--2023--6129" src="https://img.shields.io/badge/CVE--2023--6129-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code><3.0.13-1~deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><code>3.0.13-1~deb12u1</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.126%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>48th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

Issue summary: The POLY1305 MAC (message authentication code) implementation contains a bug that might corrupt the internal state of applications running on PowerPC CPU based platforms if the CPU provides vector instructions.  Impact summary: If an attacker can influence whether the POLY1305 MAC algorithm is used, the application state might be corrupted with various application dependent consequences.  The POLY1305 MAC (message authentication code) implementation in OpenSSL for PowerPC CPUs restores the contents of vector registers in a different order than they are saved. Thus the contents of some of these vector registers are corrupted when returning to the caller. The vulnerable code is used only on newer PowerPC processors supporting the PowerISA 2.07 instructions.  The consequences of this kind of internal application state corruption can be various - from no consequences, if the calling application does not depend on the contents of non-volatile XMM registers at all, to the worst consequences, where the attacker could get complete control of the application process. However unless the compiler uses the vector registers for storing pointers, the most likely consequence, if any, would be an incorrect result of some application dependent calculations or a crash leading to a denial of service.  The POLY1305 MAC algorithm is most frequently used as part of the CHACHA20-POLY1305 AEAD (authenticated encryption with associated data) algorithm. The most common usage of this AEAD cipher is with TLS protocol versions 1.2 and 1.3. If this cipher is enabled on the server a malicious client can influence whether this AEAD cipher is used. This implies that TLS server applications using OpenSSL can be potentially impacted. However we are currently not aware of any concrete application that would be affected by this issue therefore we consider this a Low severity security issue.

---
- openssl 3.1.5-1 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1060347)
[bookworm] - openssl 3.0.13-1~deb12u1
[bullseye] - openssl <not-affected> (Vulnerable code not present)
[buster] - openssl <not-affected> (Vulnerable code not present)
https://www.openwall.com/lists/oss-security/2024/01/09/1
https://www.openssl.org/news/secadv/20240109.txt
https://git.openssl.org/gitweb/?p=openssl.git;a=commitdiff;h=f3fc5808fe9ff74042d639839610d03b8fdcc015 (openssl-3.1)
https://git.openssl.org/gitweb/?p=openssl.git;a=commitdiff;h=050d26383d4e264966fb83428e72d5d48f402d35 (openssl-3.0)

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2023-5363?s=debian&n=openssl&ns=debian&t=deb&osn=debian&osv=12&vr=%3C3.0.11-1%7Edeb12u2"><img alt="low : CVE--2023--5363" src="https://img.shields.io/badge/CVE--2023--5363-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code><3.0.11-1~deb12u2</code></td></tr>
<tr><td>Fixed version</td><td><code>3.0.11-1~deb12u2</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.088%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>40th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

Issue summary: A bug has been identified in the processing of key and initialisation vector (IV) lengths.  This can lead to potential truncation or overruns during the initialisation of some symmetric ciphers.  Impact summary: A truncation in the IV can result in non-uniqueness, which could result in loss of confidentiality for some cipher modes.  When calling EVP_EncryptInit_ex2(), EVP_DecryptInit_ex2() or EVP_CipherInit_ex2() the provided OSSL_PARAM array is processed after the key and IV have been established.  Any alterations to the key length, via the "keylen" parameter or the IV length, via the "ivlen" parameter, within the OSSL_PARAM array will not take effect as intended, potentially causing truncation or overreading of these values.  The following ciphers and cipher modes are impacted: RC2, RC4, RC5, CCM, GCM and OCB.  For the CCM, GCM and OCB cipher modes, truncation of the IV can result in loss of confidentiality.  For example, when following NIST's SP 800-38D section 8.2.1 guidance for constructing a deterministic IV for AES in GCM mode, truncation of the counter portion could lead to IV reuse.  Both truncations and overruns of the key and overruns of the IV will produce incorrect results and could, in some cases, trigger a memory exception.  However, these issues are not currently assessed as security critical.  Changing the key and/or IV lengths is not considered to be a common operation and the vulnerable API was recently introduced. Furthermore it is likely that application developers will have spotted this problem during testing since decryption would fail unless both peers in the communication were similarly vulnerable. For these reasons we expect the probability of an application being vulnerable to this to be quite low. However if an application is vulnerable then this issue is considered very serious. For these reasons we have assessed this issue as Moderate severity overall.  The OpenSSL SSL/TLS implementation is not affected by this issue.  The OpenSSL 3.0 and 3.1 FIPS providers are not affected by this because the issue lies outside of the FIPS provider boundary.  OpenSSL 3.1 and 3.0 are vulnerable to this issue.

---
- openssl 3.0.12-1
[bullseye] - openssl <not-affected> (Vulnerable code not present)
[buster] - openssl <not-affected> (Vulnerable code not present)
https://www.openssl.org/news/secadv/20231024.txt

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2023-2975?s=debian&n=openssl&ns=debian&t=deb&osn=debian&osv=12&vr=%3C3.0.10-1%7Edeb12u1"><img alt="low : CVE--2023--2975" src="https://img.shields.io/badge/CVE--2023--2975-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code><3.0.10-1~deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><code>3.0.10-1~deb12u1</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.396%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>74th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

Issue summary: The AES-SIV cipher implementation contains a bug that causes it to ignore empty associated data entries which are unauthenticated as a consequence.  Impact summary: Applications that use the AES-SIV algorithm and want to authenticate empty data entries as associated data can be misled by removing, adding or reordering such empty entries as these are ignored by the OpenSSL implementation. We are currently unaware of any such applications.  The AES-SIV algorithm allows for authentication of multiple associated data entries along with the encryption. To authenticate empty data the application has to call EVP_EncryptUpdate() (or EVP_CipherUpdate()) with NULL pointer as the output buffer and 0 as the input buffer length. The AES-SIV implementation in OpenSSL just returns success for such a call instead of performing the associated data authentication operation. The empty data thus will not be authenticated.  As this issue does not affect non-empty associated data authentication and we expect it to be rare for an application to use empty associated data entries this is qualified as Low severity issue.

---
- openssl 3.0.10-1 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1041818)
[bookworm] - openssl 3.0.10-1~deb12u1
[bullseye] - openssl <not-affected> (Vulnerable code not present, only affects 3.x)
[buster] - openssl <not-affected> (Vulnerable code not present, only affects 3.x)
https://www.openssl.org/news/secadv/20230714.txt
Fixed by: https://git.openssl.org/gitweb/?p=openssl.git;a=commitdiff;h=00e2f5eea29994d19293ec4e8c8775ba73678598 (openssl-3.0.10)

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2024-2511?s=debian&n=openssl&ns=debian&t=deb&osn=debian&osv=12&vr=%3C3.0.14-1%7Edeb12u1"><img alt="unspecified : CVE--2024--2511" src="https://img.shields.io/badge/CVE--2024--2511-lightgrey?label=unspecified%20&labelColor=lightgrey"/></a> 

<table>
<tr><td>Affected range</td><td><code><3.0.14-1~deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><code>3.0.14-1~deb12u1</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.045%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>18th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

Issue summary: Some non-default TLS server configurations can cause unbounded memory growth when processing TLSv1.3 sessions  Impact summary: An attacker may exploit certain server configurations to trigger unbounded memory growth that would lead to a Denial of Service  This problem can occur in TLSv1.3 if the non-default SSL_OP_NO_TICKET option is being used (but not if early_data support is also configured and the default anti-replay protection is in use). In this case, under certain conditions, the session cache can get into an incorrect state and it will fail to flush properly as it fills. The session cache will continue to grow in an unbounded manner. A malicious client could deliberately create the scenario for this failure to force a Denial of Service. It may also happen by accident in normal operation.  This issue only affects TLS servers supporting TLSv1.3. It does not affect TLS clients.  The FIPS modules in 3.2, 3.1 and 3.0 are not affected by this issue. OpenSSL 1.0.2 is also not affected by this issue.

---
[experimental] - openssl 3.3.0-1
- openssl 3.2.2-1 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1068658)
[bookworm] - openssl 3.0.14-1~deb12u1
[buster] - openssl <postponed> (Minor issue, fix along with next update round)
https://www.openssl.org/news/secadv/20240408.txt
https://github.com/openssl/openssl/commit/e9d7083e241670332e0443da0f0d4ffb52829f08 (openssl-3.2.y)
https://github.com/openssl/openssl/commit/7e4d731b1c07201ad9374c1cd9ac5263bdf35bce (openssl-3.1.y)
https://github.com/openssl/openssl/commit/b52867a9f618bb955bed2a3ce3db4d4f97ed8e5d (openssl-3.0.y)

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 1" src="https://img.shields.io/badge/C-1-8b1924"/> <img alt="high: 1" src="https://img.shields.io/badge/H-1-e25d68"/> <img alt="medium: 4" src="https://img.shields.io/badge/M-4-fbb552"/> <img alt="low: 4" src="https://img.shields.io/badge/L-4-fce1a9"/> <!-- unspecified: 0 --><strong>curl</strong> <code>7.88.1-10</code> (deb)</summary>

<small><code>pkg:deb/debian/curl@7.88.1-10?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2023-38545?s=debian&n=curl&ns=debian&t=deb&osn=debian&osv=12&vr=%3C7.88.1-10%2Bdeb12u4"><img alt="critical : CVE--2023--38545" src="https://img.shields.io/badge/CVE--2023--38545-lightgrey?label=critical%20&labelColor=8b1924"/></a> 

<table>
<tr><td>Affected range</td><td><code><7.88.1-10+deb12u4</code></td></tr>
<tr><td>Fixed version</td><td><code>7.88.1-10+deb12u4</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.934%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>83rd percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

This flaw makes curl overflow a heap based buffer in the SOCKS5 proxy handshake.  When curl is asked to pass along the host name to the SOCKS5 proxy to allow that to resolve the address instead of it getting done by curl itself, the maximum length that host name can be is 255 bytes.  If the host name is detected to be longer, curl switches to local name resolving and instead passes on the resolved address only. Due to this bug, the local variable that means "let the host resolve the name" could get the wrong value during a slow SOCKS5 handshake, and contrary to the intention, copy the too long host name to the target buffer instead of copying just the resolved address there.  The target buffer being a heap based buffer, and the host name coming from the URL that curl has been told to operate with.

---
- curl 8.3.0-3
[buster] - curl <not-affected> (Vulnerable code not present)
https://curl.se/docs/CVE-2023-38545.html
Introduced by: https://github.com/curl/curl/commit/4a4b63daaa01ef59b131d91e8e6e6dfe275c0f08 (curl-7_69_0)
Fixed by: https://github.com/curl/curl/commit/fb4415d8aee6c1045be932a34fe6107c2f5ed147 (curl-8_4_0)
https://daniel.haxx.se/blog/2023/10/11/how-i-made-a-heap-overflow-in-curl/

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2024-2398?s=debian&n=curl&ns=debian&t=deb&osn=debian&osv=12&vr=%3C7.88.1-10%2Bdeb12u6"><img alt="high : CVE--2024--2398" src="https://img.shields.io/badge/CVE--2024--2398-lightgrey?label=high%20&labelColor=e25d68"/></a> 

<table>
<tr><td>Affected range</td><td><code><7.88.1-10+deb12u6</code></td></tr>
<tr><td>Fixed version</td><td><code>7.88.1-10+deb12u6</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.046%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>20th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

When an application tells libcurl it wants to allow HTTP/2 server push, and the amount of received headers for the push surpasses the maximum allowed limit (1000), libcurl aborts the server push. When aborting, libcurl inadvertently does not free all the previously allocated headers and instead leaks the memory.  Further, this error condition fails silently and is therefore not easily detected by an application.

---
- curl 8.7.1-1
[bookworm] - curl 7.88.1-10+deb12u6
[bullseye] - curl 7.74.0-1.3+deb11u12
[buster] - curl <postponed> (Minor issue; can be fixed in next update)
https://curl.se/docs/CVE-2024-2398.html
Introduced by: https://github.com/curl/curl/commit/ea7134ac874a66107e54ff93657ac565cf2ec4aa (curl-7_44_0)
Fixed by: https://github.com/curl/curl/commit/deca8039991886a559b67bcd6701db800a5cf764 (curl-8_7_0)

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2024-8096?s=debian&n=curl&ns=debian&t=deb&osn=debian&osv=12&vr=%3C7.88.1-10%2Bdeb12u8"><img alt="medium : CVE--2024--8096" src="https://img.shields.io/badge/CVE--2024--8096-lightgrey?label=medium%20&labelColor=fbb552"/></a> 

<table>
<tr><td>Affected range</td><td><code><7.88.1-10+deb12u8</code></td></tr>
<tr><td>Fixed version</td><td><code>7.88.1-10+deb12u8</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.045%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>18th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

When curl is told to use the Certificate Status Request TLS extension, often referred to as OCSP stapling, to verify that the server certificate is valid, it might fail to detect some OCSP problems and instead wrongly consider the response as fine.  If the returned status reports another error than 'revoked' (like for example 'unauthorized') it is not treated as a bad certficate.

---
- curl 8.10.0-1
[bookworm] - curl 7.88.1-10+deb12u8
https://curl.se/docs/CVE-2024-8096.html
Introduced with: https://github.com/curl/curl/commit/f13669a375f5bfd14797bda91642cabe076974fa (curl-7_41_0)
Fixed by: https://github.com/curl/curl/commit/aeb1a281cab13c7ba791cb104e556b20e713941f (curl-8_10_0)

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2024-7264?s=debian&n=curl&ns=debian&t=deb&osn=debian&osv=12&vr=%3C7.88.1-10%2Bdeb12u7"><img alt="medium : CVE--2024--7264" src="https://img.shields.io/badge/CVE--2024--7264-lightgrey?label=medium%20&labelColor=fbb552"/></a> 

<table>
<tr><td>Affected range</td><td><code><7.88.1-10+deb12u7</code></td></tr>
<tr><td>Fixed version</td><td><code>7.88.1-10+deb12u7</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.056%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>26th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

libcurl's ASN1 parser code has the `GTime2str()` function, used for parsing an ASN.1 Generalized Time field. If given an syntactically incorrect field, the parser might end up using -1 for the length of the *time fraction*, leading to a `strlen()` getting performed on a pointer to a heap buffer area that is not (purposely) null terminated.  This flaw most likely leads to a crash, but can also lead to heap contents getting returned to the application when [CURLINFO_CERTINFO](https://curl.se/libcurl/c/CURLINFO_CERTINFO.html) is used.

---
- curl 8.9.1-1 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1077656)
[bookworm] - curl 7.88.1-10+deb12u7
[bullseye] - curl 7.74.0-1.3+deb11u13
https://curl.se/docs/CVE-2024-7264.html
Introduced by: https://github.com/curl/curl/commit/3a24cb7bc456366cbc3a03f7ab6d2576105a1f2d (curl-7_32_0)
Fixed by: https://github.com/curl/curl/commit/27959ecce75cdb2809c0bdb3286e60e08fadb519 (curl-8_9_1)

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2023-46218?s=debian&n=curl&ns=debian&t=deb&osn=debian&osv=12&vr=%3C7.88.1-10%2Bdeb12u5"><img alt="medium : CVE--2023--46218" src="https://img.shields.io/badge/CVE--2023--46218-lightgrey?label=medium%20&labelColor=fbb552"/></a> 

<table>
<tr><td>Affected range</td><td><code><7.88.1-10+deb12u5</code></td></tr>
<tr><td>Fixed version</td><td><code>7.88.1-10+deb12u5</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.122%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>48th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

This flaw allows a malicious HTTP server to set "super cookies" in curl that are then passed back to more origins than what is otherwise allowed or possible. This allows a site to set cookies that then would get sent to different and unrelated sites and domains.  It could do this by exploiting a mixed case flaw in curl's function that verifies a given cookie domain against the Public Suffix List (PSL). For example a cookie could be set with `domain=co.UK` when the URL used a lower case hostname `curl.co.uk`, even though `co.uk` is listed as a PSL domain.

---
- curl 8.5.0-1 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1057646)
Introduced by: https://github.com/curl/curl/commit/e77b5b7453c1e8ccd7ec0816890d98e2f392e465 (curl-7_46_0)
Fixed by: https://github.com/curl/curl/commit/2b0994c29a721c91c572cff7808c572a24d251eb (curl-8_5_0)
https://curl.se/docs/CVE-2023-46218.html

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2023-46219?s=debian&n=curl&ns=debian&t=deb&osn=debian&osv=12&vr=%3C7.88.1-10%2Bdeb12u5"><img alt="medium : CVE--2023--46219" src="https://img.shields.io/badge/CVE--2023--46219-lightgrey?label=medium%20&labelColor=fbb552"/></a> 

<table>
<tr><td>Affected range</td><td><code><7.88.1-10+deb12u5</code></td></tr>
<tr><td>Fixed version</td><td><code>7.88.1-10+deb12u5</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.109%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>45th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

When saving HSTS data to an excessively long file name, curl could end up removing all contents, making subsequent requests using that file unaware of the HSTS status they should otherwise use.

---
- curl 8.5.0-1 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1057645)
[bookworm] - curl 7.88.1-10+deb12u5
[bullseye] - curl <ignored> (curl is not built with HSTS support)
[buster] - curl <not-affected> (Not affected by CVE-2022-32207)
Introduced by: https://github.com/curl/curl/commit/20f9dd6bae50b7223171b17ba7798946e74f877f (curl-7_84_0)
The issue is introduced with the fix for CVE-2022-32207.
Fixed by: https://github.com/curl/curl/commit/73b65e94f3531179de45c6f3c836a610e3d0a846 (curl-8_5_0)
https://curl.se/docs/CVE-2023-46219.html

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2023-38546?s=debian&n=curl&ns=debian&t=deb&osn=debian&osv=12&vr=%3C7.88.1-10%2Bdeb12u4"><img alt="low : CVE--2023--38546" src="https://img.shields.io/badge/CVE--2023--38546-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code><7.88.1-10+deb12u4</code></td></tr>
<tr><td>Fixed version</td><td><code>7.88.1-10+deb12u4</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.132%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>49th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

This flaw allows an attacker to insert cookies at will into a running program using libcurl, if the specific series of conditions are met.  libcurl performs transfers. In its API, an application creates "easy handles" that are the individual handles for single transfers.  libcurl provides a function call that duplicates en easy handle called [curl_easy_duphandle](https://curl.se/libcurl/c/curl_easy_duphandle.html).  If a transfer has cookies enabled when the handle is duplicated, the cookie-enable state is also cloned - but without cloning the actual cookies. If the source handle did not read any cookies from a specific file on disk, the cloned version of the handle would instead store the file name as `none` (using the four ASCII letters, no quotes).  Subsequent use of the cloned handle that does not explicitly set a source to load cookies from would then inadvertently load cookies from a file named `none` - if such a file exists and is readable in the current directory of the program using libcurl. And if using the correct file format of course.

---
- curl 8.3.0-3
https://curl.se/docs/CVE-2023-38546.html
Introduced by: https://github.com/curl/curl/commit/74d5a6fb3b9a96d9fa51ba90996e94c878ebd151 (curl-7_9_1)
Fixed by: https://github.com/curl/curl/commit/61275672b46d9abb3285740467b882e22ed75da8 (curl-8_4_0)

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2024-2004?s=debian&n=curl&ns=debian&t=deb&osn=debian&osv=12&vr=%3C7.88.1-10%2Bdeb12u6"><img alt="low : CVE--2024--2004" src="https://img.shields.io/badge/CVE--2024--2004-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code><7.88.1-10+deb12u6</code></td></tr>
<tr><td>Fixed version</td><td><code>7.88.1-10+deb12u6</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.046%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>20th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

When a protocol selection parameter option disables all protocols without adding any then the default set of protocols would remain in the allowed set due to an error in the logic for removing protocols. The below command would perform a request to curl.se with a plaintext protocol which has been explicitly disabled.      curl --proto -all,-http http://curl.se  The flaw is only present if the set of selected protocols disables the entire set of available protocols, in itself a command with no practical use and therefore unlikely to be encountered in real situations. The curl security team has thus assessed this to be low severity bug.

---
- curl 8.7.1-1
[bookworm] - curl 7.88.1-10+deb12u6
[bullseye] - curl <not-affected> (Vulnerable code not present)
[buster] - curl <not-affected> (Vulnerable code not present)
https://curl.se/docs/CVE-2024-2004.html
Introduced by: https://github.com/curl/curl/commit/e6f8445edef8e7996d1cfb141d6df184efef972c (curl-7_85_0)
Fixed by: https://github.com/curl/curl/commit/17d302e56221f5040092db77d4f85086e8a20e0e (curl-8_7_0)

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2023-38039?s=debian&n=curl&ns=debian&t=deb&osn=debian&osv=12&vr=%3C7.88.1-10%2Bdeb12u3"><img alt="low : CVE--2023--38039" src="https://img.shields.io/badge/CVE--2023--38039-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code><7.88.1-10+deb12u3</code></td></tr>
<tr><td>Fixed version</td><td><code>7.88.1-10+deb12u3</code></td></tr>
<tr><td>EPSS Score</td><td><code>1.949%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>89th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

When curl retrieves an HTTP response, it stores the incoming headers so that they can be accessed later via the libcurl headers API.  However, curl did not have a limit in how many or how large headers it would accept in a response, allowing a malicious server to stream an endless series of headers and eventually cause curl to run out of heap memory.

---
- curl 8.3.0-1
[bookworm] - curl 7.88.1-10+deb12u3
[bullseye] - curl <not-affected> (Vulnerable code not present)
[buster] - curl <not-affected> (Vulnerable code not present)
https://www.openwall.com/lists/oss-security/2023/09/13/1
https://curl.se/docs/CVE-2023-38039.html
Introduced by: https://github.com/curl/curl/commit/7c8c723682d524ac9580b9ca3b71419163cb5660 (curl-7_83_0)
Experimental tag removed in: https://github.com/curl/curl/commit/4d94fac9f0d1dd02b8308291e4c47651142dc28b (curl-7_84_0)
Fixed by: https://github.com/curl/curl/commit/3ee79c1674fd6f99e8efca52cd7510e08b766770 (curl-8_3_0)

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2023-32001?s=debian&n=curl&ns=debian&t=deb&osn=debian&osv=12&vr=%3C7.88.1-10%2Bdeb12u1"><img alt="low : CVE--2023--32001" src="https://img.shields.io/badge/CVE--2023--32001-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code><7.88.1-10+deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><code>7.88.1-10+deb12u1</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.044%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>15th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

libcurl can be told to save cookie, HSTS and/or alt-svc data to files. When
doing this, it called `stat()` followed by `fopen()` in a way that made it
vulnerable to a TOCTOU race condition problem.

By exploiting this flaw, an attacker could trick the victim to create or
overwrite protected files holding this data in ways it was not intended to.


---
REJECTED

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 1" src="https://img.shields.io/badge/C-1-8b1924"/> <img alt="high: 1" src="https://img.shields.io/badge/H-1-e25d68"/> <img alt="medium: 1" src="https://img.shields.io/badge/M-1-fbb552"/> <img alt="low: 0" src="https://img.shields.io/badge/L-0-lightgrey"/> <!-- unspecified: 0 --><strong>krb5</strong> <code>1.20.1-2</code> (deb)</summary>

<small><code>pkg:deb/debian/krb5@1.20.1-2?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2024-37371?s=debian&n=krb5&ns=debian&t=deb&osn=debian&osv=12&vr=%3C1.20.1-2%2Bdeb12u2"><img alt="critical : CVE--2024--37371" src="https://img.shields.io/badge/CVE--2024--37371-lightgrey?label=critical%20&labelColor=8b1924"/></a> 

<table>
<tr><td>Affected range</td><td><code><1.20.1-2+deb12u2</code></td></tr>
<tr><td>Fixed version</td><td><code>1.20.1-2+deb12u2</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.114%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>46th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

In MIT Kerberos 5 (aka krb5) before 1.21.3, an attacker can cause invalid memory reads during GSS message token handling by sending message tokens with invalid length fields.

---
- krb5 1.21.3-1
https://github.com/krb5/krb5/commit/55fbf435edbe2e92dd8101669b1ce7144bc96fef (krb5-1.21.3-final)

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2024-37370?s=debian&n=krb5&ns=debian&t=deb&osn=debian&osv=12&vr=%3C1.20.1-2%2Bdeb12u2"><img alt="high : CVE--2024--37370" src="https://img.shields.io/badge/CVE--2024--37370-lightgrey?label=high%20&labelColor=e25d68"/></a> 

<table>
<tr><td>Affected range</td><td><code><1.20.1-2+deb12u2</code></td></tr>
<tr><td>Fixed version</td><td><code>1.20.1-2+deb12u2</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.114%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>46th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

In MIT Kerberos 5 (aka krb5) before 1.21.3, an attacker can modify the plaintext Extra Count field of a confidential GSS krb5 wrap token, causing the unwrapped token to appear truncated to the application.

---
- krb5 1.21.3-1
https://github.com/krb5/krb5/commit/55fbf435edbe2e92dd8101669b1ce7144bc96fef (krb5-1.21.3-final)

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2023-36054?s=debian&n=krb5&ns=debian&t=deb&osn=debian&osv=12&vr=%3C1.20.1-2%2Bdeb12u1"><img alt="medium : CVE--2023--36054" src="https://img.shields.io/badge/CVE--2023--36054-lightgrey?label=medium%20&labelColor=fbb552"/></a> 

<table>
<tr><td>Affected range</td><td><code><1.20.1-2+deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><code>1.20.1-2+deb12u1</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.515%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>77th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

lib/kadm5/kadm_rpc_xdr.c in MIT Kerberos 5 (aka krb5) before 1.20.2 and 1.21.x before 1.21.1 frees an uninitialized pointer. A remote authenticated user can trigger a kadmind crash. This occurs because _xdr_kadm5_principal_ent_rec does not validate the relationship between n_key_data and the key_data array count.

---
- krb5 1.20.1-3 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1043431)
[bookworm] - krb5 1.20.1-2+deb12u1
[bullseye] - krb5 1.18.3-6+deb11u4
https://github.com/krb5/krb5/commit/ef08b09c9459551aabbe7924fb176f1583053cdd

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 1" src="https://img.shields.io/badge/C-1-8b1924"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 2" src="https://img.shields.io/badge/M-2-fbb552"/> <img alt="low: 4" src="https://img.shields.io/badge/L-4-fce1a9"/> <!-- unspecified: 0 --><strong>openssh</strong> <code>1:9.2p1-2</code> (deb)</summary>

<small><code>pkg:deb/debian/openssh@1:9.2p1-2?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2023-38408?s=debian&n=openssh&ns=debian&t=deb&osn=debian&osv=12&vr=%3C1%3A9.2p1-2%2Bdeb12u1"><img alt="critical : CVE--2023--38408" src="https://img.shields.io/badge/CVE--2023--38408-lightgrey?label=critical%20&labelColor=8b1924"/></a> 

<table>
<tr><td>Affected range</td><td><code><1:9.2p1-2+deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><code>1:9.2p1-2+deb12u1</code></td></tr>
<tr><td>EPSS Score</td><td><code>3.986%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>92nd percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

The PKCS#11 feature in ssh-agent in OpenSSH before 9.3p2 has an insufficiently trustworthy search path, leading to remote code execution if an agent is forwarded to an attacker-controlled system. (Code in /usr/lib is not necessarily safe for loading into ssh-agent.) NOTE: this issue exists because of an incomplete fix for CVE-2016-10009.

---
- openssh 1:9.3p2-1 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1042460)
[bookworm] - openssh 1:9.2p1-2+deb12u1
[bullseye] - openssh 1:8.4p1-5+deb11u2
https://www.openwall.com/lists/oss-security/2023/07/19/9
https://github.com/openssh/openssh-portable/commit/892506b13654301f69f9545f48213fc210e5c5cc
https://github.com/openssh/openssh-portable/commit/1f2731f5d7a8f8a8385c6031667ed29072c0d92a
https://github.com/openssh/openssh-portable/commit/29ef8a04866ca14688d5b7fed7b8b9deab851f77
https://github.com/openssh/openssh-portable/commit/099cdf59ce1e72f55d421c8445bf6321b3004755
Exploitation requires the presence of specific libraries on the victim system.
Remote exploitation requires that the agent was forwarded to an attacker-controlled
system.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2025-26465?s=debian&n=openssh&ns=debian&t=deb&osn=debian&osv=12&vr=%3C1%3A9.2p1-2%2Bdeb12u5"><img alt="medium : CVE--2025--26465" src="https://img.shields.io/badge/CVE--2025--26465-lightgrey?label=medium%20&labelColor=fbb552"/></a> 

<table>
<tr><td>Affected range</td><td><code><1:9.2p1-2+deb12u5</code></td></tr>
<tr><td>Fixed version</td><td><code>1:9.2p1-2+deb12u5</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.043%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>12th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A vulnerability was found in OpenSSH when the VerifyHostKeyDNS option is enabled. A machine-in-the-middle attack can be performed by a malicious machine impersonating a legit server. This issue occurs due to how OpenSSH mishandles error codes in specific conditions when verifying the host key. For an attack to be considered successful, the attacker needs to manage to exhaust the client's memory resource first, turning the attack complexity high.

---
- openssh 1:9.9p2-1
https://www.openssh.com/releasenotes.html#9.9p2
https://www.qualys.com/2025/02/18/openssh-mitm-dos.txt
Introduced with: https://github.com/openssh/openssh-portable/commit/5e39a49930d885aac9c76af3129332b6e772cd75 (V_6_8_P1)
Fixed by: https://github.com/openssh/openssh-portable/commit/0832aac79517611dd4de93ad0a83577994d9c907 (V_9_9_P1)

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2023-51385?s=debian&n=openssh&ns=debian&t=deb&osn=debian&osv=12&vr=%3C1%3A9.2p1-2%2Bdeb12u2"><img alt="medium : CVE--2023--51385" src="https://img.shields.io/badge/CVE--2023--51385-lightgrey?label=medium%20&labelColor=fbb552"/></a> 

<table>
<tr><td>Affected range</td><td><code><1:9.2p1-2+deb12u2</code></td></tr>
<tr><td>Fixed version</td><td><code>1:9.2p1-2+deb12u2</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.341%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>72nd percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

In ssh in OpenSSH before 9.6, OS command injection might occur if a user name or host name has shell metacharacters, and this name is referenced by an expansion token in certain situations. For example, an untrusted Git repository can have a submodule with shell metacharacters in a user name or host name.

---
- openssh 1:9.6p1-1
https://www.openwall.com/lists/oss-security/2023/12/18/2
https://github.com/openssh/openssh-portable/commit/7ef3787c84b6b524501211b11a26c742f829af1a (V_9_6_P1)
https://vin01.github.io/piptagole/ssh/security/openssh/libssh/remote-code-execution/2023/12/20/openssh-proxycommand-libssh-rce.html

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2024-6387?s=debian&n=openssh&ns=debian&t=deb&osn=debian&osv=12&vr=%3C1%3A9.2p1-2%2Bdeb12u3"><img alt="low : CVE--2024--6387" src="https://img.shields.io/badge/CVE--2024--6387-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code><1:9.2p1-2+deb12u3</code></td></tr>
<tr><td>Fixed version</td><td><code>1:9.2p1-2+deb12u3</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.284%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>69th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A security regression (CVE-2006-5051) was discovered in OpenSSH's server (sshd). There is a race condition which can lead sshd to handle some signals in an unsafe manner. An unauthenticated, remote attacker may be able to trigger it by failing to authenticate within a set time period.

---
- openssh 1:9.7p1-7
[bullseye] - openssh <not-affected> (Vulnerable code introduced later)
Introduced with: https://github.com/openssh/openssh-portable/commit/752250caabda3dd24635503c4cd689b32a650794 (V_8_5_P1)
Fixed by: https://github.com/openssh/openssh-portable/commit/81c1099d22b81ebfd20a334ce986c4f753b0db29 (V_9_8_P1)
https://lists.mindrot.org/pipermail/openssh-unix-announce/2024-July/000158.html
https://www.openwall.com/lists/oss-security/2024/07/01/1
https://www.qualys.com/2024/07/01/cve-2024-6387/regresshion.txt

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2023-51384?s=debian&n=openssh&ns=debian&t=deb&osn=debian&osv=12&vr=%3C1%3A9.2p1-2%2Bdeb12u2"><img alt="low : CVE--2023--51384" src="https://img.shields.io/badge/CVE--2023--51384-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code><1:9.2p1-2+deb12u2</code></td></tr>
<tr><td>Fixed version</td><td><code>1:9.2p1-2+deb12u2</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.043%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>12th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

In ssh-agent in OpenSSH before 9.6, certain destination constraints can be incompletely applied. When destination constraints are specified during addition of PKCS#11-hosted private keys, these constraints are only applied to the first key, even if a PKCS#11 token returns multiple keys.

---
- openssh 1:9.6p1-1
[bookworm] - openssh 1:9.2p1-2+deb12u2
[bullseye] - openssh <not-affected> (Vulnerable code introduced later; per-hop destination constraints support added in OpenSSH 8.9)
[buster] - openssh <not-affected> (Vulnerable code introduced later; per-hop destination constraints support added in OpenSSH 8.9)
https://www.openwall.com/lists/oss-security/2023/12/18/2
https://github.com/openssh/openssh-portable/commit/881d9c6af9da4257c69c327c4e2f1508b2fa754b (V_9_6_P1)

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2023-48795?s=debian&n=openssh&ns=debian&t=deb&osn=debian&osv=12&vr=%3C1%3A9.2p1-2%2Bdeb12u2"><img alt="low : CVE--2023--48795" src="https://img.shields.io/badge/CVE--2023--48795-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code><1:9.2p1-2+deb12u2</code></td></tr>
<tr><td>Fixed version</td><td><code>1:9.2p1-2+deb12u2</code></td></tr>
<tr><td>EPSS Score</td><td><code>95.483%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>100th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

The SSH transport protocol with certain OpenSSH extensions, found in OpenSSH before 9.6 and other products, allows remote attackers to bypass integrity checks such that some packets are omitted (from the extension negotiation message), and a client and server may consequently end up with a connection for which some security features have been downgraded or disabled, aka a Terrapin attack. This occurs because the SSH Binary Packet Protocol (BPP), implemented by these extensions, mishandles the handshake phase and mishandles use of sequence numbers. For example, there is an effective attack against SSH's use of ChaCha20-Poly1305 (and CBC with Encrypt-then-MAC). The bypass occurs in chacha20-poly1305@openssh.com and (if CBC is used) the -etm@openssh.com MAC algorithms. This also affects Maverick Synergy Java SSH API before 3.1.0-SNAPSHOT, Dropbear through 2022.83, Ssh before 5.1.1 in Erlang/OTP, PuTTY before 0.80, AsyncSSH before 2.14.2, golang.org/x/crypto before 0.17.0, libssh before 0.10.6, libssh2 through 1.11.0, Thorn Tech SFTP Gateway before 3.4.6, Tera Term before 5.1, Paramiko before 3.4.0, jsch before 0.2.15, SFTPGo before 2.5.6, Netgate pfSense Plus through 23.09.1, Netgate pfSense CE through 2.7.2, HPN-SSH through 18.2.0, ProFTPD before 1.3.8b (and before 1.3.9rc2), ORYX CycloneSSH before 2.3.4, NetSarang XShell 7 before Build 0144, CrushFTP before 10.6.0, ConnectBot SSH library before 2.2.22, Apache MINA sshd through 2.11.0, sshj through 0.37.0, TinySSH through 20230101, trilead-ssh2 6401, LANCOM LCOS and LANconfig, FileZilla before 3.66.4, Nova before 11.8, PKIX-SSH before 14.4, SecureCRT before 9.4.3, Transmit5 before 5.10.4, Win32-OpenSSH before 9.5.0.0p1-Beta, WinSCP before 6.2.2, Bitvise SSH Server before 9.32, Bitvise SSH Client before 9.33, KiTTY through 0.76.1.13, the net-ssh gem 7.2.0 for Ruby, the mscdex ssh2 module before 1.15.0 for Node.js, the thrussh library before 0.35.1 for Rust, and the Russh crate before 0.40.2 for Rust.

---
- dropbear 2022.83-4 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1059001)
[bookworm] - dropbear 2022.83-1+deb12u1
[bullseye] - dropbear 2020.81-3+deb11u1
[buster] - dropbear <not-affected> (ChaCha20-Poly1305 support introduced in 2020.79; *-EtM not supported as of 2022.83)
- erlang 1:25.3.2.8+dfsg-1 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1059002)
[bookworm] - erlang <no-dsa> (Minor issue)
[bullseye] - erlang <no-dsa> (Minor issue)
[buster] - erlang <no-dsa> (Minor issue)
- filezilla 3.66.4-1
[bookworm] - filezilla 3.63.0-1+deb12u3
[bullseye] - filezilla 3.52.2-3+deb11u1
[buster] - filezilla <not-affected> (OpenSSH extension in question not implemented)
- golang-go.crypto 1:0.17.0-1 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1059003)
[bookworm] - golang-go.crypto <no-dsa> (Minor issue)
[bullseye] - golang-go.crypto <no-dsa> (Minor issue)
[buster] - golang-go.crypto <postponed> (Limited support, minor issue, follow bullseye DSAs/point-releases)
- jsch <not-affected> (ChaCha20-Poly1305 support introduced in 0.1.61; *-EtM support introduced in 0.1.58)
- libssh 0.10.6-1 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1059004)
- libssh2 1.11.0-4 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1059005)
[bookworm] - libssh2 <not-affected> (ChaCha20-Poly1305 and CBC-EtM support not present)
[bullseye] - libssh2 <not-affected> (ChaCha20-Poly1305 and CBC-EtM support not present)
[buster] - libssh2 <not-affected> (ChaCha20-Poly1305 and CBC-EtM support not present)
- openssh 1:9.6p1-1
- paramiko 3.4.0-1 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1059006)
[bookworm] - paramiko <ignored> (Minor issue)
[bullseye] - paramiko <no-dsa> (Minor issue)
[buster] - paramiko <not-affected> (ChaCha20-Poly1305 and CBC-EtM support not present)
- phpseclib 1.0.22-1
- php-phpseclib 2.0.46-1
- php-phpseclib3 3.0.35-1
- proftpd-dfsg 1.3.8.b+dfsg-1 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1059144)
[bookworm] - proftpd-dfsg 1.3.8+dfsg-4+deb12u3
[buster] - proftpd-dfsg <no-dsa> (Minor issue)
- proftpd-mod-proxy 0.9.3-1 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1059290)
[bookworm] - proftpd-mod-proxy 0.9.2-1+deb12u1
[bullseye] - proftpd-mod-proxy <ignored> (Minor issue)
- putty 0.80-1
- python-asyncssh 2.15.0-1 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1059007)
- tinyssh 20230101-4 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1059058; unimportant)
- trilead-ssh2 <unfixed> (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1059294)
[bookworm] - trilead-ssh2 <ignored> (Minor issue)
[bullseye] - trilead-ssh2 <no-dsa> (Minor issue)
[buster] - trilead-ssh2 <no-dsa> (Minor issue)
https://terrapin-attack.com/
https://www.openwall.com/lists/oss-security/2023/12/18/3
dropbear: https://github.com/mkj/dropbear/commit/6e43be5c7b99dbee49dc72b6f989f29fdd7e9356
Erlang/OTP: https://github.com/erlang/otp/commit/ee67d46285394db95133709cef74b0c462d665aa (OTP-24.3.4.15, OTP-25.3.2.8, OTP-26.2.1)
filezilla: https://svn.filezilla-project.org/filezilla?view=revision&revision=11047
filezilla: https://svn.filezilla-project.org/filezilla?view=revision&revision=11048
filezilla: https://svn.filezilla-project.org/filezilla?view=revision&revision=11049
golang.org/x/crypto/ssh: https://groups.google.com/g/golang-announce/c/qA3XtxvMUyg
golang.org/x/crypto/ssh: https://github.com/golang/go/issues/64784
golang.org/x/crypto/ssh: https://github.com/golang/crypto/commit/9d2ee975ef9fe627bf0a6f01c1f69e8ef1d4f05d (v0.17.0)
jsch: https://github.com/mwiede/jsch/issues/457
jsch: https://github.com/norrisjeremy/jsch/commit/6214da974286a8b94a95f4cf6cec96e972ffd370 (jsch-0.2.15)
libssh: https://www.libssh.org/security/advisories/CVE-2023-48795.txt
libssh: https://gitlab.com/libssh/libssh-mirror/-/commit/4cef5e965a46e9271aed62631b152e4bd23c1e3c (libssh-0.10.6)
libssh: https://gitlab.com/libssh/libssh-mirror/-/commit/0870c8db28be9eb457ee3d4f9a168959d9507efd (libssh-0.10.6)
libssh: https://gitlab.com/libssh/libssh-mirror/-/commit/5846e57538c750c5ce67df887d09fa99861c79c6 (libssh-0.10.6)
libssh: https://gitlab.com/libssh/libssh-mirror/-/commit/89df759200d31fc79fbbe213d8eda0d329eebf6d (libssh-0.10.6)
libssh2: https://github.com/libssh2/libssh2/issues/1290
libssh2: https://github.com/libssh2/libssh2/pull/1291
libssh2: https://github.com/libssh2/libssh2/commit/d34d9258b8420b19ec3f97b4cc5bf7aa7d98e35a
OpenSSH: https://www.openwall.com/lists/oss-security/2023/12/18/2
OpenSSH (strict key exchange): https://github.com/openssh/openssh-portable/commit/1edb00c58f8a6875fad6a497aa2bacf37f9e6cd5 (V_9_6_P1)
paramiko: https://github.com/paramiko/paramiko/issues/2337
phpseclib: https://github.com/phpseclib/phpseclib/issues/1972
phpseclib: https://github.com/phpseclib/phpseclib/commit/c8e3ab9317abae80d7f58fd9acd9214b57572b32 (1.0.22, 2.0.46, 3.0.35)
proftpd: https://github.com/proftpd/proftpd/issues/1760
proftpd: https://github.com/proftpd/proftpd/commit/7fba68ebb3ded3047a35aa639e115eba7d585682 (v1.3.9rc2)
proftpd: https://github.com/proftpd/proftpd/commit/bcec15efe6c53dac40420731013f1cd2fd54123b (v1.3.8b)
proftpd-mod-proxy: https://github.com/Castaglia/proftpd-mod_proxy/issues/257
proftpd-mod-proxy: https://github.com/Castaglia/proftpd-mod_proxy/commit/54612735629231de2242d6395d334539604872fb (v0.9.3)
PuTTY: https://www.chiark.greenend.org.uk/~sgtatham/putty/wishlist/vuln-terrapin.html
PuTTY: https://git.tartarus.org/?p=simon/putty.git;a=commit;h=9e099151574885f3c717ac10a633a9218db8e7bb (0.80)
PuTTY: https://git.tartarus.org/?p=simon/putty.git;a=commit;h=f2e7086902b3605c96e54ef9c956ca7ab000010e (0.80)
PuTTY: https://git.tartarus.org/?p=simon/putty.git;a=commit;h=9fcbb86f715bc03e58921482efe663aa0c662d62 (0.80)
PuTTY: https://git.tartarus.org/?p=simon/putty.git;a=commit;h=244be5412728a7334a2d457fbac4e0a2597165e5 (0.80)
PuTTY: https://git.tartarus.org/?p=simon/putty.git;a=commit;h=58fc33a155ad496bdcf380fa6193302240a15ae9 (0.80)
PuTTY: https://git.tartarus.org/?p=simon/putty.git;a=commit;h=0b00e4ce26d89cd010e31e66fd02ac77cb982367 (0.80)
PuTTY: https://git.tartarus.org/?p=simon/putty.git;a=commit;h=fdc891d17063ab26cf68c74245ab1fd9771556cb (0.80)
PuTTY: https://git.tartarus.org/?p=simon/putty.git;a=commit;h=b80a41d386dbfa1b095c17bd2ed001477f302d46 (0.80)
asyncssh: https://github.com/ronf/asyncssh/security/advisories/GHSA-hfmc-7525-mj55
asyncssh: https://github.com/ronf/asyncssh/commit/0bc73254f41acb140187e0c89606311f88de5b7b (v2.14.2)
tinyssh: https://github.com/janmojzis/tinyssh/issues/81
tinyssh: https://github.com/janmojzis/tinyssh/commit/ebaa1bd23c2c548af70cc8151e85c74f4c8594bb
tinyssh: 20230101-4 implements kex-strict-s-v00@openssh.com for the strict kex support. But
tinyssh: since there is no support for EXT_INFO in tinyssh, even with the present
tinyssh: chacha20-poly1305@openssh.com encryption algorith, there is no downgrade of the
tinyssh: connection security.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2023-28531?s=debian&n=openssh&ns=debian&t=deb&osn=debian&osv=12&vr=%3C1%3A9.2p1-2%2Bdeb12u2"><img alt="low : CVE--2023--28531" src="https://img.shields.io/badge/CVE--2023--28531-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code><1:9.2p1-2+deb12u2</code></td></tr>
<tr><td>Fixed version</td><td><code>1:9.2p1-2+deb12u2</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.153%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>53rd percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

ssh-add in OpenSSH before 9.3 adds smartcard keys to ssh-agent without the intended per-hop destination constraints. The earliest affected version is 8.9.

---
- openssh 1:9.3p1-1 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1033166)
[bookworm] - openssh 1:9.2p1-2+deb12u2
[bullseye] - openssh <not-affected> (Vulnerable code introduced later; per-hop destination constraints support added in OpenSSH 8.9)
[buster] - openssh <not-affected> (Vulnerable code introduced later; per-hop destination constraints support added in OpenSSH 8.9)
https://github.com/openssh/openssh-portable/commit/54ac4ab2b53ce9fcb66b8250dee91c070e4167ed (V_9_3_P1)

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 1" src="https://img.shields.io/badge/C-1-8b1924"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 1" src="https://img.shields.io/badge/M-1-fbb552"/> <img alt="low: 0" src="https://img.shields.io/badge/L-0-lightgrey"/> <!-- unspecified: 0 --><strong>glib2.0</strong> <code>2.74.6-2</code> (deb)</summary>

<small><code>pkg:deb/debian/glib2.0@2.74.6-2?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2024-52533?s=debian&n=glib2.0&ns=debian&t=deb&osn=debian&osv=12&vr=%3C2.74.6-2%2Bdeb12u5"><img alt="critical : CVE--2024--52533" src="https://img.shields.io/badge/CVE--2024--52533-lightgrey?label=critical%20&labelColor=8b1924"/></a> 

<table>
<tr><td>Affected range</td><td><code><2.74.6-2+deb12u5</code></td></tr>
<tr><td>Fixed version</td><td><code>2.74.6-2+deb12u5</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.045%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>18th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

gio/gsocks4aproxy.c in GNOME GLib before 2.82.1 has an off-by-one error and resultant buffer overflow because SOCKS4_CONN_MSG_LEN is not sufficient for a trailing '\0' character.

---
- glib2.0 2.82.1-1 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1087419)
[bookworm] - glib2.0 2.74.6-2+deb12u5
https://gitlab.gnome.org/GNOME/glib/-/issues/3461
https://gitlab.gnome.org/GNOME/glib/-/commit/25833cefda24c60af913d6f2d532b5afd608b821 (main)
https://gitlab.gnome.org/GNOME/glib/-/commit/ec0b708b981af77fef8e4bbb603cde4de4cd2e29 (2.82.1)

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2024-34397?s=debian&n=glib2.0&ns=debian&t=deb&osn=debian&osv=12&vr=%3C2.74.6-2%2Bdeb12u1"><img alt="medium : CVE--2024--34397" src="https://img.shields.io/badge/CVE--2024--34397-lightgrey?label=medium%20&labelColor=fbb552"/></a> 

<table>
<tr><td>Affected range</td><td><code><2.74.6-2+deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><code>2.74.6-2+deb12u1</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.044%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>16th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

An issue was discovered in GNOME GLib before 2.78.5, and 2.79.x and 2.80.x before 2.80.1. When a GDBus-based client subscribes to signals from a trusted system service such as NetworkManager on a shared computer, other users of the same computer can send spoofed D-Bus signals that the GDBus-based client will wrongly interpret as having been sent by the trusted system service. This could lead to the GDBus-based client behaving incorrectly, with an application-dependent impact.

---
- glib2.0 2.80.0-10
https://gitlab.gnome.org/GNOME/glib/-/issues/3268
Fixes: https://gitlab.gnome.org/GNOME/glib/-/issues/3268#fixes
Requires regression fix for src:gnome-shell: https://gitlab.gnome.org/GNOME/gnome-shell/-/commit/50a011a19dcc6997ea6173c07bb80b2d9888d363

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 1" src="https://img.shields.io/badge/C-1-8b1924"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 0" src="https://img.shields.io/badge/L-0-lightgrey"/> <!-- unspecified: 0 --><strong>aom</strong> <code>3.6.0-1</code> (deb)</summary>

<small><code>pkg:deb/debian/aom@3.6.0-1?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2024-5171?s=debian&n=aom&ns=debian&t=deb&osn=debian&osv=12&vr=%3C3.6.0-1%2Bdeb12u1"><img alt="critical : CVE--2024--5171" src="https://img.shields.io/badge/CVE--2024--5171-lightgrey?label=critical%20&labelColor=8b1924"/></a> 

<table>
<tr><td>Affected range</td><td><code><3.6.0-1+deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><code>3.6.0-1+deb12u1</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.060%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>28th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

Integer overflow in libaom internal function img_alloc_helper can lead to heap buffer overflow. This function can be reached via 3 callers:     *  Calling aom_img_alloc() with a large value of the d_w, d_h, or align parameter may result in integer overflows in the calculations of buffer sizes and offsets and some fields of the returned aom_image_t struct may be invalid.   *  Calling aom_img_wrap() with a large value of the d_w, d_h, or align parameter may result in integer overflows in the calculations of buffer sizes and offsets and some fields of the returned aom_image_t struct may be invalid.   *  Calling aom_img_alloc_with_border() with a large value of the d_w, d_h, align, size_align, or border parameter may result in integer overflows in the calculations of buffer sizes and offsets and some fields of the returned aom_image_t struct may be invalid.

---
- aom 3.8.2-3
https://issues.chromium.org/issues/332382766
https://aomedia.googlesource.com/aom/+/19d9966572a410804349e1a8ee2017fed49a6dab
https://aomedia.googlesource.com/aom/+/8156fb76d88845d716867d20333fd27001be47a8

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 5" src="https://img.shields.io/badge/H-5-e25d68"/> <img alt="medium: 3" src="https://img.shields.io/badge/M-3-fbb552"/> <img alt="low: 4" src="https://img.shields.io/badge/L-4-fce1a9"/> <!-- unspecified: 0 --><strong>postgresql-15</strong> <code>15.3-0+deb12u1</code> (deb)</summary>

<small><code>pkg:deb/debian/postgresql-15@15.3-0%2Bdeb12u1?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2024-7348?s=debian&n=postgresql-15&ns=debian&t=deb&osn=debian&osv=12&vr=%3C15.8-0%2Bdeb12u1"><img alt="high : CVE--2024--7348" src="https://img.shields.io/badge/CVE--2024--7348-lightgrey?label=high%20&labelColor=e25d68"/></a> 

<table>
<tr><td>Affected range</td><td><code><15.8-0+deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><code>15.8-0+deb12u1</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.050%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>22nd percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

Time-of-check Time-of-use (TOCTOU) race condition in pg_dump in PostgreSQL allows an object creator to execute arbitrary SQL functions as the user running pg_dump, which is often a superuser. The attack involves replacing another relation type with a view or foreign table. The attack requires waiting for pg_dump to start, but winning the race condition is trivial if the attacker retains an open transaction. Versions before PostgreSQL 16.4, 15.8, 14.13, 13.16, and 12.20 are affected.

---
- postgresql-16 16.4-1
- postgresql-15 <removed>
- postgresql-13 <removed>
https://www.postgresql.org/about/news/postgresql-164-158-1413-1316-1220-and-17-beta-3-released-2910/
https://www.postgresql.org/support/security/CVE-2024-7348/
https://git.postgresql.org/gitweb/?p=postgresql.git;a=commitdiff;h=79c7a7e29695a32fef2e65682be224b8d61ec972 (REL_12_20)

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2024-10979?s=debian&n=postgresql-15&ns=debian&t=deb&osn=debian&osv=12&vr=%3C15.9-0%2Bdeb12u1"><img alt="high : CVE--2024--10979" src="https://img.shields.io/badge/CVE--2024--10979-lightgrey?label=high%20&labelColor=e25d68"/></a> 

<table>
<tr><td>Affected range</td><td><code><15.9-0+deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><code>15.9-0+deb12u1</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.070%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>33rd percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

Incorrect control of environment variables in PostgreSQL PL/Perl allows an unprivileged database user to change sensitive process environment variables (e.g. PATH).  That often suffices to enable arbitrary code execution, even if the attacker lacks a database server operating system user.  Versions before PostgreSQL 17.1, 16.5, 15.9, 14.14, 13.17, and 12.21 are affected.

---
- postgresql-17 17.1-1
- postgresql-16 <removed> (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1088687)
- postgresql-15 <removed>
- postgresql-13 <removed>
https://www.postgresql.org/support/security/CVE-2024-10979/
Fixed by: https://git.postgresql.org/gitweb/?p=postgresql.git;a=commit;h=3ebcfa54db3309651d8f1d3be6451a8449f6c6ec (v17.2, 1 of 3)
Fixed by: https://git.postgresql.org/gitweb/?p=postgresql.git;a=commit;h=4cd4f3b97492c1b38115d0563a2e55b136eb542a (v17.2, 2 of 3)
Fixed by: https://git.postgresql.org/gitweb/?p=postgresql.git;a=commit;h=8d19f3fea003b1f744516b84cbdb0097ae7b2912 (v17.2, 3 of 3)
Fixed by: https://git.postgresql.org/gitweb/?p=postgresql.git;a=commit;h=8fe3e697a1a83a722b107c7cb9c31084e1f4d077 (v16.6, 1 of 4)
Fixed by: https://git.postgresql.org/gitweb/?p=postgresql.git;a=commit;h=88269df4da032bb1536d4291a13f3af4e1e599ba (v16.6, 2 of 4)
Fixed by: https://git.postgresql.org/gitweb/?p=postgresql.git;a=commit;h=168579e23bdbeda1a140440c0272b335d53ad061 (v16.6, 3 of 4)
Fixed by: https://git.postgresql.org/gitweb/?p=postgresql.git;a=commit;h=64df8870097aa286363a5d81462802783abbfa61 (v16.6, 4 of 4)
Fixed by: https://git.postgresql.org/gitweb/?p=postgresql.git;a=commit;h=e530835c6cc5b2dbf330ebe6b0a7fb9f19f5a54c (v15.10, 1 of 2)
Fixed by: https://git.postgresql.org/gitweb/?p=postgresql.git;a=commit;h=c834b375a6dc36ff92f9f738ef1d7af09d91165f (v15.10, 2 of 2)
Fixed by: https://git.postgresql.org/gitweb/?p=postgresql.git;a=commit;h=d15ec27c977100037ae513ab7fe1a214bfc2507b (v14.15, 1 of 3)
Fixed by: https://git.postgresql.org/gitweb/?p=postgresql.git;a=commit;h=f89bd92c963c3be30a1cf26960aa86aaad117235 (v14.15, 2 of 3)
Fixed by: https://git.postgresql.org/gitweb/?p=postgresql.git;a=commit;h=256e34653aadd3582b98411d7d26f4fbb865e0ec (v14.15, 3 of 3)
Fixed by: https://git.postgresql.org/gitweb/?p=postgresql.git;a=commit;h=e428cd058f0bebb5782b0c263565b0ad088e9650 (v13.18, 1 of 3)
Fixed by: https://git.postgresql.org/gitweb/?p=postgresql.git;a=commit;h=6bccd7b037d09b91ce272c68f43705e2fecd4cca (v13.18, 2 of 3)
Fixed by: https://git.postgresql.org/gitweb/?p=postgresql.git;a=commit;h=0bd9560d964abc09e446e4c5e264bb7a0886e5ea (v13.18, 3 of 3)
Fixed by: https://git.postgresql.org/gitweb/?p=postgresql.git;a=commit;h=2ab12d860e51e468703a2777b3759b7a61639df2 (v12.21, 1 of 3)
Fixed by: https://git.postgresql.org/gitweb/?p=postgresql.git;a=commit;h=b1e58defb6a43fe35511eaa80858293b07c8b512 (v12.21, 2 of 3)
Fixed by: https://git.postgresql.org/gitweb/?p=postgresql.git;a=commit;h=9fc1c3a02ddc4cf2a34550c0f985288cea7094bd (v12.21, 3 of 3)

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2023-5869?s=debian&n=postgresql-15&ns=debian&t=deb&osn=debian&osv=12&vr=%3C15.5-0%2Bdeb12u1"><img alt="high : CVE--2023--5869" src="https://img.shields.io/badge/CVE--2023--5869-lightgrey?label=high%20&labelColor=e25d68"/></a> 

<table>
<tr><td>Affected range</td><td><code><15.5-0+deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><code>15.5-0+deb12u1</code></td></tr>
<tr><td>EPSS Score</td><td><code>4.152%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>92nd percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A flaw was found in PostgreSQL that allows authenticated database users to execute arbitrary code through missing overflow checks during SQL array value modification. This issue exists due to an integer overflow during array modification where a remote user can trigger the overflow by providing specially crafted data. This enables the execution of arbitrary code on the target system, allowing users to write arbitrary bytes to memory and extensively read the server's memory.

---
- postgresql-16 16.1-1
- postgresql-15 <removed> (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1056283)
- postgresql-13 <removed>
- postgresql-11 <removed>
https://www.postgresql.org/support/security/CVE-2023-5869/
https://www.postgresql.org/about/news/postgresql-161-155-1410-1313-1217-and-1122-released-2749/

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2024-0985?s=debian&n=postgresql-15&ns=debian&t=deb&osn=debian&osv=12&vr=%3C15.6-0%2Bdeb12u1"><img alt="high : CVE--2024--0985" src="https://img.shields.io/badge/CVE--2024--0985-lightgrey?label=high%20&labelColor=e25d68"/></a> 

<table>
<tr><td>Affected range</td><td><code><15.6-0+deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><code>15.6-0+deb12u1</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.172%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>55th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

Late privilege drop in REFRESH MATERIALIZED VIEW CONCURRENTLY in PostgreSQL allows an object creator to execute arbitrary SQL functions as the command issuer. The command intends to run SQL functions as the owner of the materialized view, enabling safe refresh of untrusted materialized views. The victim is a superuser or member of one of the attacker's roles. The attack requires luring the victim into running REFRESH MATERIALIZED VIEW CONCURRENTLY on the attacker's materialized view. Versions before PostgreSQL 16.2, 15.6, 14.11, 13.14, and 12.18 are affected.

---
- postgresql-16 16.2-1
- postgresql-15 <removed>
- postgresql-13 <removed>
- postgresql-11 <removed>
https://github.com/google/security-research/security/advisories/GHSA-9984-7hcf-v553
https://www.postgresql.org/support/security/CVE-2024-0985/
https://git.postgresql.org/gitweb/?p=postgresql.git;a=commit;h=d6a61cb3bef3c8fbc35c2a6182e75a8c1d351e41 (REL_16_2)
https://git.postgresql.org/gitweb/?p=postgresql.git;a=commit;h=f2fdea198b3d0ab30b9e8478a762488ecebabd88 (REL_15_6)
https://git.postgresql.org/gitweb/?p=postgresql.git;a=commit;h=d541ce3b6f0582723150f45d52eab119985d3c19 (REL_13_14)
https://git.postgresql.org/gitweb/?p=postgresql.git;a=commit;h=2699fc035a75d0774c1f013e9320882287f78adb (REL_12_18)
Commits have wrong CVE mentioned but the correct one is CVE-2024-0985

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2023-39417?s=debian&n=postgresql-15&ns=debian&t=deb&osn=debian&osv=12&vr=%3C15.5-0%2Bdeb12u1"><img alt="high : CVE--2023--39417" src="https://img.shields.io/badge/CVE--2023--39417-lightgrey?label=high%20&labelColor=e25d68"/></a> 

<table>
<tr><td>Affected range</td><td><code><15.5-0+deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><code>15.5-0+deb12u1</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.371%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>73rd percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

IN THE EXTENSION SCRIPT, a SQL Injection vulnerability was found in PostgreSQL if it uses @extowner@, @extschema@, or @extschema:...@ inside a quoting construct (dollar quoting, '', or ""). If an administrator has installed files of a vulnerable, trusted, non-bundled extension, an attacker with database-level CREATE privilege can execute arbitrary code as the bootstrap superuser.

---
- postgresql-15 15.4-1
- postgresql-13 <removed>
- postgresql-11 <removed>
https://www.postgresql.org/support/security/CVE-2023-39417/
https://www.postgresql.org/about/news/postgresql-154-149-1312-1216-1121-and-postgresql-16-beta-3-released-2689/
https://git.postgresql.org/gitweb/?p=postgresql.git;a=commitdiff;h=de494ec14f6bd7f2676623a5934723a6c8ba51c2 (REL_15_4)
https://git.postgresql.org/gitweb/?p=postgresql.git;a=commitdiff;h=b1b585e0fc3dd195bc2e338c80760bede08de5f1 (REL_13_12)
https://git.postgresql.org/gitweb/?p=postgresql.git;a=commitdiff;h=919ebb023e74546c6293352556365091c5402366 (REL_11_21)

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2023-5868?s=debian&n=postgresql-15&ns=debian&t=deb&osn=debian&osv=12&vr=%3C15.5-0%2Bdeb12u1"><img alt="medium : CVE--2023--5868" src="https://img.shields.io/badge/CVE--2023--5868-lightgrey?label=medium%20&labelColor=fbb552"/></a> 

<table>
<tr><td>Affected range</td><td><code><15.5-0+deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><code>15.5-0+deb12u1</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.338%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>71st percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A memory disclosure vulnerability was found in PostgreSQL that allows remote users to access sensitive information by exploiting certain aggregate function calls with 'unknown'-type arguments. Handling 'unknown'-type values from string literals without type designation can disclose bytes, potentially revealing notable and confidential information. This issue exists due to excessive data output in aggregate function calls, enabling remote users to read some portion of system memory.

---
- postgresql-16 16.1-1
- postgresql-15 <removed> (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1056283)
- postgresql-13 <removed>
- postgresql-11 <removed>
https://www.postgresql.org/support/security/CVE-2023-5868/
https://www.postgresql.org/about/news/postgresql-161-155-1410-1313-1217-and-1122-released-2749/

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2024-10978?s=debian&n=postgresql-15&ns=debian&t=deb&osn=debian&osv=12&vr=%3C15.9-0%2Bdeb12u1"><img alt="medium : CVE--2024--10978" src="https://img.shields.io/badge/CVE--2024--10978-lightgrey?label=medium%20&labelColor=fbb552"/></a> 

<table>
<tr><td>Affected range</td><td><code><15.9-0+deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><code>15.9-0+deb12u1</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.128%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>49th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

Incorrect privilege assignment in PostgreSQL allows a less-privileged application user to view or change different rows from those intended.  An attack requires the application to use SET ROLE, SET SESSION AUTHORIZATION, or an equivalent feature.  The problem arises when an application query uses parameters from the attacker or conveys query results to the attacker.  If that query reacts to current_setting('role') or the current user ID, it may modify or return data as though the session had not used SET ROLE or SET SESSION AUTHORIZATION.  The attacker does not control which incorrect user ID applies.  Query text from less-privileged sources is not a concern here, because SET ROLE and SET SESSION AUTHORIZATION are not sandboxes for unvetted queries.  Versions before PostgreSQL 17.1, 16.5, 15.9, 14.14, 13.17, and 12.21 are affected.

---
- postgresql-17 17.1-1
- postgresql-16 <removed> (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1088687)
- postgresql-15 <removed>
- postgresql-13 <removed>
https://www.postgresql.org/support/security/CVE-2024-10978/
Fixed by: https://git.postgresql.org/gitweb/?p=postgresql.git;a=commit;h=cd82afdda5e9d3269706a142e9093ba83f484185 (v17.2, 1 of 2)
Fixed by: https://git.postgresql.org/gitweb/?p=postgresql.git;a=commit;h=f4f5d27d87247da1ec7e5a6e7990a22ffba9f63a (v17.2, 2 of 2)
Fixed by: https://git.postgresql.org/gitweb/?p=postgresql.git;a=commit;h=1c05004a895308da10ec000ba6b92f72f4f5b8e2 (v17.2, regression fix)
Fixed by: https://git.postgresql.org/gitweb/?p=postgresql.git;a=commit;h=ae340d0318521ae7234ed3b7221a1f65f39a52c0 (v16.6, 1 of 2)
Fixed by: https://git.postgresql.org/gitweb/?p=postgresql.git;a=commit;h=95f5a523729f6814c8757860d9a2264148b7b0df (v16.6, 2 of 2)
Fixed by: https://git.postgresql.org/gitweb/?p=postgresql.git;a=commit;h=b0918c1286d316f6ffa93995452270afd4fc4335 (v16.6, regression fix)
Fixed by: https://git.postgresql.org/gitweb/?p=postgresql.git;a=commit;h=a5d2e6205f716c79ecfb15eb1aae75bae3f8daa9 (v15.10, 1 of 2)
Fixed by: https://git.postgresql.org/gitweb/?p=postgresql.git;a=commit;h=109a323807d752f66699a9ce0762244f536e784f (v15.10, 2 of 2)
Fixed by: https://git.postgresql.org/gitweb/?p=postgresql.git;a=commit;h=edf80895f6bda824403f843df91cbc83890e4b6c (v15.10, regression fix)
Fixed by: https://git.postgresql.org/gitweb/?p=postgresql.git;a=commit;h=2a68808e241bf667ff72c31ea9d0c4eb0b893982 (v14.15, 1 of 2)
Fixed by: https://git.postgresql.org/gitweb/?p=postgresql.git;a=commit;h=00b94e8e2f99a8ed1d7f854838234ce37f582da0 (v14.15, 2 of 2)
Fixed by: https://git.postgresql.org/gitweb/?p=postgresql.git;a=commit;h=be062bfa54d780c07a3b36c4123da2c960c8e97d (v14.15, regression fix)
Fixed by: https://git.postgresql.org/gitweb/?p=postgresql.git;a=commit;h=76123ded6e9b3624e380ac326645bd026aacd2f5 (v13.18, 1 of 2)
Fixed by: https://git.postgresql.org/gitweb/?p=postgresql.git;a=commit;h=dc7378793add3c3d9a40ec2118d92bd719acab97 (v13.18, 2 of 2)
Fixed by: https://git.postgresql.org/gitweb/?p=postgresql.git;a=commit;h=07c6e0f613612ff060572a085c1c24aa44c8b2bb (v13.18, regression fix)
Fixed by: https://git.postgresql.org/gitweb/?p=postgresql.git;a=commit;h=4c9d96f74ba4e7d01c086ca54f217e242dd65fae (v12.21, 1 of 2)
Fixed by: https://git.postgresql.org/gitweb/?p=postgresql.git;a=commit;h=0edad8654848affe0786c798aea9e1a43dde54bc (v12.21, 2 of 2)
Fixed by: https://git.postgresql.org/gitweb/?p=postgresql.git;a=commit;h=c463338656ac47e5210fcf9fbf7d20efccce8de8 (v12.21, regression fix)

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2024-10976?s=debian&n=postgresql-15&ns=debian&t=deb&osn=debian&osv=12&vr=%3C15.9-0%2Bdeb12u1"><img alt="medium : CVE--2024--10976" src="https://img.shields.io/badge/CVE--2024--10976-lightgrey?label=medium%20&labelColor=fbb552"/></a> 

<table>
<tr><td>Affected range</td><td><code><15.9-0+deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><code>15.9-0+deb12u1</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.045%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>16th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

Incomplete tracking in PostgreSQL of tables with row security allows a reused query to view or change different rows from those intended.  CVE-2023-2455 and CVE-2016-2193 fixed most interaction between row security and user ID changes.  They missed cases where a subquery, WITH query, security invoker view, or SQL-language function references a table with a row-level security policy.  This has the same consequences as the two earlier CVEs.  That is to say, it leads to potentially incorrect policies being applied in cases where role-specific policies are used and a given query is planned under one role and then executed under other roles.  This scenario can happen under security definer functions or when a common user and query is planned initially and then re-used across multiple SET ROLEs.  Applying an incorrect policy may permit a user to complete otherwise-forbidden reads and modifications.  This affects only databases that have used CREATE POLICY to define a row security policy.  An attacker must tailor an attack to a particular application's pattern of query plan reuse, user ID changes, and role-specific row security policies.  Versions before PostgreSQL 17.1, 16.5, 15.9, 14.14, 13.17, and 12.21 are affected.

---
- postgresql-17 17.1-1
- postgresql-16 <removed> (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1088687)
- postgresql-15 <removed>
- postgresql-13 <removed>
https://www.postgresql.org/support/security/CVE-2024-10976/
Fixed by: https://git.postgresql.org/gitweb/?p=postgresql.git;a=commit;h=edcda9bb4c4500b75bb4a16c7c59834398ca2906 (v17.2)
Fixed by: https://git.postgresql.org/gitweb/?p=postgresql.git;a=commit;h=562289460e118fcad44ec916dcdab21e4763c38c (v16.6)
Fixed by: https://git.postgresql.org/gitweb/?p=postgresql.git;a=commit;h=6db5ea8de8ce15897b706009aaf701d23bd65b23 (v15.10)
Fixed by: https://git.postgresql.org/gitweb/?p=postgresql.git;a=commit;h=4e51030af9e0a12d7fa06b73acd0c85024f81062 (v14.15)
Fixed by: https://git.postgresql.org/gitweb/?p=postgresql.git;a=commit;h=952ff31e2a89e8ca79ecb12d61fddbeac3d89176 (v13.18)
Fixed by: https://git.postgresql.org/gitweb/?p=postgresql.git;a=commit;h=448525e8a44080b6048e24f6942284b7eeae1a5c (v12.21)

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2024-10977?s=debian&n=postgresql-15&ns=debian&t=deb&osn=debian&osv=12&vr=%3C15.9-0%2Bdeb12u1"><img alt="low : CVE--2024--10977" src="https://img.shields.io/badge/CVE--2024--10977-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code><15.9-0+deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><code>15.9-0+deb12u1</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.046%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>19th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

Client use of server error message in PostgreSQL allows a server not trusted under current SSL or GSS settings to furnish arbitrary non-NUL bytes to the libpq application.  For example, a man-in-the-middle attacker could send a long error message that a human or screen-scraper user of psql mistakes for valid query results.  This is probably not a concern for clients where the user interface unambiguously indicates the boundary between one error message and other text.  Versions before PostgreSQL 17.1, 16.5, 15.9, 14.14, 13.17, and 12.21 are affected.

---
- postgresql-17 17.1-1
- postgresql-16 <removed> (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1088687)
- postgresql-15 <removed>
- postgresql-13 <removed>
https://www.postgresql.org/support/security/CVE-2024-10977/
Fixed by: https://git.postgresql.org/gitweb/?p=postgresql.git;a=commit;h=a5cc4c66719be2ae1eebe92ad97727dc905bbc6d (v17.2)
Fixed by: https://git.postgresql.org/gitweb/?p=postgresql.git;a=commit;h=67d28bd02ec06f5056754bc295f57d2dd2bbd749 (v16.6)
Fixed by: https://git.postgresql.org/gitweb/?p=postgresql.git;a=commit;h=d2c3e31c13a6820980c2c6019f0b8f9f0b63ae6e (v15.10)
Fixed by: https://git.postgresql.org/gitweb/?p=postgresql.git;a=commit;h=e6c9454764d880ee30735aa8c1e05d3674722ff9 (v14.15)
Fixed by: https://git.postgresql.org/gitweb/?p=postgresql.git;a=commit;h=7b49707b72612ef068ce9275b9b6da104f1960f3 (v13.18)
Fixed by: https://git.postgresql.org/gitweb/?p=postgresql.git;a=commit;h=2a951ef0aace58026c31b9a88aeeda19c9af4205 (v12.21)

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2023-5870?s=debian&n=postgresql-15&ns=debian&t=deb&osn=debian&osv=12&vr=%3C15.5-0%2Bdeb12u1"><img alt="low : CVE--2023--5870" src="https://img.shields.io/badge/CVE--2023--5870-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code><15.5-0+deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><code>15.5-0+deb12u1</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.189%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>57th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A flaw was found in PostgreSQL involving the pg_cancel_backend role that signals background workers, including the logical replication launcher, autovacuum workers, and the autovacuum launcher. Successful exploitation requires a non-core extension with a less-resilient background worker and would affect that specific background worker only. This issue may allow a remote high privileged user to launch a denial of service (DoS) attack.

---
- postgresql-16 16.1-1
- postgresql-15 <removed> (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1056283)
- postgresql-13 <removed>
- postgresql-11 <removed>
https://www.postgresql.org/support/security/CVE-2023-5870/
https://www.postgresql.org/about/news/postgresql-161-155-1410-1313-1217-and-1122-released-2749/

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2024-4317?s=debian&n=postgresql-15&ns=debian&t=deb&osn=debian&osv=12&vr=%3C15.7-0%2Bdeb12u1"><img alt="low : CVE--2024--4317" src="https://img.shields.io/badge/CVE--2024--4317-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code><15.7-0+deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><code>15.7-0+deb12u1</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.045%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>16th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

Missing authorization in PostgreSQL built-in views pg_stats_ext and pg_stats_ext_exprs allows an unprivileged database user to read most common values and other statistics from CREATE STATISTICS commands of other users. The most common values may reveal column values the eavesdropper could not otherwise read or results of functions they cannot execute. Installing an unaffected version only fixes fresh PostgreSQL installations, namely those that are created with the initdb utility after installing that version. Current PostgreSQL installations will remain vulnerable until they follow the instructions in the release notes. Within major versions 14-16, minor versions before PostgreSQL 16.3, 15.7, and 14.12 are affected. Versions before PostgreSQL 14 are unaffected.

---
- postgresql-16 16.3-1
- postgresql-15 <removed>
[bookworm] - postgresql-15 15.7-0+deb12u1
- postgresql-13 <not-affected> (Vulnerable code not present)
- postgresql-11 <not-affected> (Vulnerable code not present)
https://www.postgresql.org/support/security/CVE-2024-4317/

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2023-39418?s=debian&n=postgresql-15&ns=debian&t=deb&osn=debian&osv=12&vr=%3C15.5-0%2Bdeb12u1"><img alt="low : CVE--2023--39418" src="https://img.shields.io/badge/CVE--2023--39418-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code><15.5-0+deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><code>15.5-0+deb12u1</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.496%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>76th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A vulnerability was found in PostgreSQL with the use of the MERGE command, which fails to test new rows against row security policies defined for UPDATE and SELECT. If UPDATE and SELECT policies forbid some rows that INSERT policies do not forbid, a user could store such rows.

---
- postgresql-15 15.4-1
- postgresql-13 <not-affected> (Only affects 15.x)
- postgresql-11 <not-affected> (Only affects 15.x)
https://www.postgresql.org/support/security/CVE-2023-39418/
https://www.postgresql.org/about/news/postgresql-154-149-1312-1216-1121-and-postgresql-16-beta-3-released-2689/
https://git.postgresql.org/gitweb/?p=postgresql.git;a=commitdiff;h=cb2ae5741f2458a474ed3c31458d242e678ff229 (REL_15_4)

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 5" src="https://img.shields.io/badge/H-5-e25d68"/> <img alt="medium: 2" src="https://img.shields.io/badge/M-2-fbb552"/> <img alt="low: 0" src="https://img.shields.io/badge/L-0-lightgrey"/> <!-- unspecified: 0 --><strong>libde265</strong> <code>1.0.11-1</code> (deb)</summary>

<small><code>pkg:deb/debian/libde265@1.0.11-1?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2023-49468?s=debian&n=libde265&ns=debian&t=deb&osn=debian&osv=12&vr=%3C1.0.11-1%2Bdeb12u2"><img alt="high : CVE--2023--49468" src="https://img.shields.io/badge/CVE--2023--49468-lightgrey?label=high%20&labelColor=e25d68"/></a> 

<table>
<tr><td>Affected range</td><td><code><1.0.11-1+deb12u2</code></td></tr>
<tr><td>Fixed version</td><td><code>1.0.11-1+deb12u2</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.173%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>55th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

Libde265 v1.0.14 was discovered to contain a global buffer overflow vulnerability in the read_coding_unit function at slice.cc.

---
- libde265 1.0.15-1 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1059275)
[bookworm] - libde265 1.0.11-1+deb12u2
[bullseye] - libde265 1.0.11-0+deb11u3
https://github.com/strukturag/libde265/issues/432
Fixed by: https://github.com/strukturag/libde265/commit/3e822a3ccf88df1380b165d6ce5a00494a27ceeb (v1.0.15)

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2023-49467?s=debian&n=libde265&ns=debian&t=deb&osn=debian&osv=12&vr=%3C1.0.11-1%2Bdeb12u2"><img alt="high : CVE--2023--49467" src="https://img.shields.io/badge/CVE--2023--49467-lightgrey?label=high%20&labelColor=e25d68"/></a> 

<table>
<tr><td>Affected range</td><td><code><1.0.11-1+deb12u2</code></td></tr>
<tr><td>Fixed version</td><td><code>1.0.11-1+deb12u2</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.173%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>55th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

Libde265 v1.0.14 was discovered to contain a heap-buffer-overflow vulnerability in the derive_combined_bipredictive_merging_candidates function at motion.cc.

---
- libde265 1.0.15-1 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1059275)
[bookworm] - libde265 1.0.11-1+deb12u2
[bullseye] - libde265 1.0.11-0+deb11u3
https://github.com/strukturag/libde265/issues/434
Fixed by: https://github.com/strukturag/libde265/commit/7e4faf254bbd2e52b0f216cb987573a2cce97b54 (v1.0.15)

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2023-49465?s=debian&n=libde265&ns=debian&t=deb&osn=debian&osv=12&vr=%3C1.0.11-1%2Bdeb12u2"><img alt="high : CVE--2023--49465" src="https://img.shields.io/badge/CVE--2023--49465-lightgrey?label=high%20&labelColor=e25d68"/></a> 

<table>
<tr><td>Affected range</td><td><code><1.0.11-1+deb12u2</code></td></tr>
<tr><td>Fixed version</td><td><code>1.0.11-1+deb12u2</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.173%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>55th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

Libde265 v1.0.14 was discovered to contain a heap-buffer-overflow vulnerability in the derive_spatial_luma_vector_prediction function at motion.cc.

---
- libde265 1.0.15-1 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1059275)
[bookworm] - libde265 1.0.11-1+deb12u2
[bullseye] - libde265 1.0.11-0+deb11u3
https://github.com/strukturag/libde265/issues/435
Fixed by: https://github.com/strukturag/libde265/commit/1475c7d2f0a6dc35c27e18abc4db9679bfd32568 (v1.0.15)

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2023-27103?s=debian&n=libde265&ns=debian&t=deb&osn=debian&osv=12&vr=%3C1.0.11-1%2Bdeb12u1"><img alt="high : CVE--2023--27103" src="https://img.shields.io/badge/CVE--2023--27103-lightgrey?label=high%20&labelColor=e25d68"/></a> 

<table>
<tr><td>Affected range</td><td><code><1.0.11-1+deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><code>1.0.11-1+deb12u1</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.199%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>58th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

Libde265 v1.0.11 was discovered to contain a heap buffer overflow via the function derive_collocated_motion_vectors at motion.cc.

---
- libde265 1.0.12-1 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1033257)
[bookworm] - libde265 1.0.11-1+deb12u1
[bullseye] - libde265 1.0.11-0+deb11u2
https://github.com/strukturag/libde265/issues/394
https://github.com/strukturag/libde265/commit/d6bf73e765b7a23627bfd7a8645c143fd9097995 (v1.0.12)

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2023-43887?s=debian&n=libde265&ns=debian&t=deb&osn=debian&osv=12&vr=%3C1.0.11-1%2Bdeb12u1"><img alt="high : CVE--2023--43887" src="https://img.shields.io/badge/CVE--2023--43887-lightgrey?label=high%20&labelColor=e25d68"/></a> 

<table>
<tr><td>Affected range</td><td><code><1.0.11-1+deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><code>1.0.11-1+deb12u1</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.122%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>48th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

Libde265 v1.0.12 was discovered to contain multiple buffer overflows via the num_tile_columns and num_tile_row parameters in the function pic_parameter_set::dump.

---
- libde265 1.0.13-1
[bookworm] - libde265 1.0.11-1+deb12u1
[bullseye] - libde265 1.0.11-0+deb11u2
https://github.com/strukturag/libde265/issues/418
https://github.com/strukturag/libde265/commit/63b596c915977f038eafd7647d1db25488a8c133 (v1.0.13)

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2023-47471?s=debian&n=libde265&ns=debian&t=deb&osn=debian&osv=12&vr=%3C1.0.11-1%2Bdeb12u1"><img alt="medium : CVE--2023--47471" src="https://img.shields.io/badge/CVE--2023--47471-lightgrey?label=medium%20&labelColor=fbb552"/></a> 

<table>
<tr><td>Affected range</td><td><code><1.0.11-1+deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><code>1.0.11-1+deb12u1</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.082%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>38th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

Buffer Overflow vulnerability in strukturag libde265 v1.10.12 allows a local attacker to cause a denial of service via the slice_segment_header function in the slice.cc component.

---
- libde265 1.0.13-1 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1056187)
[bookworm] - libde265 1.0.11-1+deb12u1
[bullseye] - libde265 1.0.11-0+deb11u2
https://github.com/strukturag/libde265/issues/426
https://github.com/strukturag/libde265/commit/e36b4a1b0bafa53df47514c419d5be3e8916ebc7 (v1.0.13)

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2023-27102?s=debian&n=libde265&ns=debian&t=deb&osn=debian&osv=12&vr=%3C1.0.11-1%2Bdeb12u1"><img alt="medium : CVE--2023--27102" src="https://img.shields.io/badge/CVE--2023--27102-lightgrey?label=medium%20&labelColor=fbb552"/></a> 

<table>
<tr><td>Affected range</td><td><code><1.0.11-1+deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><code>1.0.11-1+deb12u1</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.076%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>36th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

Libde265 v1.0.11 was discovered to contain a segmentation violation via the function decoder_context::process_slice_segment_header at decctx.cc.

---
- libde265 1.0.12-1 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1033257)
[bookworm] - libde265 1.0.11-1+deb12u1
[bullseye] - libde265 1.0.11-0+deb11u2
https://github.com/strukturag/libde265/issues/393
https://github.com/strukturag/libde265/commit/0b1752abff97cb542941d317a0d18aa50cb199b1 (v1.0.12)

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 3" src="https://img.shields.io/badge/H-3-e25d68"/> <img alt="medium: 4" src="https://img.shields.io/badge/M-4-fbb552"/> <img alt="low: 7" src="https://img.shields.io/badge/L-7-fce1a9"/> <!-- unspecified: 0 --><strong>python3.11</strong> <code>3.11.2-6</code> (deb)</summary>

<small><code>pkg:deb/debian/python3.11@3.11.2-6?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2024-7592?s=debian&n=python3.11&ns=debian&t=deb&osn=debian&osv=12&vr=%3C3.11.2-6%2Bdeb12u5"><img alt="high : CVE--2024--7592" src="https://img.shields.io/badge/CVE--2024--7592-lightgrey?label=high%20&labelColor=e25d68"/></a> 

<table>
<tr><td>Affected range</td><td><code><3.11.2-6+deb12u5</code></td></tr>
<tr><td>Fixed version</td><td><code>3.11.2-6+deb12u5</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.110%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>46th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

There is a LOW severity vulnerability affecting CPython, specifically the 'http.cookies' standard library module.   When parsing cookies that contained backslashes for quoted characters in the cookie value, the parser would use an algorithm with quadratic complexity, resulting in excess CPU resources being used while parsing the value.

---
- python3.13 3.13.0~rc2-1
- python3.12 3.12.6-1
- python3.11 <removed>
[bookworm] - python3.11 3.11.2-6+deb12u5
- python3.9 <removed>
https://github.com/python/cpython/pull/123075
https://github.com/python/cpython/issues/123067
https://github.com/python/cpython/commit/391e5626e3ee5af267b97e37abc7475732e67621 (v3.13.0rc2)
https://github.com/python/cpython/commit/dcc3eaef98cd94d6cb6cb0f44bd1c903d04f33b1 (v3.12.6)
https://github.com/python/cpython/commit/d4ac921a4b081f7f996a5d2b101684b67ba0ed7f (v3.11.10)
https://github.com/python/cpython/commit/b2f11ca7667e4d57c71c1c88b255115f16042d9a (v3.10.15)
https://github.com/python/cpython/commit/d662e2db2605515a767f88ad48096b8ac623c774 (v3.9.20)
https://mail.python.org/archives/list/security-announce@python.org/thread/HXJAAAALNUNGCQUS2W7WR6GFIZIHFOOK/

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2024-6232?s=debian&n=python3.11&ns=debian&t=deb&osn=debian&osv=12&vr=%3C3.11.2-6%2Bdeb12u4"><img alt="high : CVE--2024--6232" src="https://img.shields.io/badge/CVE--2024--6232-lightgrey?label=high%20&labelColor=e25d68"/></a> 

<table>
<tr><td>Affected range</td><td><code><3.11.2-6+deb12u4</code></td></tr>
<tr><td>Fixed version</td><td><code>3.11.2-6+deb12u4</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.110%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>46th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

There is a MEDIUM severity vulnerability affecting CPython.      Regular expressions that allowed excessive backtracking during tarfile.TarFile header parsing are vulnerable to ReDoS via specifically-crafted tar archives.

---
- python3.13 3.13.0~rc2-1
- python3.12 3.12.6-1
- python3.11 <removed>
[bookworm] - python3.11 3.11.2-6+deb12u4
- python3.9 <removed>
- python2.7 <removed>
[bullseye] - python2.7 <ignored> (Unsupported in Bullseye, only included to build a few applications)
https://github.com/python/cpython/issues/121285
https://github.com/python/cpython/pull/121286
https://github.com/python/cpython/commit/ed3a49ea734ada357ff4442996fd4ae71d253373 (v3.13.0rc2)
https://github.com/python/cpython/commit/4eaf4891c12589e3c7bdad5f5b076e4c8392dd06 (v3.12.6)
https://github.com/python/cpython/commit/d449caf8a179e3b954268b3a88eb9170be3c8fbf (v3.11.10)
https://github.com/python/cpython/commit/743acbe872485dc18df4d8ab2dc7895187f062c4 (v3.10.15)

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2023-24329?s=debian&n=python3.11&ns=debian&t=deb&osn=debian&osv=12&vr=%3C3.11.2-6%2Bdeb12u2"><img alt="high : CVE--2023--24329" src="https://img.shields.io/badge/CVE--2023--24329-lightgrey?label=high%20&labelColor=e25d68"/></a> 

<table>
<tr><td>Affected range</td><td><code><3.11.2-6+deb12u2</code></td></tr>
<tr><td>Fixed version</td><td><code>3.11.2-6+deb12u2</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.197%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>58th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

An issue in the urllib.parse component of Python before 3.11.4 allows attackers to bypass blocklisting methods by supplying a URL that starts with blank characters.

---
- python3.11 3.11.4-1
[bookworm] - python3.11 3.11.2-6+deb12u2
- python3.9 <removed>
- python3.7 <removed>
[buster] - python3.7 <ignored> (Cf. related CVE-2022-0391)
- python2.7 <removed>
[bullseye] - python2.7 2.7.18-8+deb11u1
- pypy3 7.3.12+dfsg-1
[bookworm] - pypy3 7.3.11+dfsg-2+deb12u2
[buster] - pypy3 <no-dsa> (Minor issue)
https://pointernull.com/security/python-url-parse-problem.html
https://github.com/python/cpython/pull/99421
https://github.com/python/cpython/pull/99446 (backport for 3.11 branch)
https://github.com/python/cpython/commit/439b9cfaf43080e91c4ad69f312f21fa098befc7 (v3.12.0a2)
https://github.com/python/cpython/commit/72d356e3584ebfb8e813a8e9f2cd3dccf233c0d9 (v3.11.1)
The change linked above does not seem to fix the CVE:
https://github.com/python/cpython/issues/102153
https://github.com/python/cpython/pull/104575 (3.11)
https://github.com/python/cpython/pull/104592 (3.11, 3.10)
https://github.com/python/cpython/pull/104593 (3.9)
https://github.com/python/cpython/commit/2f630e1ce18ad2e07428296532a68b11dc66ad10 (v3.12.0b1)
https://github.com/python/cpython/commit/610cc0ab1b760b2abaac92bd256b96191c46b941 (v3.11.4)
https://github.com/python/cpython/commit/f48a96a28012d28ae37a2f4587a780a5eb779946 (v3.10.12)
https://github.com/python/cpython/commit/d7f8a5fe07b0ff3a419ccec434cc405b21a5a304 (v3.9.17)

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2024-0450?s=debian&n=python3.11&ns=debian&t=deb&osn=debian&osv=12&vr=%3C3.11.2-6%2Bdeb12u2"><img alt="medium : CVE--2024--0450" src="https://img.shields.io/badge/CVE--2024--0450-lightgrey?label=medium%20&labelColor=fbb552"/></a> 

<table>
<tr><td>Affected range</td><td><code><3.11.2-6+deb12u2</code></td></tr>
<tr><td>Fixed version</td><td><code>3.11.2-6+deb12u2</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.046%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>20th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

An issue was found in the CPython `zipfile` module affecting versions 3.12.1, 3.11.7, 3.10.13, 3.9.18, and 3.8.18 and prior.  The zipfile module is vulnerable to “quoted-overlap” zip-bombs which exploit the zip format to create a zip-bomb with a high compression ratio. The fixed versions of CPython makes the zipfile module reject zip archives which overlap entries in the archive.

---
- pypy3 7.3.16+dfsg-1
[bookworm] - pypy3 7.3.11+dfsg-2+deb12u2
- python3.12 3.12.2-1
- python3.11 3.11.8-1 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1070133)
[bookworm] - python3.11 3.11.2-6+deb12u2
- python3.10 <removed>
- python3.9 <removed>
- python3.7 <removed>
- python2.7 <removed>
[bullseye] - python2.7 <ignored> (Unsupported in Bullseye, only included to build a few applications)
https://github.com/python/cpython/pull/110016
https://github.com/python/cpython/issues/109858
https://github.com/python/cpython/commit/66363b9a7b9fe7c99eba3a185b74c5fdbf842eba (v3.13.0a3)
https://github.com/python/cpython/commit/fa181fcf2156f703347b03a3b1966ce47be8ab3b (v3.12.2)
https://github.com/python/cpython/commit/a956e510f6336d5ae111ba429a61c3ade30a7549 (v3.11.8)
https://github.com/python/cpython/commit/30fe5d853b56138dbec62432d370a1f99409fc85 (v3.10.14)
https://github.com/python/cpython/commit/a2c59992e9e8d35baba9695eb186ad6c6ff85c51 (v3.9.19)
https://mail.python.org/archives/list/security-announce@python.org/thread/XELNUX2L3IOHBTFU7RQHCY6OUVEWZ2FG/

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2024-6923?s=debian&n=python3.11&ns=debian&t=deb&osn=debian&osv=12&vr=%3C3.11.2-6%2Bdeb12u5"><img alt="medium : CVE--2024--6923" src="https://img.shields.io/badge/CVE--2024--6923-lightgrey?label=medium%20&labelColor=fbb552"/></a> 

<table>
<tr><td>Affected range</td><td><code><3.11.2-6+deb12u5</code></td></tr>
<tr><td>Fixed version</td><td><code>3.11.2-6+deb12u5</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.044%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>16th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

There is a MEDIUM severity vulnerability affecting CPython.  The  email module didn’t properly quote newlines for email headers when  serializing an email message allowing for header injection when an email  is serialized.

---
- python3.13 3.13.0~rc2-1
- python3.12 3.12.5-1
- python3.11 <removed>
[bookworm] - python3.11 3.11.2-6+deb12u5
- python3.9 <removed>
- python2.7 <removed>
[bullseye] - python2.7 <ignored> (Unsupported in Bullseye, only included to build a few applications)
https://github.com/python/cpython/issues/121650
https://github.com/python/cpython/pull/122233
https://github.com/python/cpython/commit/4aaa4259b5a6e664b7316a4d60bdec7ee0f124d0 (v3.13.0rc2)
https://github.com/python/cpython/commit/4766d1200fdf8b6728137aa2927a297e224d5fa7 (v3.12.5)
https://github.com/python/cpython/commit/f7c0f09e69e950cf3c5ada9dbde93898eb975533 (v3.11.10)
https://github.com/python/cpython/commit/06f28dc236708f72871c64d4bc4b4ea144c50147 (v3.10.15)
https://github.com/python/cpython/commit/f7be505d137a22528cb0fc004422c0081d5d90e6 (v3.9.20)

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2023-40217?s=debian&n=python3.11&ns=debian&t=deb&osn=debian&osv=12&vr=%3C3.11.2-6%2Bdeb12u2"><img alt="medium : CVE--2023--40217" src="https://img.shields.io/badge/CVE--2023--40217-lightgrey?label=medium%20&labelColor=fbb552"/></a> 

<table>
<tr><td>Affected range</td><td><code><3.11.2-6+deb12u2</code></td></tr>
<tr><td>Fixed version</td><td><code>3.11.2-6+deb12u2</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.115%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>47th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

An issue was discovered in Python before 3.8.18, 3.9.x before 3.9.18, 3.10.x before 3.10.13, and 3.11.x before 3.11.5. It primarily affects servers (such as HTTP servers) that use TLS client authentication. If a TLS server-side socket is created, receives data into the socket buffer, and then is closed quickly, there is a brief window where the SSLSocket instance will detect the socket as "not connected" and won't initiate a handshake, but buffered data will still be readable from the socket buffer. This data will not be authenticated if the server-side TLS peer is expecting client certificate authentication, and is indistinguishable from valid TLS stream data. Data is limited in size to the amount that will fit in the buffer. (The TLS connection cannot directly be used for data exfiltration because the vulnerable code path requires that the connection be closed on initialization of the SSLSocket.)

---
- python3.12 3.12.0~rc1-2
- python3.11 3.11.5-1
[bookworm] - python3.11 3.11.2-6+deb12u2
- python3.10 3.10.13-1
- python3.9 <removed>
- python3.7 <removed>
- python2.7 <removed>
[bullseye] - python2.7 2.7.18-8+deb11u1
- pypy3 7.3.13+dfsg-1
[bookworm] - pypy3 7.3.11+dfsg-2+deb12u2
[buster] - pypy3 <no-dsa> (Minor issue)
https://mail.python.org/archives/list/security-announce@python.org/thread/PEPLII27KYHLF4AK3ZQGKYNCRERG4YXY/
https://github.com/python/cpython/issues/108310
https://github.com/python/cpython/pull/108315
https://github.com/python/cpython/commit/0cb0c238d520a8718e313b52cffc356a5a7561bf (main)
https://github.com/python/cpython/commit/256586ab8776e4526ca594b4866b9a3492e628f1 (3.12)
https://github.com/python/cpython/commit/75a875e0df0530b75b1470d797942f90f4a718d3 (v3.11.5)
https://github.com/python/cpython/commit/37d7180cb647f0bed0c1caab0037f3bc82e2af96 (v3.10.13)
https://github.com/python/cpython/commit/264b1dacc67346efa0933d1e63f622676e0ed96b (v3.9.18)
Additional patches to stabilize the test suite may also be applied to all versions:
1. https://github.com/python/cpython/commit/64f99350351bc46e016b2286f36ba7cd669b79e3
2. https://github.com/python/cpython/commit/592bacb6fc0833336c0453e818e9b95016e9fd47

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2023-27043?s=debian&n=python3.11&ns=debian&t=deb&osn=debian&osv=12&vr=%3C3.11.2-6%2Bdeb12u5"><img alt="medium : CVE--2023--27043" src="https://img.shields.io/badge/CVE--2023--27043-lightgrey?label=medium%20&labelColor=fbb552"/></a> 

<table>
<tr><td>Affected range</td><td><code><3.11.2-6+deb12u5</code></td></tr>
<tr><td>Fixed version</td><td><code>3.11.2-6+deb12u5</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.184%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>56th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

The email module of Python through 3.11.3 incorrectly parses e-mail addresses that contain a special character. The wrong portion of an RFC2822 header is identified as the value of the addr-spec. In some applications, an attacker can bypass a protection mechanism in which application access is granted only after verifying receipt of e-mail to a specific domain (e.g., only @company.example.com addresses may be used for signup). This occurs in email/_parseaddr.py in recent versions of Python.

---
- python3.12 3.12.6-1 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1059299)
- python3.11 <removed> (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1059298)
[bookworm] - python3.11 3.11.2-6+deb12u5
- python3.10 <removed>
- python3.9 <removed>
- python3.7 <removed>
[buster] - python3.7 <postponed> (Minor issue)
- python2.7 <removed>
[bullseye] - python2.7 <ignored> (Unsupported in Bullseye, only included to build a few applications)
[buster] - python2.7 <postponed> (Minor issue)
- pypy3 7.3.17+dfsg-3 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1072179)
[bookworm] - pypy3 7.3.11+dfsg-2+deb12u3
[buster] - pypy3 <postponed> (Minor issue)
https://github.com/python/cpython/issues/102988
https://github.com/python/cpython/commit/15068242bd4405475f70a81805a8895ca309a310 (v3.12.6)
https://github.com/python/cpython/commit/bc4a703a934a59657ecd018320ef990bc5542803 (v3.11.10)
https://github.com/python/cpython/commit/2a9273a0e4466e2f057f9ce6fe98cd8ce570331b (v3.10.15)
https://github.com/python/cpython/commit/ee953f2b8fc12ee9b8209ab60a2f06c603e5a624 (v3.9.20)

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2024-9287?s=debian&n=python3.11&ns=debian&t=deb&osn=debian&osv=12&vr=%3C3.11.2-6%2Bdeb12u5"><img alt="low : CVE--2024--9287" src="https://img.shields.io/badge/CVE--2024--9287-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code><3.11.2-6+deb12u5</code></td></tr>
<tr><td>Fixed version</td><td><code>3.11.2-6+deb12u5</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.042%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>5th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A vulnerability has been found in the CPython `venv` module and CLI where path names provided when creating a virtual environment were not quoted properly, allowing the creator to inject commands into virtual environment "activation" scripts (ie "source venv/bin/activate"). This means that attacker-controlled virtual environments are able to run commands when the virtual environment is activated. Virtual environments which are not created by an attacker or which aren't activated before being used (ie "./venv/bin/python") are not affected.

---
- python3.13 3.13.1-1
- python3.12 3.12.8-1
- python3.11 <removed>
[bookworm] - python3.11 3.11.2-6+deb12u5
- python3.9 <removed>
- python2.7 <not-affected> (Vulnerable code not present)
- pypy3 7.3.17+dfsg-3 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1089117)
[bookworm] - pypy3 7.3.11+dfsg-2+deb12u3
https://mail.python.org/archives/list/security-announce@python.org/thread/RSPJ2B5JL22FG3TKUJ7D7DQ4N5JRRBZL/
https://github.com/python/cpython/issues/124651
https://github.com/python/cpython/pull/124712
https://github.com/python/cpython/commit/e52095a0c1005a87eed2276af7a1f2f66e2b6483 (v3.13.1)
https://github.com/python/cpython/commit/8450b2482586857d689b6658f08de9c8179af7db (v3.12.8)
https://github.com/python/cpython/commit/ae961ae94bf19c8f8c7fbea3d1c25cc55ce8ae97 (v3.11.11)
https://github.com/python/cpython/commit/633555735a023d3e4d92ba31da35b1205f9ecbd7 (v3.9.21)

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2024-8088?s=debian&n=python3.11&ns=debian&t=deb&osn=debian&osv=12&vr=%3C3.11.2-6%2Bdeb12u3"><img alt="low : CVE--2024--8088" src="https://img.shields.io/badge/CVE--2024--8088-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code><3.11.2-6+deb12u3</code></td></tr>
<tr><td>Fixed version</td><td><code>3.11.2-6+deb12u3</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.046%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>20th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

There is a HIGH severity vulnerability affecting the CPython "zipfile" module affecting "zipfile.Path". Note that the more common API "zipfile.ZipFile" class is unaffected.      When iterating over names of entries in a zip archive (for example, methods of "zipfile.Path" like "namelist()", "iterdir()", etc) the process can be put into an infinite loop with a maliciously crafted zip archive. This defect applies when reading only metadata or extracting the contents of the zip archive. Programs that are not handling user-controlled zip archives are not affected.

---
- python3.13 3.13.0~rc2-1
- python3.12 3.12.6-1
- python3.11 <removed>
- python3.9 <removed>
- python2.7 <not-affected> (zipfile.Path introduced in v3.8)
https://mail.python.org/archives/list/security-announce@python.org/thread/GNFCKVI4TCATKQLALJ5SN4L4CSPSMILU/
https://github.com/python/cpython/pull/122906
https://github.com/python/cpython/issues/122905
https://github.com/python/cpython/commit/8c7348939d8a3ecd79d630075f6be1b0c5b41f64 (v3.13.0rc2)
https://github.com/python/cpython/commit/dcc5182f27c1500006a1ef78e10613bb45788dea (v3.12.6)
https://github.com/python/cpython/commit/795f2597a4be988e2bb19b69ff9958e981cb894e (v3.11.10)
https://github.com/python/cpython/commit/e0264a61119d551658d9445af38323ba94fc16db (v3.10.15)
Regression (cf. #1080245): https://github.com/python/cpython/issues/123270
Regression fixed by: https://github.com/python/cpython/commit/fc0b8259e693caa8400fa8b6ac1e494e47ea7798 (v3.11.10)
Regression fixed by: https://github.com/python/cpython/commit/962055268ed4f2ca1d717bfc8b6385de50a23ab7 (v3.9.20)

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2024-4032?s=debian&n=python3.11&ns=debian&t=deb&osn=debian&osv=12&vr=%3C3.11.2-6%2Bdeb12u3"><img alt="low : CVE--2024--4032" src="https://img.shields.io/badge/CVE--2024--4032-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code><3.11.2-6+deb12u3</code></td></tr>
<tr><td>Fixed version</td><td><code>3.11.2-6+deb12u3</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.046%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>20th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

The “ipaddress” module contained incorrect information about whether certain IPv4 and IPv6 addresses were designated as “globally reachable” or “private”. This affected the is_private and is_global properties of the ipaddress.IPv4Address, ipaddress.IPv4Network, ipaddress.IPv6Address, and ipaddress.IPv6Network classes, where values wouldn’t be returned in accordance with the latest information from the IANA Special-Purpose Address Registries.  CPython 3.12.4 and 3.13.0a6 contain updated information from these registries and thus have the intended behavior.

---
- python3.13 <not-affected> (Fixed before initial upload to Debian unstable)
- python3.12 3.12.4-1
- python3.11 <removed>
- python3.9 <removed>
- python3.7 <removed>
- python2.7 <not-affected> (ipaddress module added in 3.3)
https://github.com/advisories/GHSA-mh6q-v4mp-2cc7
https://github.com/python/cpython/issues/113171
https://github.com/python/cpython/pull/113179
https://github.com/python/cpython/commit/ba431579efdcbaed7a96f2ac4ea0775879a332fb (3.11.y-branch)
https://github.com/python/cpython/commit/22adf29da8d99933ffed8647d3e0726edd16f7f8 (3.9.y-branch)

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2024-11168?s=debian&n=python3.11&ns=debian&t=deb&osn=debian&osv=12&vr=%3C3.11.2-6%2Bdeb12u5"><img alt="low : CVE--2024--11168" src="https://img.shields.io/badge/CVE--2024--11168-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code><3.11.2-6+deb12u5</code></td></tr>
<tr><td>Fixed version</td><td><code>3.11.2-6+deb12u5</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.060%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>28th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

The urllib.parse.urlsplit() and urlparse() functions improperly validated bracketed hosts (`[]`), allowing hosts that weren't IPv6 or IPvFuture. This behavior was not conformant to RFC 3986 and potentially enabled SSRF if a URL is processed by more than one URL parser.

---
- python3.12 <not-affected> (Fixed with first upload to Debian unstable)
- python3.11 3.11.4-1
[bookworm] - python3.11 3.11.2-6+deb12u5
- python3.9 <removed>
https://github.com/python/cpython/issues/103848
https://github.com/python/cpython/pull/103849
https://github.com/python/cpython/commit/29f348e232e82938ba2165843c448c2b291504c5 (v3.12.0b1)
https://github.com/python/cpython/commit/b2171a2fd41416cf68afd67460578631d755a550 (v3.11.4)

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2024-0397?s=debian&n=python3.11&ns=debian&t=deb&osn=debian&osv=12&vr=%3C3.11.2-6%2Bdeb12u3"><img alt="low : CVE--2024--0397" src="https://img.shields.io/badge/CVE--2024--0397-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code><3.11.2-6+deb12u3</code></td></tr>
<tr><td>Fixed version</td><td><code>3.11.2-6+deb12u3</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.044%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>16th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A defect was discovered in the Python “ssl” module where there is a memory race condition with the ssl.SSLContext methods “cert_store_stats()” and “get_ca_certs()”. The race condition can be triggered if the methods are called at the same time as certificates are loaded into the SSLContext, such as during the TLS handshake with a certificate directory configured. This issue is fixed in CPython 3.10.14, 3.11.9, 3.12.3, and 3.13.0a5.

---
- python3.13 <not-affected> (Fixed before initial upload to Debian unstable)
- python3.12 3.12.3-1
- python3.11 3.11.9-1
- python3.9 <removed>
- python3.7 <removed>
- python2.7 <removed>
[bullseye] - python2.7 <ignored> (Unsupported in Bullseye, only included to build a few applications)
https://github.com/advisories/GHSA-xhf3-pp4q-gxh5
https://github.com/python/cpython/issues/114572
https://github.com/python/cpython/pull/114573
https://github.com/python/cpython/commit/542f3272f56f31ed04e74c40635a913fbc12d286 (v3.12.3)
https://github.com/python/cpython/commit/01c37f1d0714f5822d34063ca7180b595abf589d (v3.11.9)
https://github.com/python/cpython/commit/b228655c227b2ca298a8ffac44d14ce3d22f6faa (3.9-branch)

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2023-6597?s=debian&n=python3.11&ns=debian&t=deb&osn=debian&osv=12&vr=%3C3.11.2-6%2Bdeb12u2"><img alt="low : CVE--2023--6597" src="https://img.shields.io/badge/CVE--2023--6597-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code><3.11.2-6+deb12u2</code></td></tr>
<tr><td>Fixed version</td><td><code>3.11.2-6+deb12u2</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.045%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>17th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

An issue was found in the CPython `tempfile.TemporaryDirectory` class affecting versions 3.12.1, 3.11.7, 3.10.13, 3.9.18, and 3.8.18 and prior.  The tempfile.TemporaryDirectory class would dereference symlinks during cleanup of permissions-related errors. This means users which can run privileged programs are potentially able to modify permissions of files referenced by symlinks in some circumstances.

---
- python3.12 3.12.1-1
- python3.11 3.11.8-1 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1070135)
[bookworm] - python3.11 3.11.2-6+deb12u2
- python3.10 <removed>
- python3.9 <removed>
- python3.7 <removed>
- python2.7 <not-affected> (tempfile.TemporaryDirectory added in 3.2)
- pypy3 7.3.13+dfsg-1
[bookworm] - pypy3 7.3.11+dfsg-2+deb12u2
[buster] - pypy3 <no-dsa> (Minor issue)
https://github.com/python/cpython/pull/99930
https://github.com/python/cpython/issues/91133
https://github.com/python/cpython/commit/6ceb8aeda504b079fef7a57b8d81472f15cdd9a5 (v3.12.1)
https://github.com/python/cpython/commit/5585334d772b253a01a6730e8202ffb1607c3d25 (v3.11.8)
https://github.com/python/cpython/commit/8eaeefe49d179ca4908d052745e3bb8b6f238f82 (v3.10.14)
https://github.com/python/cpython/commit/d54e22a669ae6e987199bb5d2c69bb5a46b0083b (v3.9.19)
https://mail.python.org/archives/list/security-announce@python.org/thread/Q5C6ATFC67K53XFV4KE45325S7NS62LD/
Introduced by: https://github.com/python/cpython/commit/e9b51c0ad81da1da11ae65840ac8b50a8521373c (v3.8.0b1)

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2023-41105?s=debian&n=python3.11&ns=debian&t=deb&osn=debian&osv=12&vr=%3C3.11.2-6%2Bdeb12u2"><img alt="low : CVE--2023--41105" src="https://img.shields.io/badge/CVE--2023--41105-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code><3.11.2-6+deb12u2</code></td></tr>
<tr><td>Fixed version</td><td><code>3.11.2-6+deb12u2</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.125%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>48th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

An issue was discovered in Python 3.11 through 3.11.4. If a path containing '\0' bytes is passed to os.path.normpath(), the path will be truncated unexpectedly at the first '\0' byte. There are plausible cases in which an application would have rejected a filename for security reasons in Python 3.10.x or earlier, but that filename is no longer rejected in Python 3.11.x.

---
- python3.12 3.12.0~rc1-2
- python3.11 3.11.5-1
[bookworm] - python3.11 3.11.2-6+deb12u2
- python3.10 <not-affected> (Vulnerable code introduced in 3.11.y)
- python3.9 <not-affected> (Vulnerable code introduced in 3.11.y)
- python3.7 <not-affected> (Vulnerable code introduced in 3.11.y)
- python2.7 <not-affected> (Vulnerable code introduced in 3.11.y)
https://github.com/python/cpython/issues/106242
https://github.com/python/cpython/pull/107983
Backport for 3.12: https://github.com/python/cpython/pull/107981
Backport for 3.11: https://github.com/python/cpython/pull/107982

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 3" src="https://img.shields.io/badge/H-3-e25d68"/> <img alt="medium: 1" src="https://img.shields.io/badge/M-1-fbb552"/> <img alt="low: 4" src="https://img.shields.io/badge/L-4-fce1a9"/> <img alt="unspecified: 3" src="https://img.shields.io/badge/U-3-lightgrey"/><strong>glibc</strong> <code>2.36-9</code> (deb)</summary>

<small><code>pkg:deb/debian/glibc@2.36-9?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2023-4911?s=debian&n=glibc&ns=debian&t=deb&osn=debian&osv=12&vr=%3C2.36-9%2Bdeb12u3"><img alt="high : CVE--2023--4911" src="https://img.shields.io/badge/CVE--2023--4911-lightgrey?label=high%20&labelColor=e25d68"/></a> 

<table>
<tr><td>Affected range</td><td><code><2.36-9+deb12u3</code></td></tr>
<tr><td>Fixed version</td><td><code>2.36-9+deb12u3</code></td></tr>
<tr><td>EPSS Score</td><td><code>24.763%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>97th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A buffer overflow was discovered in the GNU C Library's dynamic loader ld.so while processing the GLIBC_TUNABLES environment variable. This issue could allow a local attacker to use maliciously crafted GLIBC_TUNABLES environment variables when launching binaries with SUID permission to execute code with elevated privileges.

---
- glibc 2.37-12
[buster] - glibc <not-affected> (Vulnerable code introduced later)
https://www.openwall.com/lists/oss-security/2023/10/03/2
Introduced by: https://sourceware.org/git/?p=glibc.git;a=commit;h=2ed18c5b534d9e92fc006202a5af0df6b72e7aca (glibc-2.34; backported in debian/2.31-12)
Fixed by: https://sourceware.org/git/?p=glibc.git;a=commit;h=1056e5b4c3f2d90ed2b4a55f96add28da2f4c8fa
https://www.qualys.com/2023/10/03/cve-2023-4911/looney-tunables-local-privilege-escalation-glibc-ld-so.txt
https://sourceware.org/cgit/glibc/tree/advisories/GLIBC-SA-2023-0004

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2024-33602?s=debian&n=glibc&ns=debian&t=deb&osn=debian&osv=12&vr=%3C2.36-9%2Bdeb12u7"><img alt="high : CVE--2024--33602" src="https://img.shields.io/badge/CVE--2024--33602-lightgrey?label=high%20&labelColor=e25d68"/></a> 

<table>
<tr><td>Affected range</td><td><code><2.36-9+deb12u7</code></td></tr>
<tr><td>Fixed version</td><td><code>2.36-9+deb12u7</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.045%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>18th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

nscd: netgroup cache assumes NSS callback uses in-buffer strings  The Name Service Cache Daemon's (nscd) netgroup cache can corrupt memory when the NSS callback does not store all strings in the provided buffer. The flaw was introduced in glibc 2.15 when the cache was added to nscd.  This vulnerability is only present in the nscd binary.

---
- glibc 2.37-19
https://sourceware.org/bugzilla/show_bug.cgi?id=31680
https://inbox.sourceware.org/libc-alpha/cover.1713974801.git.fweimer@redhat.com/
https://www.openwall.com/lists/oss-security/2024/04/24/2
https://sourceware.org/git/?p=glibc.git;a=blob;f=advisories/GLIBC-SA-2024-0008
Fixed by: https://sourceware.org/git?p=glibc.git;a=commit;h=c04a21e050d64a1193a6daab872bca2528bda44b

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2024-2961?s=debian&n=glibc&ns=debian&t=deb&osn=debian&osv=12&vr=%3C2.36-9%2Bdeb12u6"><img alt="high : CVE--2024--2961" src="https://img.shields.io/badge/CVE--2024--2961-lightgrey?label=high%20&labelColor=e25d68"/></a> 

<table>
<tr><td>Affected range</td><td><code><2.36-9+deb12u6</code></td></tr>
<tr><td>Fixed version</td><td><code>2.36-9+deb12u6</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.071%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>34th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

The iconv() function in the GNU C Library versions 2.39 and older may overflow the output buffer passed to it by up to 4 bytes when converting strings to the ISO-2022-CN-EXT character set, which may be used to crash an application or overwrite a neighbouring variable.

---
- glibc 2.37-18 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1069191)
https://www.openwall.com/lists/oss-security/2024/04/17/9
https://www.openwall.com/lists/oss-security/2024/04/18/4
https://sourceware.org/git/?p=glibc.git;a=blob;f=advisories/GLIBC-SA-2024-0004
Introduced by: https://sourceware.org/git?p=glibc.git;a=commit;h=755104edc75c53f4a0e7440334e944ad3c6b32fc (cvs/libc-2_1_94)
Fixed by: https://sourceware.org/git?p=glibc.git;a=commit;h=f9dc609e06b1136bb0408be9605ce7973a767ada
https://www.ambionics.io/blog/iconv-cve-2024-2961-p1
https://github.com/ambionics/cnext-exploits/

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2023-4806?s=debian&n=glibc&ns=debian&t=deb&osn=debian&osv=12&vr=%3C2.36-9%2Bdeb12u3"><img alt="medium : CVE--2023--4806" src="https://img.shields.io/badge/CVE--2023--4806-lightgrey?label=medium%20&labelColor=fbb552"/></a> 

<table>
<tr><td>Affected range</td><td><code><2.36-9+deb12u3</code></td></tr>
<tr><td>Fixed version</td><td><code>2.36-9+deb12u3</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.125%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>48th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A flaw was found in glibc. In an extremely rare situation, the getaddrinfo function may access memory that has been freed, resulting in an application crash. This issue is only exploitable when a NSS module implements only the _nss_*_gethostbyname2_r and _nss_*_getcanonname_r hooks without implementing the _nss_*_gethostbyname3_r hook. The resolved name should return a large number of IPv6 and IPv4, and the call to the getaddrinfo function should have the AF_INET6 address family with AI_CANONNAME, AI_ALL and AI_V4MAPPED as flags.

---
- glibc 2.37-10
[bookworm] - glibc 2.36-9+deb12u3
[bullseye] - glibc <ignored> (Minor issue)
[buster] - glibc <no-dsa> (Minor issue)
https://sourceware.org/bugzilla/show_bug.cgi?id=30843
https://sourceware.org/git/gitweb.cgi?p=glibc.git;h=973fe93a5675c42798b2161c6f29c01b0e243994
When fixing this issue in older releases make sure to not open CVE-2023-5156.
https://sourceware.org/cgit/glibc/tree/advisories/GLIBC-SA-2023-0003

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2023-6780?s=debian&n=glibc&ns=debian&t=deb&osn=debian&osv=12&vr=%3C2.36-9%2Bdeb12u4"><img alt="low : CVE--2023--6780" src="https://img.shields.io/badge/CVE--2023--6780-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code><2.36-9+deb12u4</code></td></tr>
<tr><td>Fixed version</td><td><code>2.36-9+deb12u4</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.219%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>60th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

An integer overflow was found in the __vsyslog_internal function of the glibc library. This function is called by the syslog and vsyslog functions. This issue occurs when these functions are called with a very long message, leading to an incorrect calculation of the buffer size to store the message, resulting in undefined behavior. This issue affects glibc 2.37 and newer.

---
- glibc 2.37-15
[bullseye] - glibc <not-affected> (Vulnerable code not present)
[buster] - glibc <not-affected> (Vulnerable code not present)
Fixed by: https://sourceware.org/git/?p=glibc.git;a=commit;h=ddf542da94caf97ff43cc2875c88749880b7259b
https://sourceware.org/pipermail/libc-announce/2024/000037.html
https://sourceware.org/git/?p=glibc.git;a=blob_plain;f=advisories/GLIBC-SA-2024-0003;hb=HEAD
https://sourceware.org/cgit/glibc/tree/advisories/GLIBC-SA-2024-0003

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2023-6779?s=debian&n=glibc&ns=debian&t=deb&osn=debian&osv=12&vr=%3C2.36-9%2Bdeb12u4"><img alt="low : CVE--2023--6779" src="https://img.shields.io/badge/CVE--2023--6779-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code><2.36-9+deb12u4</code></td></tr>
<tr><td>Fixed version</td><td><code>2.36-9+deb12u4</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.302%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>70th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

An off-by-one heap-based buffer overflow was found in the __vsyslog_internal function of the glibc library. This function is called by the syslog and vsyslog functions. This issue occurs when these functions are called with a message bigger than INT_MAX bytes, leading to an incorrect calculation of the buffer size to store the message, resulting in an application crash. This issue affects glibc 2.37 and newer.

---
- glibc 2.37-15
[bullseye] - glibc <not-affected> (Vulnerable code not present)
[buster] - glibc <not-affected> (Vulnerable code not present)
Fixed by: https://sourceware.org/git/?p=glibc.git;a=commit;h=7e5a0c286da33159d47d0122007aac016f3e02cd
https://sourceware.org/pipermail/libc-announce/2024/000037.html
https://sourceware.org/git/?p=glibc.git;a=blob_plain;f=advisories/GLIBC-SA-2024-0002;hb=HEAD
https://sourceware.org/cgit/glibc/tree/advisories/GLIBC-SA-2024-0002

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2023-6246?s=debian&n=glibc&ns=debian&t=deb&osn=debian&osv=12&vr=%3C2.36-9%2Bdeb12u4"><img alt="low : CVE--2023--6246" src="https://img.shields.io/badge/CVE--2023--6246-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code><2.36-9+deb12u4</code></td></tr>
<tr><td>Fixed version</td><td><code>2.36-9+deb12u4</code></td></tr>
<tr><td>EPSS Score</td><td><code>1.508%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>87th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A heap-based buffer overflow was found in the __vsyslog_internal function of the glibc library. This function is called by the syslog and vsyslog functions. This issue occurs when the openlog function was not called, or called with the ident argument set to NULL, and the program name (the basename of argv[0]) is bigger than 1024 bytes, resulting in an application crash or local privilege escalation. This issue affects glibc 2.36 and newer.

---
- glibc 2.37-15
[bullseye] - glibc <not-affected> (Vulnerable code not present)
[buster] - glibc <not-affected> (Vulnerable code not present)
https://www.qualys.com/2024/01/30/syslog
Introduced by: https://sourceware.org/git?p=glibc.git;a=commit;h=52a5be0df411ef3ff45c10c7c308cb92993d15b1
Fixed by: https://sourceware.org/git?p=glibc.git;a=commit;h=6bd0e4efcc78f3c0115e5ea9739a1642807450da
https://sourceware.org/pipermail/libc-announce/2024/000037.html
https://sourceware.org/git/?p=glibc.git;a=blob_plain;f=advisories/GLIBC-SA-2024-0001;hb=HEAD
https://sourceware.org/cgit/glibc/tree/advisories/GLIBC-SA-2024-0001

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2023-4527?s=debian&n=glibc&ns=debian&t=deb&osn=debian&osv=12&vr=%3C2.36-9%2Bdeb12u3"><img alt="low : CVE--2023--4527" src="https://img.shields.io/badge/CVE--2023--4527-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code><2.36-9+deb12u3</code></td></tr>
<tr><td>Fixed version</td><td><code>2.36-9+deb12u3</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.146%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>52nd percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A flaw was found in glibc. When the getaddrinfo function is called with the AF_UNSPEC address family and the system is configured with no-aaaa mode via /etc/resolv.conf, a DNS response via TCP larger than 2048 bytes can potentially disclose stack contents through the function returned address data, and may cause a crash.

---
- glibc 2.37-9 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1051958)
[bookworm] - glibc 2.36-9+deb12u3
[bullseye] - glibc <not-affected> (Vulnerable code not present)
[buster] - glibc <not-affected> (Vulnerable code not present)
https://sourceware.org/bugzilla/show_bug.cgi?id=30842
Introduced by: https://sourceware.org/git/?p=glibc.git;a=commitdiff;h=f282cdbe7f436c75864e5640a409a10485e9abb2 (glibc-2.36)
Fixed by: https://sourceware.org/git/gitweb.cgi?p=glibc.git;h=4ea972b7edd7e36610e8cde18bf7a8149d7bac4f (release/2.36/master branch)
Fixed by: https://sourceware.org/git/gitweb.cgi?p=glibc.git;h=b7529346025a130fee483d42178b5c118da971bb (release/2.37/master branch)
Fixed by: https://sourceware.org/git/gitweb.cgi?p=glibc.git;h=b25508dd774b617f99419bdc3cf2ace4560cd2d6 (release/2.38/master branch)
https://www.openwall.com/lists/oss-security/2023/09/25/1
https://sourceware.org/cgit/glibc/tree/advisories/GLIBC-SA-2023-0002

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2024-33601?s=debian&n=glibc&ns=debian&t=deb&osn=debian&osv=12&vr=%3C2.36-9%2Bdeb12u7"><img alt="unspecified : CVE--2024--33601" src="https://img.shields.io/badge/CVE--2024--33601-lightgrey?label=unspecified%20&labelColor=lightgrey"/></a> 

<table>
<tr><td>Affected range</td><td><code><2.36-9+deb12u7</code></td></tr>
<tr><td>Fixed version</td><td><code>2.36-9+deb12u7</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.045%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>18th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

nscd: netgroup cache may terminate daemon on memory allocation failure  The Name Service Cache Daemon's (nscd) netgroup cache uses xmalloc or xrealloc and these functions may terminate the process due to a memory allocation failure resulting in a denial of service to the clients.  The flaw was introduced in glibc 2.15 when the cache was added to nscd.  This vulnerability is only present in the nscd binary.

---
- glibc 2.37-19
https://sourceware.org/bugzilla/show_bug.cgi?id=31679
https://inbox.sourceware.org/libc-alpha/cover.1713974801.git.fweimer@redhat.com/
https://www.openwall.com/lists/oss-security/2024/04/24/2
https://sourceware.org/git/?p=glibc.git;a=blob;f=advisories/GLIBC-SA-2024-0007
Fixed by: https://sourceware.org/git?p=glibc.git;a=commit;h=c04a21e050d64a1193a6daab872bca2528bda44b

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2024-33600?s=debian&n=glibc&ns=debian&t=deb&osn=debian&osv=12&vr=%3C2.36-9%2Bdeb12u7"><img alt="unspecified : CVE--2024--33600" src="https://img.shields.io/badge/CVE--2024--33600-lightgrey?label=unspecified%20&labelColor=lightgrey"/></a> 

<table>
<tr><td>Affected range</td><td><code><2.36-9+deb12u7</code></td></tr>
<tr><td>Fixed version</td><td><code>2.36-9+deb12u7</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.045%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>18th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

nscd: Null pointer crashes after notfound response  If the Name Service Cache Daemon's (nscd) cache fails to add a not-found netgroup response to the cache, the client request can result in a null pointer dereference.  This flaw was introduced in glibc 2.15 when the cache was added to nscd.  This vulnerability is only present in the nscd binary.

---
- glibc 2.37-19
https://sourceware.org/bugzilla/show_bug.cgi?id=31678
https://inbox.sourceware.org/libc-alpha/cover.1713974801.git.fweimer@redhat.com/
https://www.openwall.com/lists/oss-security/2024/04/24/2
https://sourceware.org/git/?p=glibc.git;a=blob;f=advisories/GLIBC-SA-2024-0006
Fixed by: https://sourceware.org/git?p=glibc.git;a=commit;h=b048a482f088e53144d26a61c390bed0210f49f2
Fixed by: https://sourceware.org/git/?p=glibc.git;a=commit;h=7835b00dbce53c3c87bbbb1754a95fb5e58187aa

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2024-33599?s=debian&n=glibc&ns=debian&t=deb&osn=debian&osv=12&vr=%3C2.36-9%2Bdeb12u7"><img alt="unspecified : CVE--2024--33599" src="https://img.shields.io/badge/CVE--2024--33599-lightgrey?label=unspecified%20&labelColor=lightgrey"/></a> 

<table>
<tr><td>Affected range</td><td><code><2.36-9+deb12u7</code></td></tr>
<tr><td>Fixed version</td><td><code>2.36-9+deb12u7</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.045%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>18th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

nscd: Stack-based buffer overflow in netgroup cache  If the Name Service Cache Daemon's (nscd) fixed size cache is exhausted by client requests then a subsequent client request for netgroup data may result in a stack-based buffer overflow.  This flaw was introduced in glibc 2.15 when the cache was added to nscd.  This vulnerability is only present in the nscd binary.

---
- glibc 2.37-19
https://sourceware.org/bugzilla/show_bug.cgi?id=31677
https://inbox.sourceware.org/libc-alpha/cover.1713974801.git.fweimer@redhat.com/
https://www.openwall.com/lists/oss-security/2024/04/24/2
https://sourceware.org/git/?p=glibc.git;a=blob;f=advisories/GLIBC-SA-2024-0005
Fixed by: https://sourceware.org/git?p=glibc.git;a=commit;h=87801a8fd06db1d654eea3e4f7626ff476a9bdaa

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 2" src="https://img.shields.io/badge/H-2-e25d68"/> <img alt="medium: 8" src="https://img.shields.io/badge/M-8-fbb552"/> <img alt="low: 0" src="https://img.shields.io/badge/L-0-lightgrey"/> <img alt="unspecified: 2" src="https://img.shields.io/badge/U-2-lightgrey"/><strong>tiff</strong> <code>4.5.0-6</code> (deb)</summary>

<small><code>pkg:deb/debian/tiff@4.5.0-6?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2024-7006?s=debian&n=tiff&ns=debian&t=deb&osn=debian&osv=12&vr=%3C4.5.0-6%2Bdeb12u2"><img alt="high : CVE--2024--7006" src="https://img.shields.io/badge/CVE--2024--7006-lightgrey?label=high%20&labelColor=e25d68"/></a> 

<table>
<tr><td>Affected range</td><td><code><4.5.0-6+deb12u2</code></td></tr>
<tr><td>Fixed version</td><td><code>4.5.0-6+deb12u2</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.050%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>23rd percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A null pointer dereference flaw was found in Libtiff via `tif_dirinfo.c`. This issue may allow an attacker to trigger memory allocation failures through certain means, such as restricting the heap space size or injecting faults, causing a segmentation fault. This can cause an application crash, eventually leading to a denial of service.

---
- tiff 4.5.1+git230720-5 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1078648)
[bookworm] - tiff 4.5.0-6+deb12u2
https://gitlab.com/libtiff/libtiff/-/merge_requests/559
https://gitlab.com/libtiff/libtiff/-/issues/624
Fixed by: https://gitlab.com/libtiff/libtiff/-/commit/818fb8ce881cf839fbc710f6690aadb992aa0f9e

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2023-52356?s=debian&n=tiff&ns=debian&t=deb&osn=debian&osv=12&vr=%3C4.5.0-6%2Bdeb12u2"><img alt="high : CVE--2023--52356" src="https://img.shields.io/badge/CVE--2023--52356-lightgrey?label=high%20&labelColor=e25d68"/></a> 

<table>
<tr><td>Affected range</td><td><code><4.5.0-6+deb12u2</code></td></tr>
<tr><td>Fixed version</td><td><code>4.5.0-6+deb12u2</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.232%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>61st percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A segment fault (SEGV) flaw was found in libtiff that could be triggered by passing a crafted tiff file to the TIFFReadRGBATileExt() API. This flaw allows a remote attacker to cause a heap-buffer overflow, leading to a denial of service.

---
- tiff 4.5.1+git230720-4 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1061524)
[bookworm] - tiff 4.5.0-6+deb12u2
https://gitlab.com/libtiff/libtiff/-/issues/622
https://gitlab.com/libtiff/libtiff/-/merge_requests/546
https://gitlab.com/libtiff/libtiff/-/commit/51558511bdbbcffdce534db21dbaf5d54b31638a

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2023-41175?s=debian&n=tiff&ns=debian&t=deb&osn=debian&osv=12&vr=%3C4.5.0-6%2Bdeb12u1"><img alt="medium : CVE--2023--41175" src="https://img.shields.io/badge/CVE--2023--41175-lightgrey?label=medium%20&labelColor=fbb552"/></a> 

<table>
<tr><td>Affected range</td><td><code><4.5.0-6+deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><code>4.5.0-6+deb12u1</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.137%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>50th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A vulnerability was found in libtiff due to multiple potential integer overflows in raw2tiff.c. This flaw allows remote attackers to cause a denial of service or possibly execute an arbitrary code via a crafted tiff image, which triggers a heap-based buffer overflow.

---
- tiff 4.5.1+git230720-1
https://gitlab.com/libtiff/libtiff/-/issues/592
https://gitlab.com/libtiff/libtiff/-/commit/6e2dac5f904496d127c92ddc4e56eccfca25c2ee
https://bugzilla.redhat.com/show_bug.cgi?id=2235264

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2023-40745?s=debian&n=tiff&ns=debian&t=deb&osn=debian&osv=12&vr=%3C4.5.0-6%2Bdeb12u1"><img alt="medium : CVE--2023--40745" src="https://img.shields.io/badge/CVE--2023--40745-lightgrey?label=medium%20&labelColor=fbb552"/></a> 

<table>
<tr><td>Affected range</td><td><code><4.5.0-6+deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><code>4.5.0-6+deb12u1</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.137%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>50th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

LibTIFF is vulnerable to an integer overflow. This flaw allows remote attackers to cause a denial of service (application crash) or possibly execute an arbitrary code via a crafted tiff image, which triggers a heap-based buffer overflow.

---
- tiff 4.5.1+git230720-1
https://gitlab.com/libtiff/libtiff/-/commit/4fc16f649fa2875d5c388cf2edc295510a247ee5
https://gitlab.com/libtiff/libtiff/-/issues/591
https://bugzilla.redhat.com/show_bug.cgi?id=2235265

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2023-3618?s=debian&n=tiff&ns=debian&t=deb&osn=debian&osv=12&vr=%3C4.5.0-6%2Bdeb12u2"><img alt="medium : CVE--2023--3618" src="https://img.shields.io/badge/CVE--2023--3618-lightgrey?label=medium%20&labelColor=fbb552"/></a> 

<table>
<tr><td>Affected range</td><td><code><4.5.0-6+deb12u2</code></td></tr>
<tr><td>Fixed version</td><td><code>4.5.0-6+deb12u2</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.535%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>77th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A flaw was found in libtiff. A specially crafted tiff file can lead to a segmentation fault due to a buffer overflow in the Fax3Encode function in libtiff/tif_fax3.c, resulting in a denial of service.

---
- tiff 4.5.1~rc3-1 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1040945)
[bookworm] - tiff 4.5.0-6+deb12u2
https://gitlab.com/libtiff/libtiff/-/issues/529
https://gitlab.com/libtiff/libtiff/-/commit/b5c7d4c4e03333ac16b5cfb11acaaeaa493334f8 (v4.5.1rc1)

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2023-3576?s=debian&n=tiff&ns=debian&t=deb&osn=debian&osv=12&vr=%3C4.5.0-6%2Bdeb12u1"><img alt="medium : CVE--2023--3576" src="https://img.shields.io/badge/CVE--2023--3576-lightgrey?label=medium%20&labelColor=fbb552"/></a> 

<table>
<tr><td>Affected range</td><td><code><4.5.0-6+deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><code>4.5.0-6+deb12u1</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.049%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>21st percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A memory leak flaw was found in Libtiff's tiffcrop utility. This issue occurs when tiffcrop operates on a TIFF image file, allowing an attacker to pass a crafted TIFF image file to tiffcrop utility, which causes this memory leak issue, resulting an application crash, eventually leading to a denial of service.

---
- tiff 4.5.1~rc3-1
https://gitlab.com/libtiff/libtiff/-/merge_requests/475
Fixed by: https://gitlab.com/libtiff/libtiff/-/commit/1d5b1181c980090a6518f11e61a18b0e268bf31a (v4.5.1rc1)

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2023-2908?s=debian&n=tiff&ns=debian&t=deb&osn=debian&osv=12&vr=%3C4.5.0-6%2Bdeb12u2"><img alt="medium : CVE--2023--2908" src="https://img.shields.io/badge/CVE--2023--2908-lightgrey?label=medium%20&labelColor=fbb552"/></a> 

<table>
<tr><td>Affected range</td><td><code><4.5.0-6+deb12u2</code></td></tr>
<tr><td>Fixed version</td><td><code>4.5.0-6+deb12u2</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.105%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>45th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A null pointer dereference issue was found in Libtiff's tif_dir.c file. This issue may allow an attacker to pass a crafted TIFF image file to the tiffcp utility which triggers a runtime error that causes undefined behavior. This will result in an application crash, eventually leading to a denial of service.

---
- tiff 4.5.1~rc3-1
[bookworm] - tiff 4.5.0-6+deb12u2
https://gitlab.com/libtiff/libtiff/-/merge_requests/479
https://gitlab.com/libtiff/libtiff/-/commit/9bd48f0dbd64fb94dc2b5b05238fde0bfdd4ff3f (v4.5.1rc1)
Introduced by the fix for CVE-2022-3599/CVE-2022-4645/CVE-2023-30086/CVE-2023-30774:
https://gitlab.com/libtiff/libtiff/-/commit/e813112545942107551433d61afd16ac094ff246 (v4.5.0rc1)

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2023-26966?s=debian&n=tiff&ns=debian&t=deb&osn=debian&osv=12&vr=%3C4.5.0-6%2Bdeb12u2"><img alt="medium : CVE--2023--26966" src="https://img.shields.io/badge/CVE--2023--26966-lightgrey?label=medium%20&labelColor=fbb552"/></a> 

<table>
<tr><td>Affected range</td><td><code><4.5.0-6+deb12u2</code></td></tr>
<tr><td>Fixed version</td><td><code>4.5.0-6+deb12u2</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.080%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>37th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

libtiff 4.5.0 is vulnerable to Buffer Overflow in uv_encode() when libtiff reads a corrupted little-endian TIFF file and specifies the output to be big-endian.

---
- tiff 4.5.1~rc3-1
[bookworm] - tiff 4.5.0-6+deb12u2
https://gitlab.com/libtiff/libtiff/-/issues/530
https://gitlab.com/libtiff/libtiff/-/merge_requests/473
https://gitlab.com/libtiff/libtiff/-/commit/b0e1c25dd1d065200c8d8f59ad0afe014861a1b9 (v4.5.1rc1)

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2023-26965?s=debian&n=tiff&ns=debian&t=deb&osn=debian&osv=12&vr=%3C4.5.0-6%2Bdeb12u2"><img alt="medium : CVE--2023--26965" src="https://img.shields.io/badge/CVE--2023--26965-lightgrey?label=medium%20&labelColor=fbb552"/></a> 

<table>
<tr><td>Affected range</td><td><code><4.5.0-6+deb12u2</code></td></tr>
<tr><td>Fixed version</td><td><code>4.5.0-6+deb12u2</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.114%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>46th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

loadImage() in tools/tiffcrop.c in LibTIFF through 4.5.0 has a heap-based use after free via a crafted TIFF image.

---
- tiff 4.5.1~rc3-1
[bookworm] - tiff 4.5.0-6+deb12u2
https://gitlab.com/libtiff/libtiff/-/merge_requests/472
https://gitlab.com/libtiff/libtiff/-/commit/ec8ef90c1f573c9eb1f17d6a056aa0015f184acf (v4.5.1rc1)

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2023-25433?s=debian&n=tiff&ns=debian&t=deb&osn=debian&osv=12&vr=%3C4.5.0-6%2Bdeb12u2"><img alt="medium : CVE--2023--25433" src="https://img.shields.io/badge/CVE--2023--25433-lightgrey?label=medium%20&labelColor=fbb552"/></a> 

<table>
<tr><td>Affected range</td><td><code><4.5.0-6+deb12u2</code></td></tr>
<tr><td>Fixed version</td><td><code>4.5.0-6+deb12u2</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.080%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>37th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

libtiff 4.5.0 is vulnerable to Buffer Overflow via /libtiff/tools/tiffcrop.c:8499. Incorrect updating of buffer size after rotateImage() in tiffcrop cause heap-buffer-overflow and SEGV.

---
- tiff 4.5.1~rc3-1
[bookworm] - tiff 4.5.0-6+deb12u2
https://gitlab.com/libtiff/libtiff/-/issues/520
https://gitlab.com/libtiff/libtiff/-/commit/9c22495e5eeeae9e00a1596720c969656bb8d678 (v4.5.1rc1)
https://gitlab.com/libtiff/libtiff/-/commit/688012dca2c39033aa2dc7bcea9796787cfd1b44 (v4.5.1rc1)

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2023-38289?s=debian&n=tiff&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D4.5.0-6"><img alt="unspecified : CVE--2023--38289" src="https://img.shields.io/badge/CVE--2023--38289-lightgrey?label=unspecified%20&labelColor=lightgrey"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=4.5.0-6</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

REJECTED

---
REJECTED

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2023-38288?s=debian&n=tiff&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D4.5.0-6"><img alt="unspecified : CVE--2023--38288" src="https://img.shields.io/badge/CVE--2023--38288-lightgrey?label=unspecified%20&labelColor=lightgrey"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=4.5.0-6</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

REJECTED

---
REJECTED

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 2" src="https://img.shields.io/badge/H-2-e25d68"/> <img alt="medium: 4" src="https://img.shields.io/badge/M-4-fbb552"/> <img alt="low: 0" src="https://img.shields.io/badge/L-0-lightgrey"/> <!-- unspecified: 0 --><strong>gnutls28</strong> <code>3.7.9-2</code> (deb)</summary>

<small><code>pkg:deb/debian/gnutls28@3.7.9-2?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2024-0567?s=debian&n=gnutls28&ns=debian&t=deb&osn=debian&osv=12&vr=%3C3.7.9-2%2Bdeb12u2"><img alt="high : CVE--2024--0567" src="https://img.shields.io/badge/CVE--2024--0567-lightgrey?label=high%20&labelColor=e25d68"/></a> 

<table>
<tr><td>Affected range</td><td><code><3.7.9-2+deb12u2</code></td></tr>
<tr><td>Fixed version</td><td><code>3.7.9-2+deb12u2</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.421%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>74th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A vulnerability was found in GnuTLS, where a cockpit (which uses gnuTLS) rejects a certificate chain with distributed trust. This issue occurs when validating a certificate chain with cockpit-certificate-ensure. This flaw allows an unauthenticated, remote client or attacker to initiate a denial of service attack.

---
- gnutls28 3.8.3-1 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1061045)
[bookworm] - gnutls28 3.7.9-2+deb12u2
[bullseye] - gnutls28 3.7.1-5+deb11u5
[buster] - gnutls28 <not-affected> (Vulnerabity introduced in 3.7)
https://gitlab.com/gnutls/gnutls/-/issues/1521
https://gnutls.org/security-new.html#GNUTLS-SA-2024-01-09
https://lists.gnupg.org/pipermail/gnutls-help/2024-January/004841.html
https://gitlab.com/gnutls/gnutls/-/commit/9edbdaa84e38b1bfb53a7d72c1de44f8de373405 (3.8.3)

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2024-0553?s=debian&n=gnutls28&ns=debian&t=deb&osn=debian&osv=12&vr=%3C3.7.9-2%2Bdeb12u2"><img alt="high : CVE--2024--0553" src="https://img.shields.io/badge/CVE--2024--0553-lightgrey?label=high%20&labelColor=e25d68"/></a> 

<table>
<tr><td>Affected range</td><td><code><3.7.9-2+deb12u2</code></td></tr>
<tr><td>Fixed version</td><td><code>3.7.9-2+deb12u2</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.441%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>75th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A vulnerability was found in GnuTLS. The response times to malformed ciphertexts in RSA-PSK ClientKeyExchange differ from the response times of ciphertexts with correct PKCS#1 v1.5 padding. This issue may allow a remote attacker to perform a timing side-channel attack in the RSA-PSK key exchange, potentially leading to the leakage of sensitive data. CVE-2024-0553 is designated as an incomplete resolution for CVE-2023-5981.

---
- gnutls28 3.8.3-1 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1061046)
[bookworm] - gnutls28 3.7.9-2+deb12u2
[bullseye] - gnutls28 3.7.1-5+deb11u5
https://gitlab.com/gnutls/gnutls/-/issues/1522
https://gnutls.org/security-new.html#GNUTLS-SA-2024-01-14
https://gitlab.com/gnutls/gnutls/-/commit/40dbbd8de499668590e8af51a15799fbc430595e (3.8.3)
https://lists.gnupg.org/pipermail/gnutls-help/2024-January/004841.html
Issue exists because of incomplete fix for CVE-2023-5981

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2023-5981?s=debian&n=gnutls28&ns=debian&t=deb&osn=debian&osv=12&vr=%3C3.7.9-2%2Bdeb12u1"><img alt="medium : CVE--2023--5981" src="https://img.shields.io/badge/CVE--2023--5981-lightgrey?label=medium%20&labelColor=fbb552"/></a> 

<table>
<tr><td>Affected range</td><td><code><3.7.9-2+deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><code>3.7.9-2+deb12u1</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.155%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>53rd percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A vulnerability was found that the response times to malformed ciphertexts in RSA-PSK ClientKeyExchange differ from response times of ciphertexts with correct PKCS#1 v1.5 padding.

---
- gnutls28 3.8.2-1 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1056188)
[bookworm] - gnutls28 3.7.9-2+deb12u1
[bullseye] - gnutls28 3.7.1-5+deb11u4
https://gitlab.com/gnutls/gnutls/-/issues/1511
https://gnutls.org/security-new.html#GNUTLS-SA-2023-10-23
https://lists.gnupg.org/pipermail/gnutls-help/2023-November/004837.html
Fixed by: https://gitlab.com/gnutls/gnutls/-/commit/29d6298d0b04cfff970b993915db71ba3f580b6d (3.8.2)
Fixing this issue incompletely opens up CVE-2024-0553

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2024-28834?s=debian&n=gnutls28&ns=debian&t=deb&osn=debian&osv=12&vr=%3C3.7.9-2%2Bdeb12u3"><img alt="medium : CVE--2024--28834" src="https://img.shields.io/badge/CVE--2024--28834-lightgrey?label=medium%20&labelColor=fbb552"/></a> 

<table>
<tr><td>Affected range</td><td><code><3.7.9-2+deb12u3</code></td></tr>
<tr><td>Fixed version</td><td><code>3.7.9-2+deb12u3</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.044%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>16th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A flaw was found in GnuTLS. The Minerva attack is a cryptographic vulnerability that exploits deterministic behavior in systems like GnuTLS, leading to side-channel leaks. In specific scenarios, such as when using the GNUTLS_PRIVKEY_FLAG_REPRODUCIBLE flag, it can result in a noticeable step in nonce size from 513 to 512 bits, exposing a potential timing side-channel.

---
[experimental] - gnutls28 3.8.4-1
- gnutls28 3.8.4-2 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1067464)
[bookworm] - gnutls28 3.7.9-2+deb12u3
[buster] - gnutls28 <not-affected> (Vulnerable code not present)
https://gitlab.com/gnutls/gnutls/-/issues/1516
https://lists.gnupg.org/pipermail/gnutls-help/2024-March/004845.html
https://www.gnutls.org/security-new.html#GNUTLS-SA-2023-12-04
Fixed by: https://gitlab.com/gnutls/gnutls/-/commit/1c4701ffc342259fc5965d5a0de90d87f780e3e5 (3.8.4)
Introduced with: https://gitlab.com/gnutls/gnutls/-/merge_requests/1051 (gnutls_3_6_10)

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2024-12243?s=debian&n=gnutls28&ns=debian&t=deb&osn=debian&osv=12&vr=%3C3.7.9-2%2Bdeb12u4"><img alt="medium : CVE--2024--12243" src="https://img.shields.io/badge/CVE--2024--12243-lightgrey?label=medium%20&labelColor=fbb552"/></a> 

<table>
<tr><td>Affected range</td><td><code><3.7.9-2+deb12u4</code></td></tr>
<tr><td>Fixed version</td><td><code>3.7.9-2+deb12u4</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.045%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>18th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A flaw was found in GnuTLS, which relies on libtasn1 for ASN.1 data processing. Due to an inefficient algorithm in libtasn1, decoding certain DER-encoded certificate data can take excessive time, leading to increased resource consumption. This flaw allows a remote attacker to send a specially crafted certificate, causing GnuTLS to become unresponsive or slow, resulting in a denial-of-service condition.

---
[experimental] - gnutls28 3.8.9-1
- gnutls28 3.8.9-2
https://www.gnutls.org/security-new.html#GNUTLS-SA-2025-02-07
https://lists.gnupg.org/pipermail/gnutls-help/2025-February/004875.html
https://gitlab.com/gnutls/gnutls/-/issues/1553
Fixed by: https://gitlab.com/gnutls/gnutls/-/commit/4760bc63531e3f5039e70ede91a20e1194410892 (3.8.9)

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2024-28835?s=debian&n=gnutls28&ns=debian&t=deb&osn=debian&osv=12&vr=%3C3.7.9-2%2Bdeb12u3"><img alt="medium : CVE--2024--28835" src="https://img.shields.io/badge/CVE--2024--28835-lightgrey?label=medium%20&labelColor=fbb552"/></a> 

<table>
<tr><td>Affected range</td><td><code><3.7.9-2+deb12u3</code></td></tr>
<tr><td>Fixed version</td><td><code>3.7.9-2+deb12u3</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.044%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>13th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A flaw has been discovered in GnuTLS where an application crash can be induced when attempting to verify a specially crafted .pem bundle using the "certtool --verify-chain" command.

---
[experimental] - gnutls28 3.8.4-1
- gnutls28 3.8.4-2 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1067463)
[bookworm] - gnutls28 3.7.9-2+deb12u3
[buster] - gnutls28 <not-affected> (Vulnerable code not present)
https://bugzilla.redhat.com/show_bug.cgi?id=2269084
https://gitlab.com/gnutls/gnutls/-/issues/1525
https://gitlab.com/gnutls/gnutls/-/issues/1527
https://lists.gnupg.org/pipermail/gnutls-help/2024-March/004845.html
https://www.gnutls.org/security-new.html#GNUTLS-SA-2024-01-23
Fixed by: https://gitlab.com/gnutls/gnutls/-/commit/e369e67a62f44561d417cb233acc566cc696d82d (3.8.4)
Introduced with: https://gitlab.com/gnutls/gnutls/-/commit/d268f19510a95f92d11d8f8dc7d94fcae4d765cc (3.7.0)

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 2" src="https://img.shields.io/badge/H-2-e25d68"/> <img alt="medium: 2" src="https://img.shields.io/badge/M-2-fbb552"/> <img alt="low: 0" src="https://img.shields.io/badge/L-0-lightgrey"/> <!-- unspecified: 0 --><strong>libx11</strong> <code>2:1.8.4-2</code> (deb)</summary>

<small><code>pkg:deb/debian/libx11@2:1.8.4-2?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2023-43787?s=debian&n=libx11&ns=debian&t=deb&osn=debian&osv=12&vr=%3C2%3A1.8.4-2%2Bdeb12u2"><img alt="high : CVE--2023--43787" src="https://img.shields.io/badge/CVE--2023--43787-lightgrey?label=high%20&labelColor=e25d68"/></a> 

<table>
<tr><td>Affected range</td><td><code><2:1.8.4-2+deb12u2</code></td></tr>
<tr><td>Fixed version</td><td><code>2:1.8.4-2+deb12u2</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.042%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>5th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A vulnerability was found in libX11 due to an integer overflow within the XCreateImage() function. This flaw allows a local user to trigger an integer overflow and execute arbitrary code with elevated privileges.

---
- libx11 2:1.8.7-1
https://www.openwall.com/lists/oss-security/2023/10/03/1
Fixed by: https://gitlab.freedesktop.org/xorg/lib/libx11/-/commit/7916869d16bdd115ac5be30a67c3749907aea6a0
Hardening: https://gitlab.freedesktop.org/xorg/lib/libxpm/-/commit/91f887b41bf75648df725a4ed3be036da02e911e
https://jfrog.com/blog/xorg-libx11-vulns-cve-2023-43786-cve-2023-43787-part-one/
https://jfrog.com/blog/xorg-libx11-vulns-cve-2023-43786-cve-2023-43787-part-two/

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2023-3138?s=debian&n=libx11&ns=debian&t=deb&osn=debian&osv=12&vr=%3C2%3A1.8.4-2%2Bdeb12u1"><img alt="high : CVE--2023--3138" src="https://img.shields.io/badge/CVE--2023--3138-lightgrey?label=high%20&labelColor=e25d68"/></a> 

<table>
<tr><td>Affected range</td><td><code><2:1.8.4-2+deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><code>2:1.8.4-2+deb12u1</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.159%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>54th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A vulnerability was found in libX11. The security flaw occurs because the functions in src/InitExt.c in libX11 do not check that the values provided for the Request, Event, or Error IDs are within the bounds of the arrays that those functions write to, using those IDs as array indexes. They trust that they were called with values provided by an Xserver adhering to the bounds specified in the X11 protocol, as all X servers provided by X.Org do. As the protocol only specifies a single byte for these values, an out-of-bounds value provided by a malicious server (or a malicious proxy-in-the-middle) can only overwrite other portions of the Display structure and not write outside the bounds of the Display structure itself, possibly causing the client to crash with this memory corruption.

---
- libx11 2:1.8.6-1 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1038133)
https://www.openwall.com/lists/oss-security/2023/06/15/2
https://gitlab.freedesktop.org/xorg/lib/libx11/-/commit/304a654a0d57bf0f00d8998185f0360332cfa36c

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2023-43785?s=debian&n=libx11&ns=debian&t=deb&osn=debian&osv=12&vr=%3C2%3A1.8.4-2%2Bdeb12u2"><img alt="medium : CVE--2023--43785" src="https://img.shields.io/badge/CVE--2023--43785-lightgrey?label=medium%20&labelColor=fbb552"/></a> 

<table>
<tr><td>Affected range</td><td><code><2:1.8.4-2+deb12u2</code></td></tr>
<tr><td>Fixed version</td><td><code>2:1.8.4-2+deb12u2</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.042%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>5th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A vulnerability was found in libX11 due to a boundary condition within the _XkbReadKeySyms() function. This flaw allows a local user to trigger an out-of-bounds read error and read the contents of memory on the system.

---
- libx11 2:1.8.7-1
https://www.openwall.com/lists/oss-security/2023/10/03/1
Fixed by: https://gitlab.freedesktop.org/xorg/lib/libx11/-/commit/6858d468d9ca55fb4c5fd70b223dbc78a3358a7f

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2023-43786?s=debian&n=libx11&ns=debian&t=deb&osn=debian&osv=12&vr=%3C2%3A1.8.4-2%2Bdeb12u2"><img alt="medium : CVE--2023--43786" src="https://img.shields.io/badge/CVE--2023--43786-lightgrey?label=medium%20&labelColor=fbb552"/></a> 

<table>
<tr><td>Affected range</td><td><code><2:1.8.4-2+deb12u2</code></td></tr>
<tr><td>Fixed version</td><td><code>2:1.8.4-2+deb12u2</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.042%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>5th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A vulnerability was found in libX11 due to an infinite loop within the PutSubImage() function. This flaw allows a local user to consume all available system resources and cause a denial of service condition.

---
- libx11 2:1.8.7-1
https://www.openwall.com/lists/oss-security/2023/10/03/1
Fixed by: https://gitlab.freedesktop.org/xorg/lib/libx11/-/commit/204c3393c4c90a29ed6bef64e43849536e863a86
Hardening: https://gitlab.freedesktop.org/xorg/lib/libx11/-/commit/73a37d5f2fcadd6540159b432a70d80f442ddf4a
Hardening: https://gitlab.freedesktop.org/xorg/lib/libx11/-/commit/b4031fc023816aca07fbd592ed97010b9b48784b
Hardening: https://gitlab.freedesktop.org/xorg/lib/libxpm/-/commit/84fb14574c039f19ad7face87eb9acc31a50701c
https://jfrog.com/blog/xorg-libx11-vulns-cve-2023-43786-cve-2023-43787-part-one/
https://jfrog.com/blog/xorg-libx11-vulns-cve-2023-43786-cve-2023-43787-part-two/

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 1" src="https://img.shields.io/badge/H-1-e25d68"/> <img alt="medium: 7" src="https://img.shields.io/badge/M-7-fbb552"/> <img alt="low: 0" src="https://img.shields.io/badge/L-0-lightgrey"/> <!-- unspecified: 0 --><strong>imagemagick</strong> <code>8:6.9.11.60+dfsg-1.6</code> (deb)</summary>

<small><code>pkg:deb/debian/imagemagick@8:6.9.11.60%2Bdfsg-1.6?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2021-3610?s=debian&n=imagemagick&ns=debian&t=deb&osn=debian&osv=12&vr=%3C8%3A6.9.11.60%2Bdfsg-1.6%2Bdeb12u1"><img alt="high : CVE--2021--3610" src="https://img.shields.io/badge/CVE--2021--3610-lightgrey?label=high%20&labelColor=e25d68"/></a> 

<table>
<tr><td>Affected range</td><td><code><8:6.9.11.60+dfsg-1.6+deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><code>8:6.9.11.60+dfsg-1.6+deb12u1</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.151%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>52nd percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A heap-based buffer overflow vulnerability was found in ImageMagick in versions prior to 7.0.11-14 in ReadTIFFImage() in coders/tiff.c. This issue is due to an incorrect setting of the pixel array size, which can lead to a crash and segmentation fault.

---
[experimental] - imagemagick 8:6.9.12.20+dfsg1-1
- imagemagick 8:6.9.12.98+dfsg1-2 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1037090)
[buster] - imagemagick <not-affected> (Vulnerable code introduced later)
https://github.com/ImageMagick/ImageMagick/commit/930ff0d1a9bc42925a7856e9ea53f5fc9f318bf3
ImageMagick6 prerequisite for <= 6.9.10-92: https://github.com/ImageMagick/ImageMagick6/commit/2d96228eec9fbea62ddb6c1450fa8d43e2c6b68a
ImageMagick6 prerequisite for <= 6.9.11-10: https://github.com/ImageMagick/ImageMagick6/commit/7374894385161859ffbb84e280fcc89e7ae257e4
ImageMagick6 prerequisite for <= 6.9.11-54: https://github.com/ImageMagick/ImageMagick6/commit/cdb67005376bcc8cbb0b743fb22787794cd30ebc
ImageMagick6 [1/2]: https://github.com/ImageMagick/ImageMagick6/commit/b307bcadcdf6ea6819951ac1786b7904f27b25c6 (6.9.12-14)
ImageMagick6 [2/2]: https://github.com/ImageMagick/ImageMagick6/commit/c75ae771a00c38b757c5ef4b424b51e761b02552 (6.9.12-14)
Introduced by (Support 32-bit tiles TIFF images): https://github.com/ImageMagick/ImageMagick6/commit/b874d50070557eb98bdc6a3095ef4769af583dd2 (6.9.10-88)

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2023-5341?s=debian&n=imagemagick&ns=debian&t=deb&osn=debian&osv=12&vr=%3C8%3A6.9.11.60%2Bdfsg-1.6%2Bdeb12u1"><img alt="medium : CVE--2023--5341" src="https://img.shields.io/badge/CVE--2023--5341-lightgrey?label=medium%20&labelColor=fbb552"/></a> 

<table>
<tr><td>Affected range</td><td><code><8:6.9.11.60+dfsg-1.6+deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><code>8:6.9.11.60+dfsg-1.6+deb12u1</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.060%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>28th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A heap use-after-free flaw was found in coders/bmp.c in ImageMagick.

---
- imagemagick 8:6.9.12.98+dfsg1-2
https://github.com/ImageMagick/ImageMagick/commit/aa673b2e4defc7cad5bec16c4fc8324f71e531f1 (7.1.1-19)
https://github.com/ImageMagick/ImageMagick6/commit/405684654eb9b43424c3c0276ea343681021d9e0 (6.9.12-97)

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2023-3428?s=debian&n=imagemagick&ns=debian&t=deb&osn=debian&osv=12&vr=%3C8%3A6.9.11.60%2Bdfsg-1.6%2Bdeb12u1"><img alt="medium : CVE--2023--3428" src="https://img.shields.io/badge/CVE--2023--3428-lightgrey?label=medium%20&labelColor=fbb552"/></a> 

<table>
<tr><td>Affected range</td><td><code><8:6.9.11.60+dfsg-1.6+deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><code>8:6.9.11.60+dfsg-1.6+deb12u1</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.049%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>21st percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A heap-based buffer overflow vulnerability was found  in coders/tiff.c in ImageMagick. This issue may allow a local attacker to trick the user into opening a specially crafted file, resulting in an application crash and denial of service.

---
[experimental] - imagemagick 8:6.9.12.98+dfsg1-1
- imagemagick 8:6.9.12.98+dfsg1-2
[buster] - imagemagick <not-affected> (code is introduced later)
Fixed by: https://github.com/ImageMagick/ImageMagick/commit/a531d28e31309676ce8168c3b6dbbb5374b78790 (7.1.1-13)
Prerequisite: https://github.com/ImageMagick/ImageMagick6/commit/2b4eabb9d09b278f16727c635e928bd951c58773 (6.9.12-55)
Fixed by: https://github.com/ImageMagick/ImageMagick6/commit/0d00400727170b0540a355a1bc52787bc7bcdea5 (6.9.12-91)

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2023-34151?s=debian&n=imagemagick&ns=debian&t=deb&osn=debian&osv=12&vr=%3C8%3A6.9.11.60%2Bdfsg-1.6%2Bdeb12u1"><img alt="medium : CVE--2023--34151" src="https://img.shields.io/badge/CVE--2023--34151-lightgrey?label=medium%20&labelColor=fbb552"/></a> 

<table>
<tr><td>Affected range</td><td><code><8:6.9.11.60+dfsg-1.6+deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><code>8:6.9.11.60+dfsg-1.6+deb12u1</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.072%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>34th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A vulnerability was found in ImageMagick. This security flaw ouccers as an undefined behaviors of casting double to size_t in svg, mvg and other coders (recurring bugs of CVE-2022-32546).

---
- imagemagick 8:6.9.12.98+dfsg1-2 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1036999)
https://github.com/ImageMagick/ImageMagick/issues/6341
ImageMagick: https://github.com/ImageMagick/ImageMagick/commit/3d6d98d8a2be30d74172ab43b5b8e874d2deb158 (7.1.1-10)
Vulnerability was incomplete and fixed across multiple version by upstream
[1/9] https://github.com/ImageMagick/ImageMagick6/commit/be15ac962dea19536be1009d157639030fc42be9
[2/9] https://github.com/ImageMagick/ImageMagick6/commit/8b7b17c8fef72dab479e6ca676676d8c5e395dd6
[3/9] https://github.com/ImageMagick/ImageMagick6/commit/c5a9368d871943eceafce143bb87612b2a9623b2
[4/9] https://github.com/ImageMagick/ImageMagick6/commit/c5a9368d871943eceafce143bb87612b2a9623b2
[5/9] https://github.com/ImageMagick/ImageMagick6/commit/75ebd9975f6ba8106ec15a6b3e6ba95f4c14e117
[6/9] https://github.com/ImageMagick/ImageMagick6/commit/b72508c8fce196cd031856574c202490be830649
[7/9] https://github.com/ImageMagick/ImageMagick6/commit/88789966667b748f14a904f8c9122274810e8a3e
[8/9] https://github.com/ImageMagick/ImageMagick6/commit/bc5ac19bd93895e5c6158aad0d8e49a0c50b0ebb
[9/9] https://github.com/ImageMagick/ImageMagick6/commit/3252d4771ff1142888ba83c439588969fcea98e4

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2023-1906?s=debian&n=imagemagick&ns=debian&t=deb&osn=debian&osv=12&vr=%3C8%3A6.9.11.60%2Bdfsg-1.6%2Bdeb12u1"><img alt="medium : CVE--2023--1906" src="https://img.shields.io/badge/CVE--2023--1906-lightgrey?label=medium%20&labelColor=fbb552"/></a> 

<table>
<tr><td>Affected range</td><td><code><8:6.9.11.60+dfsg-1.6+deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><code>8:6.9.11.60+dfsg-1.6+deb12u1</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.112%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>46th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A heap-based buffer overflow issue was discovered in ImageMagick's ImportMultiSpectralQuantum() function in MagickCore/quantum-import.c. An attacker could pass specially crafted file to convert, triggering an out-of-bounds read error, allowing an application to crash, resulting in a denial of service.

---
- imagemagick 8:6.9.12.98+dfsg1-2 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1034373)
[buster] - imagemagick <not-affected> (Vulnerable code introduced later)
https://github.com/ImageMagick/ImageMagick/security/advisories/GHSA-35q2-86c7-9247
https://github.com/ImageMagick/ImageMagick6/commit/e30c693b37c3b41723f1469d1226a2c814ca443d (ImageMagick 6.9.12-84)

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2023-1289?s=debian&n=imagemagick&ns=debian&t=deb&osn=debian&osv=12&vr=%3C8%3A6.9.11.60%2Bdfsg-1.6%2Bdeb12u1"><img alt="medium : CVE--2023--1289" src="https://img.shields.io/badge/CVE--2023--1289-lightgrey?label=medium%20&labelColor=fbb552"/></a> 

<table>
<tr><td>Affected range</td><td><code><8:6.9.11.60+dfsg-1.6+deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><code>8:6.9.11.60+dfsg-1.6+deb12u1</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.162%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>54th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A vulnerability was discovered in ImageMagick where a specially created SVG file loads itself and causes a segmentation fault. This flaw allows a remote attacker to pass a specially crafted SVG file that leads to a segmentation fault, generating many trash files in "/tmp," resulting in a denial of service. When ImageMagick crashes, it generates a lot of trash files. These trash files can be large if the SVG file contains many render actions. In a denial of service attack, if a remote attacker uploads an SVG file of size t, ImageMagick generates files of size 103*t. If an attacker uploads a 100M SVG, the server will generate about 10G.

---
- imagemagick 8:6.9.12.98+dfsg1-2
https://github.com/ImageMagick/ImageMagick/security/advisories/GHSA-j96m-mjp6-99xr
https://github.com/ImageMagick/ImageMagick/commit/c5b23cbf2119540725e6dc81f4deb25798ead6a4 (7.1.1-0)
Multiple regression or incomplete fixes were identified, and a few upstream version are incomplete
[1/9] https://github.com/ImageMagick/ImageMagick6/commit/e8c0090c6d2df7b1553053dca2008e96724204bf
[2/9] https://github.com/ImageMagick/ImageMagick6/commit/706d381b7eb79927d328c96f7b7faab5dc109368
[3/9] https://github.com/ImageMagick/ImageMagick6/commit/ddc718eaa93767ceae286e171296b5fbb0bbd812
[4/9] https://github.com/ImageMagick/ImageMagick6/commit/1485a4c2cba8ca32981016fa25e7a15ef84f06f6
[5/9] https://github.com/ImageMagick/ImageMagick6/commit/84ec30550c3146f525383f18a786a6bbd5028a93
[6/9] https://github.com/ImageMagick/ImageMagick6/commit/4dd4d0df449acb13fb859041b4996af58243e352
[7/9] https://github.com/ImageMagick/ImageMagick6/commit/f4529c0dcf3a8f96c438086b28fbef8338cda0b1
[8/9] https://github.com/ImageMagick/ImageMagick6/commit/75aac79108af0c0b0d7fc88b1f09c340b0d62c85
[9/9] https://github.com/ImageMagick/ImageMagick6/commit/060660bf45e0771cf0431e5c2749aa51fabf23f8

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2022-3213?s=debian&n=imagemagick&ns=debian&t=deb&osn=debian&osv=12&vr=%3C8%3A6.9.11.60%2Bdfsg-1.6%2Bdeb12u1"><img alt="medium : CVE--2022--3213" src="https://img.shields.io/badge/CVE--2022--3213-lightgrey?label=medium%20&labelColor=fbb552"/></a> 

<table>
<tr><td>Affected range</td><td><code><8:6.9.11.60+dfsg-1.6+deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><code>8:6.9.11.60+dfsg-1.6+deb12u1</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.067%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>32nd percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A heap buffer overflow issue was found in ImageMagick. When an application processes a malformed TIFF file, it could lead to undefined behavior or a crash causing a denial of service.

---
- imagemagick 8:6.9.12.98+dfsg1-2 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1021141)
[bookworm] - imagemagick 8:6.9.11.60+dfsg-1.6+deb12u1
[bullseye] - imagemagick 8:6.9.11.60+dfsg-1.3+deb11u3
[buster] - imagemagick <not-affected> (Vulnerable code was introduced later)
https://bugzilla.redhat.com/show_bug.cgi?id=2126824
https://github.com/ImageMagick/ImageMagick/commit/30ccf9a0da1f47161b5935a95be854fe84e6c2a2
https://github.com/ImageMagick/ImageMagick6/commit/1aea203eb36409ce6903b9e41fe7cb70030e8750 (6.9.12-62)

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2022-1115?s=debian&n=imagemagick&ns=debian&t=deb&osn=debian&osv=12&vr=%3C8%3A6.9.11.60%2Bdfsg-1.6%2Bdeb12u1"><img alt="medium : CVE--2022--1115" src="https://img.shields.io/badge/CVE--2022--1115-lightgrey?label=medium%20&labelColor=fbb552"/></a> 

<table>
<tr><td>Affected range</td><td><code><8:6.9.11.60+dfsg-1.6+deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><code>8:6.9.11.60+dfsg-1.6+deb12u1</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.145%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>52nd percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A heap-buffer-overflow flaw was found in ImageMagick’s PushShortPixel() function of quantum-private.h file. This vulnerability is triggered when an attacker passes a specially crafted TIFF image file to ImageMagick for conversion, potentially leading to a denial of service.

---
- imagemagick 8:6.9.12.98+dfsg1-2 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1013282)
[buster] - imagemagick <not-affected> (code is introduced later)
[stretch] - imagemagick <not-affected> (code is introduced later)
https://github.com/ImageMagick/ImageMagick/issues/4974
Fixed by: https://github.com/ImageMagick/ImageMagick6/commit/1f860f52bd8d58737ad883072203391096b30b51 (6.9.12-44)
Introduced by (Support 32-bit tiles TIFF images): https://github.com/ImageMagick/ImageMagick6/commit/b874d50070557eb98bdc6a3095ef476 (6.9.10-88)

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 1" src="https://img.shields.io/badge/H-1-e25d68"/> <img alt="medium: 3" src="https://img.shields.io/badge/M-3-fbb552"/> <img alt="low: 12" src="https://img.shields.io/badge/L-12-fce1a9"/> <!-- unspecified: 0 --><strong>openjpeg2</strong> <code>2.5.0-2</code> (deb)</summary>

<small><code>pkg:deb/debian/openjpeg2@2.5.0-2?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2021-3575?s=debian&n=openjpeg2&ns=debian&t=deb&osn=debian&osv=12&vr=%3C2.5.0-2%2Bdeb12u1"><img alt="high : CVE--2021--3575" src="https://img.shields.io/badge/CVE--2021--3575-lightgrey?label=high%20&labelColor=e25d68"/></a> 

<table>
<tr><td>Affected range</td><td><code><2.5.0-2+deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><code>2.5.0-2+deb12u1</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.417%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>74th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A heap-based buffer overflow was found in openjpeg in color.c:379:42 in sycc420_to_rgb when decompressing a crafted .j2k file. An attacker could use this to execute arbitrary code with the permissions of the application compiled against openjpeg.

---
[experimental] - openjpeg2 2.5.3-1~exp1
- openjpeg2 2.5.3-1 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=989775)
[bullseye] - openjpeg2 <no-dsa> (Minor issue)
[buster] - openjpeg2 <no-dsa> (Minor issue)
[stretch] - openjpeg2 <no-dsa> (Minor issue)
https://github.com/uclouvain/openjpeg/issues/1347
https://github.com/uclouvain/openjpeg/pull/1509
Fixed by: https://github.com/uclouvain/openjpeg/commit/7bd884f8750892de4f50bf4642fcfbe7011c6bdf (v2.5.1)

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2024-56827?s=debian&n=openjpeg2&ns=debian&t=deb&osn=debian&osv=12&vr=%3C2.5.0-2%2Bdeb12u1"><img alt="medium : CVE--2024--56827" src="https://img.shields.io/badge/CVE--2024--56827-lightgrey?label=medium%20&labelColor=fbb552"/></a> 

<table>
<tr><td>Affected range</td><td><code><2.5.0-2+deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><code>2.5.0-2+deb12u1</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.042%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>5th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A flaw was found in the OpenJPEG project. A heap buffer overflow condition may be triggered when certain options are specified while using the opj_decompress utility.  This can lead to an application crash or other undefined behavior.

---
[experimental] - openjpeg2 2.5.3-1~exp1
- openjpeg2 2.5.3-1 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1092676)
https://bugzilla.redhat.com/show_bug.cgi?id=2335174
https://github.com/uclouvain/openjpeg/issues/1564
https://github.com/uclouvain/openjpeg/commit/e492644fbded4c820ca55b5e50e598d346e850e8 (v2.5.3)

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2024-56826?s=debian&n=openjpeg2&ns=debian&t=deb&osn=debian&osv=12&vr=%3C2.5.0-2%2Bdeb12u1"><img alt="medium : CVE--2024--56826" src="https://img.shields.io/badge/CVE--2024--56826-lightgrey?label=medium%20&labelColor=fbb552"/></a> 

<table>
<tr><td>Affected range</td><td><code><2.5.0-2+deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><code>2.5.0-2+deb12u1</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.042%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>5th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A flaw was found in the OpenJPEG project. A heap buffer overflow condition may be triggered when certain options are specified while using the opj_decompress utility.  This can lead to an application crash or other undefined behavior.

---
[experimental] - openjpeg2 2.5.3-1~exp1
- openjpeg2 2.5.3-1 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1092675)
https://bugzilla.redhat.com/show_bug.cgi?id=2335172
https://github.com/uclouvain/openjpeg/issues/1563
https://github.com/uclouvain/openjpeg/commit/98592ee6d6904f1b48e8207238779b89a63befa2 (v2.5.3)

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2023-39327?s=debian&n=openjpeg2&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.5.0-2"><img alt="medium : CVE--2023--39327" src="https://img.shields.io/badge/CVE--2023--39327-lightgrey?label=medium%20&labelColor=fbb552"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.5.0-2</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.043%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>12th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A flaw was found in OpenJPEG. Maliciously constructed pictures can cause the program to enter a large loop and continuously print warning messages on the terminal.

---
- openjpeg2 <unfixed> (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1081908)
[bullseye] - openjpeg2 <no-dsa> (Minor issue)
https://github.com/uclouvain/openjpeg/issues/1472
Partial mitigation of CVE-2023-39327 (in absence of EPH):
https://github.com/uclouvain/openjpeg/commit/822562d689f491ae5d012627ba00ac235d399b9e (v2.5.3)

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2018-20846?s=debian&n=openjpeg2&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.5.0-2"><img alt="low : CVE--2018--20846" src="https://img.shields.io/badge/CVE--2018--20846-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.5.0-2</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.110%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>46th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

Out-of-bounds accesses in the functions pi_next_lrcp, pi_next_rlcp, pi_next_rpcl, pi_next_pcrl, pi_next_rpcl, and pi_next_cprl in openmj2/pi.c in OpenJPEG through 2.3.0 allow remote attackers to cause a denial of service (application crash).

---
- openjpeg2 <unfixed> (unimportant)
https://github.com/uclouvain/openjpeg/commit/c277159986c80142180fbe5efb256bbf3bdf3edc
Debian binary packages built with BUILD_MJ2:BOOL=OFF

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2018-16376?s=debian&n=openjpeg2&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.5.0-2"><img alt="low : CVE--2018--16376" src="https://img.shields.io/badge/CVE--2018--16376-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.5.0-2</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>1.048%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>84th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

An issue was discovered in OpenJPEG 2.3.0. A heap-based buffer overflow was discovered in the function t2_encode_packet in lib/openmj2/t2.c. The vulnerability causes an out-of-bounds write, which may lead to remote denial of service or possibly unspecified other impact.

---
- openjpeg2 <unfixed> (unimportant)
https://github.com/uclouvain/openjpeg/issues/1127
We build with -DBUILD_MJ2:BOOL=OFF

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2018-16375?s=debian&n=openjpeg2&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.5.0-2"><img alt="low : CVE--2018--16375" src="https://img.shields.io/badge/CVE--2018--16375-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.5.0-2</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.301%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>70th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

An issue was discovered in OpenJPEG 2.3.0. Missing checks for header_info.height and header_info.width in the function pnmtoimage in bin/jpwl/convert.c can lead to a heap-based buffer overflow.

---
- openjpeg2 <unfixed> (unimportant)
https://github.com/uclouvain/openjpeg/issues/1126
We build with -DBUILD_JPWL:BOOL=OFF

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2017-17479?s=debian&n=openjpeg2&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.5.0-2"><img alt="low : CVE--2017--17479" src="https://img.shields.io/badge/CVE--2017--17479-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.5.0-2</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>2.291%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>90th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

In OpenJPEG 2.3.0, a stack-based buffer overflow was discovered in the pgxtoimage function in jpwl/convert.c. The vulnerability causes an out-of-bounds write, which may lead to remote denial of service or possibly remote code execution.

---
- openjpeg2 <unfixed> (unimportant)
https://github.com/uclouvain/openjpeg/issues/1044
Debian packaging does not build JPWL, has BUILD_JPWL:BOOL=OFF

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2016-9581?s=debian&n=openjpeg2&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.5.0-2"><img alt="low : CVE--2016--9581" src="https://img.shields.io/badge/CVE--2016--9581-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.5.0-2</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.384%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>73rd percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

An infinite loop vulnerability in tiftoimage that results in heap buffer overflow in convert_32s_C1P1 was found in openjpeg 2.1.2.

---
- openjpeg2 <unfixed> (unimportant)
https://github.com/uclouvain/openjpeg/issues/872
Fixed by: https://github.com/szukw000/openjpeg/commit/cadff5fb6e73398de26a92e96d3d7cac893af255
not built into the binary packages

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2016-9580?s=debian&n=openjpeg2&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.5.0-2"><img alt="low : CVE--2016--9580" src="https://img.shields.io/badge/CVE--2016--9580-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.5.0-2</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.266%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>66th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

An integer overflow vulnerability was found in tiftoimage function in openjpeg 2.1.2, resulting in heap buffer overflow.

---
- openjpeg2 <unfixed> (unimportant)
https://github.com/uclouvain/openjpeg/issues/871
Fixed by: https://github.com/szukw000/openjpeg/commit/cadff5fb6e73398de26a92e96d3d7cac893af255
not built into the binary packages

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2016-9117?s=debian&n=openjpeg2&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.5.0-2"><img alt="low : CVE--2016--9117" src="https://img.shields.io/badge/CVE--2016--9117-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.5.0-2</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.095%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>42nd percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

NULL Pointer Access in function imagetopnm of convert.c(jp2):1289 in OpenJPEG 2.1.2. Impact is Denial of Service. Someone must open a crafted j2k file.

---
- openjpeg2 <unfixed> (unimportant; bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=844556)
https://github.com/uclouvain/openjpeg/issues/860
No code injection, function only exposed in the CLI tool

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2016-9116?s=debian&n=openjpeg2&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.5.0-2"><img alt="low : CVE--2016--9116" src="https://img.shields.io/badge/CVE--2016--9116-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.5.0-2</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.095%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>42nd percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

NULL Pointer Access in function imagetopnm of convert.c:2226(jp2) in OpenJPEG 2.1.2. Impact is Denial of Service. Someone must open a crafted j2k file.

---
- openjpeg2 <unfixed> (unimportant; bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=844555)
https://github.com/uclouvain/openjpeg/issues/859
No code injection, function only exposed in the CLI tool

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2016-9115?s=debian&n=openjpeg2&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.5.0-2"><img alt="low : CVE--2016--9115" src="https://img.shields.io/badge/CVE--2016--9115-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.5.0-2</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.136%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>50th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

Heap Buffer Over-read in function imagetotga of convert.c(jp2):942 in OpenJPEG 2.1.2. Impact is Denial of Service. Someone must open a crafted j2k file.

---
- openjpeg2 <unfixed> (unimportant; bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=844554)
https://github.com/uclouvain/openjpeg/issues/858
No code injection, function only exposed in the CLI tool

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2016-9114?s=debian&n=openjpeg2&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.5.0-2"><img alt="low : CVE--2016--9114" src="https://img.shields.io/badge/CVE--2016--9114-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.5.0-2</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.332%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>71st percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

There is a NULL Pointer Access in function imagetopnm of convert.c:1943(jp2) of OpenJPEG 2.1.2. image->comps[compno].data is not assigned a value after initialization(NULL). Impact is Denial of Service.

---
- openjpeg2 <unfixed> (unimportant; bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=844553)
https://github.com/uclouvain/openjpeg/issues/857
No code injection, function only exposed in the CLI tool

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2016-9113?s=debian&n=openjpeg2&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.5.0-2"><img alt="low : CVE--2016--9113" src="https://img.shields.io/badge/CVE--2016--9113-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.5.0-2</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.332%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>71st percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

There is a NULL pointer dereference in function imagetobmp of convertbmp.c:980 of OpenJPEG 2.1.2. image->comps[0].data is not assigned a value after initialization(NULL). Impact is Denial of Service.

---
- openjpeg2 <unfixed> (unimportant; bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=844552)
https://github.com/uclouvain/openjpeg/issues/856
No code injection, function only exposed in the CLI tool

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2016-10505?s=debian&n=openjpeg2&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.5.0-2"><img alt="low : CVE--2016--10505" src="https://img.shields.io/badge/CVE--2016--10505-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.5.0-2</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.762%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>81st percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

NULL pointer dereference vulnerabilities in the imagetopnm function in convert.c, sycc444_to_rgb function in color.c, color_esycc_to_rgb function in color.c, and sycc422_to_rgb function in color.c in OpenJPEG before 2.2.0 allow remote attackers to cause a denial of service (application crash) via crafted j2k files.

---
- openjpeg2 <unfixed> (unimportant)
https://github.com/uclouvain/openjpeg/issues/776
https://github.com/uclouvain/openjpeg/issues/784
https://github.com/uclouvain/openjpeg/issues/785
https://github.com/uclouvain/openjpeg/issues/792

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 1" src="https://img.shields.io/badge/H-1-e25d68"/> <img alt="medium: 1" src="https://img.shields.io/badge/M-1-fbb552"/> <img alt="low: 1" src="https://img.shields.io/badge/L-1-fce1a9"/> <!-- unspecified: 0 --><strong>libheif</strong> <code>1.15.1-1</code> (deb)</summary>

<small><code>pkg:deb/debian/libheif@1.15.1-1?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2024-41311?s=debian&n=libheif&ns=debian&t=deb&osn=debian&osv=12&vr=%3C1.15.1-1%2Bdeb12u1"><img alt="high : CVE--2024--41311" src="https://img.shields.io/badge/CVE--2024--41311-lightgrey?label=high%20&labelColor=e25d68"/></a> 

<table>
<tr><td>Affected range</td><td><code><1.15.1-1+deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><code>1.15.1-1+deb12u1</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.045%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>18th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

In Libheif 1.17.6, insufficient checks in ImageOverlay::parse() decoding a heif file containing an overlay image with forged offsets can lead to an out-of-bounds read and write.

---
- libheif 1.18.1-1
https://github.com/strukturag/libheif/issues/1226
https://github.com/strukturag/libheif/pull/1227
https://github.com/strukturag/libheif/commit/a3ed1b1eb178c5d651d6ac619c8da3d71ac2be36 (v1.18.0)

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2023-29659?s=debian&n=libheif&ns=debian&t=deb&osn=debian&osv=12&vr=%3C1.15.1-1%2Bdeb12u1"><img alt="medium : CVE--2023--29659" src="https://img.shields.io/badge/CVE--2023--29659-lightgrey?label=medium%20&labelColor=fbb552"/></a> 

<table>
<tr><td>Affected range</td><td><code><1.15.1-1+deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><code>1.15.1-1+deb12u1</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.123%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>48th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A Segmentation fault caused by a floating point exception exists in libheif 1.15.1 using crafted heif images via the heif::Fraction::round() function in box.cc, which causes a denial of service.

---
- libheif 1.16.2-1 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1035607)
[buster] - libheif <no-dsa> (Minor issue)
https://github.com/strukturag/libheif/issues/794
https://github.com/strukturag/libheif/commit/e05e15b57a38ec411cb9acb38512a1c36ff62991 (v1.15.2)

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2023-49462?s=debian&n=libheif&ns=debian&t=deb&osn=debian&osv=12&vr=%3C1.15.1-1%2Bdeb12u1"><img alt="low : CVE--2023--49462" src="https://img.shields.io/badge/CVE--2023--49462-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code><1.15.1-1+deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><code>1.15.1-1+deb12u1</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.189%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>57th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

libheif v1.17.5 was discovered to contain a segmentation violation via the component /libheif/exif.cc.

---
- libheif 1.17.6-1 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1059151)
[bullseye] - libheif <not-affected> (Vulnerable code not present)
[buster] - libheif <not-affected> (Vulnerable code not present)
https://github.com/strukturag/libheif/issues/1043
https://github.com/strukturag/libheif/commit/730a9d80bea3434f75c79e721878cc67f3889969 (v1.17.6)

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 1" src="https://img.shields.io/badge/H-1-e25d68"/> <img alt="medium: 1" src="https://img.shields.io/badge/M-1-fbb552"/> <img alt="low: 0" src="https://img.shields.io/badge/L-0-lightgrey"/> <img alt="unspecified: 1" src="https://img.shields.io/badge/U-1-lightgrey"/><strong>systemd</strong> <code>252.6-1</code> (deb)</summary>

<small><code>pkg:deb/debian/systemd@252.6-1?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2023-50387?s=debian&n=systemd&ns=debian&t=deb&osn=debian&osv=12&vr=%3C252.23-1%7Edeb12u1"><img alt="high : CVE--2023--50387" src="https://img.shields.io/badge/CVE--2023--50387-lightgrey?label=high%20&labelColor=e25d68"/></a> 

<table>
<tr><td>Affected range</td><td><code><252.23-1~deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><code>252.23-1~deb12u1</code></td></tr>
<tr><td>EPSS Score</td><td><code>7.326%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>94th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

Certain DNSSEC aspects of the DNS protocol (in RFC 4033, 4034, 4035, 6840, and related RFCs) allow remote attackers to cause a denial of service (CPU consumption) via one or more DNSSEC responses, aka the "KeyTrap" issue. One of the concerns is that, when there is a zone with many DNSKEY and RRSIG records, the protocol specification implies that an algorithm must evaluate all combinations of DNSKEY and RRSIG records.

---
- bind9 1:9.19.21-1
- dnsmasq 2.90-1
[bookworm] - dnsmasq 2.90-4~deb12u1
- knot-resolver 5.7.1-1
[bullseye] - knot-resolver <ignored> (Too intrusive to backport, if DNSSEC is used Bookworm can be used)
[buster] - knot-resolver <ignored> (Too intrusive to backport)
- pdns-recursor 4.9.3-1 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1063852)
[bullseye] - pdns-recursor <end-of-life> (No longer supported with security updates in Bullseye)
- unbound 1.19.1-1 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1063845)
- systemd 255.4-1
[bookworm] - systemd 252.23-1~deb12u1
[buster] - systemd <no-dsa> (DNSSEC is disabled by default in systemd-resolved; can be fixed via point release)
- dnsjava 3.6.2-1 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1077750)
[bookworm] - dnsjava <no-dsa> (Minor issue)
[bullseye] - dnsjava <no-dsa> (Minor issue)
https://kb.isc.org/docs/cve-2023-50387
https://gitlab.isc.org/isc-projects/bind9/-/commit/c12608ca934c0433d280e65fe6c631013e200cfe (v9.16.48)
https://gitlab.isc.org/isc-projects/bind9/-/commit/751b7cc4750ede6d8c5232751d60aad8ad84aa67 (v9.16.48)
https://gitlab.isc.org/isc-projects/bind9/-/commit/6a65a425283d70da86bf732449acd6d7c8dec718 (v9.16.48)
https://gitlab.isc.org/isc-projects/bind9/-/commit/3d206e918b3efbc20074629ad9d99095fbd2e5fd (v9.16.48)
https://gitlab.isc.org/isc-projects/bind9/-/commit/a520fbc0470a0d6b72db6aa0b8deda8798551614 (v9.16.48)
https://downloads.isc.org/isc/bind9/9.16.48/patches/0005-CVE-2023-50387-CVE-2023-50868.patch
https://lists.thekelleys.org.uk/pipermail/dnsmasq-discuss/2024q1/017430.html
https://www.knot-resolver.cz/2024-02-13-knot-resolver-5.7.1.html
https://github.com/CZ-NIC/knot-resolver/commit/7ddabe80fa05b76fc57b5a112a82a2c032032534
https://github.com/CZ-NIC/knot-resolver/commit/feb65eb97b93f0f024d70c7f5f6cbc6802ba02ec (v5.7.1)
https://github.com/CZ-NIC/knot-resolver/commit/cc5051b4441307d9b262fa382bc715391112ddbb (v5.7.1)
https://blog.powerdns.com/2024/02/13/powerdns-recursor-4-8-6-4-9-3-5-0-2-released
Fixed by: https://github.com/PowerDNS/pdns/pull/13781
https://nlnetlabs.nl/news/2024/Feb/13/unbound-1.19.1-released/
https://nlnetlabs.nl/downloads/unbound/CVE-2023-50387_CVE-2023-50868.txt
Fixed by: https://github.com/NLnetLabs/unbound/commit/882903f2fa800c4cb6f5e225b728e2887bb7b9ae (release-1.19.1)
https://github.com/systemd/systemd/issues/31413
https://github.com/systemd/systemd/commit/67d0ce8843d612a2245d0966197d4f528b911b66 (v256)
https://github.com/systemd/systemd/commit/eba291124bc11f03732d1fc468db3bfac069f9cb (v256)
https://github.com/systemd/systemd-stable/commit/1ebdb19ff194120109b08bbf888bdcc502f83211 (v255.4)
https://github.com/systemd/systemd-stable/commit/572692f0bdd6a3fabe3dd4a3e8e5565cc69b5e14 (v255.4)
https://github.com/systemd/systemd-stable/commit/2f5edffa8ffd5210165ebe7604f07d23f375fe9a (v254.10)
https://github.com/systemd/systemd-stable/commit/9899281c59a91f19c8b39362d203e997d2faf233 (v254.10)
https://github.com/systemd/systemd-stable/commit/7886eea2425fe7773cc012da0b2e266e33d4be12 (v253.17)
https://github.com/systemd/systemd-stable/commit/156e519d990a5662c719a1cbe80c6a02a2b9115f (v253.17)
https://github.com/systemd/systemd-stable/commit/7633d969f3422f9ad380a512987d398e54764817 (v252.23)
https://github.com/systemd/systemd-stable/commit/b43bcb51ebf9aea21b1e280e1872056994e3f53d (v252.23)
systemd: DNSSEC is default to off in systemd-resolved
https://github.com/advisories/GHSA-crjg-w57m-rqqf
https://github.com/dnsjava/dnsjava/commit/07ac36a11578cc1bce0cd8ddf2fe568f062aee78 (v3.6.0)
https://github.com/dnsjava/dnsjava/commit/3ddc45ce8cdb5c2274e10b7401416f497694e1cf (v3.6.0)

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2023-7008?s=debian&n=systemd&ns=debian&t=deb&osn=debian&osv=12&vr=%3C252.21-1%7Edeb12u1"><img alt="medium : CVE--2023--7008" src="https://img.shields.io/badge/CVE--2023--7008-lightgrey?label=medium%20&labelColor=fbb552"/></a> 

<table>
<tr><td>Affected range</td><td><code><252.21-1~deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><code>252.21-1~deb12u1</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.104%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>44th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A vulnerability was found in systemd-resolved. This issue may allow systemd-resolved to accept records of DNSSEC-signed domains even when they have no signature, allowing man-in-the-middles (or the upstream DNS resolver) to manipulate records.

---
- systemd 255.1-3 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1059278)
[bookworm] - systemd 252.21-1~deb12u1
[buster] - systemd <no-dsa> (Minor issue)
https://bugzilla.redhat.com/show_bug.cgi?id=2222672
https://github.com/systemd/systemd/issues/25676
systemd-resolved defaults to DNSSEC=no (disabled) everywhere, and is affected only
when manually enabled.
Introduced by: https://github.com/systemd/systemd/commit/105e151299dc1208855380be2b22d0db2d66ebc6 (v229)
Fixed by: https://github.com/systemd/systemd/commit/3b4cc1437b51fcc0b08da8cc3f5d1175eed25eb1 (v256)
Fixed by: https://github.com/systemd/systemd-stable/commit/6da5ca9dd69c0e3340d4439413718ad4963252de (v255.2)
Fixed by: https://github.com/systemd/systemd-stable/commit/029272750fe451aeaac87a8c783cfb067f001e16 (v254.8)
Fixed by: https://github.com/systemd/systemd-stable/commit/5c149c77cbf7b3743fa65ce7dc9d2b5a58351968 (v253.15)
Fixed by: https://github.com/systemd/systemd-stable/commit/bb78da7f955c0102047319c55fff9d853ab7c87a (v252.21)
Fixed by: https://github.com/systemd/systemd-stable/commit/f58fc88678b893162f2d6d4b2db094e7b1646386 (v251.20)
Fixed by: https://github.com/systemd/systemd-stable/commit/4ada1290584745ab6643eece9e1756a8c0e079ca (v250.14)
Fixed by: https://github.com/systemd/systemd-stable/commit/c8578cef7f0f1e8cb8193c29e5e77daf4e3a1c9f (v249.17)
Fixed by: https://github.com/systemd/systemd-stable/commit/3a409b210396c6a0bef621349f4caa3a865940f2 (v248.13)

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2023-50868?s=debian&n=systemd&ns=debian&t=deb&osn=debian&osv=12&vr=%3C252.23-1%7Edeb12u1"><img alt="unspecified : CVE--2023--50868" src="https://img.shields.io/badge/CVE--2023--50868-lightgrey?label=unspecified%20&labelColor=lightgrey"/></a> 

<table>
<tr><td>Affected range</td><td><code><252.23-1~deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><code>252.23-1~deb12u1</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.046%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>20th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

The Closest Encloser Proof aspect of the DNS protocol (in RFC 5155 when RFC 9276 guidance is skipped) allows remote attackers to cause a denial of service (CPU consumption for SHA-1 computations) via DNSSEC responses in a random subdomain attack, aka the "NSEC3" issue. The RFC 5155 specification implies that an algorithm must perform thousands of iterations of a hash function in certain situations.

---
- bind9 1:9.19.21-1
- dnsmasq 2.90-1
[bookworm] - dnsmasq 2.90-4~deb12u1
- knot-resolver 5.7.1-1
[bullseye] - knot-resolver <ignored> (Too intrusive to backport, if DNSSEC is used Bookworm can be used)
[buster] - knot-resolver <ignored> (Too intrusive to backport, if DNSSEC is used Bookworm can be used)
- pdns-recursor 4.9.3-1 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1063852)
[bullseye] - pdns-recursor <end-of-life> (No longer supported with security updates in Bullseye)
- unbound 1.19.1-1 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1063845)
- systemd 255.4-1
[bookworm] - systemd 252.23-1~deb12u1
[buster] - systemd <no-dsa> (DNSSEC is disabled by default in systemd-resolved; can be fixed via point release)
- dnsjava 3.6.2-1 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1077751)
[bookworm] - dnsjava <no-dsa> (Minor issue)
[bullseye] - dnsjava <no-dsa> (Minor issue)
https://kb.isc.org/docs/cve-2023-50868
https://downloads.isc.org/isc/bind9/9.16.48/patches/0005-CVE-2023-50387-CVE-2023-50868.patch
https://lists.thekelleys.org.uk/pipermail/dnsmasq-discuss/2024q1/017430.html
https://www.knot-resolver.cz/2024-02-13-knot-resolver-5.7.1.html
https://github.com/CZ-NIC/knot-resolver/commit/e966b7fdb167add0ec37c56a954c2d847f627985 (v5.7.1)
https://github.com/CZ-NIC/knot-resolver/commit/eccb8e278c1cde0548cc570eac619feaa290cede (v5.7.1)
https://github.com/CZ-NIC/knot-resolver/commit/b5051ac26f34358b40f9115f977fe1f54e8f581e (v5.7.1)
https://github.com/CZ-NIC/knot-resolver/commit/24699e9f206a8f957b516cad22a8e5790d226836 (v5.7.1)
https://github.com/CZ-NIC/knot-resolver/commit/a05cf1d379d1af0958587bd111f791b72f404364 (v5.7.1)
https://github.com/CZ-NIC/knot-resolver/commit/9b421cdf91f987e0254a06ff2c4e8fbf76dc2b58 (v5.7.1)
https://github.com/CZ-NIC/knot-resolver/commit/5e80624b18d40ae44be704751d3b22943edf287f
https://github.com/CZ-NIC/knot-resolver/commit/f9ba52e6f54bc1db122870df50cb364cb977436e (v5.7.1)
https://github.com/CZ-NIC/knot-resolver/commit/b044babbee358dc305d770a1dab3a877c49468a7 (v5.7.1)
https://blog.powerdns.com/2024/02/13/powerdns-recursor-4-8-6-4-9-3-5-0-2-released
Fixed by: https://github.com/PowerDNS/pdns/pull/13781
https://nlnetlabs.nl/news/2024/Feb/13/unbound-1.19.1-released/
https://nlnetlabs.nl/downloads/unbound/CVE-2023-50387_CVE-2023-50868.txt
Fixed by: https://github.com/NLnetLabs/unbound/commit/92f2a1ca690a44880f4c4fa70a4b5a4b029aaf1c (release-1.19.1)
https://github.com/systemd/systemd/issues/31413
https://github.com/systemd/systemd/commit/67d0ce8843d612a2245d0966197d4f528b911b66 (v256)
https://github.com/systemd/systemd/commit/eba291124bc11f03732d1fc468db3bfac069f9cb (v256)
https://github.com/systemd/systemd-stable/commit/1ebdb19ff194120109b08bbf888bdcc502f83211 (v255.4)
https://github.com/systemd/systemd-stable/commit/572692f0bdd6a3fabe3dd4a3e8e5565cc69b5e14 (v255.4)
https://github.com/systemd/systemd-stable/commit/2f5edffa8ffd5210165ebe7604f07d23f375fe9a (v254.10)
https://github.com/systemd/systemd-stable/commit/9899281c59a91f19c8b39362d203e997d2faf233 (v254.10)
https://github.com/systemd/systemd-stable/commit/7886eea2425fe7773cc012da0b2e266e33d4be12 (v253.17)
https://github.com/systemd/systemd-stable/commit/156e519d990a5662c719a1cbe80c6a02a2b9115f (v253.17)
https://github.com/systemd/systemd-stable/commit/7633d969f3422f9ad380a512987d398e54764817 (v252.23)
https://github.com/systemd/systemd-stable/commit/b43bcb51ebf9aea21b1e280e1872056994e3f53d (v252.23)
systemd: DNSSEC is default to off in systemd-resolved
https://github.com/advisories/GHSA-mmwx-rj87-vfgr
https://github.com/dnsjava/dnsjava/commit/711af79be3214f52daa5c846b95766dc0a075116 (v3.6.0)

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 1" src="https://img.shields.io/badge/H-1-e25d68"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 1" src="https://img.shields.io/badge/L-1-fce1a9"/> <!-- unspecified: 0 --><strong>ip</strong> <code>2.0.0</code> (npm)</summary>

<small><code>pkg:npm/ip@2.0.0</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2024-29415?s=github&n=ip&t=npm&vr=%3C%3D2.0.1"><img alt="high 8.1: CVE--2024--29415" src="https://img.shields.io/badge/CVE--2024--29415-lightgrey?label=high%208.1&labelColor=e25d68"/></a> <i>Server-Side Request Forgery (SSRF)</i>

<table>
<tr><td>Affected range</td><td><code><=2.0.1</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>CVSS Score</td><td><code>8.1</code></td></tr>
<tr><td>CVSS Vector</td><td><code>CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.062%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>29th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

The ip package through 2.0.1 for Node.js might allow SSRF because some IP addresses (such as 127.1, 01200034567, 012.1.2.3, 000:0:0000::01, and ::fFFf:127.0.0.1) are improperly categorized as globally routable via isPublic. NOTE: this issue exists because of an incomplete fix for CVE-2023-42282.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2023-42282?s=github&n=ip&t=npm&vr=%3E%3D2.0.0%2C%3C2.0.1"><img alt="low : CVE--2023--42282" src="https://img.shields.io/badge/CVE--2023--42282-lightgrey?label=low%20&labelColor=fce1a9"/></a> <i>Server-Side Request Forgery (SSRF)</i>

<table>
<tr><td>Affected range</td><td><code>>=2.0.0<br/><2.0.1</code></td></tr>
<tr><td>Fixed version</td><td><code>2.0.1</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.145%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>51st percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

The `isPublic()` function in the NPM package `ip` doesn't correctly identify certain private IP addresses in uncommon formats such as `0x7F.1` as private. Instead, it reports them as public by returning `true`. This can lead to security issues such as Server-Side Request Forgery (SSRF) if `isPublic()` is used to protect sensitive code paths when passed user input. Versions 1.1.9 and 2.0.1 fix the issue.

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 1" src="https://img.shields.io/badge/H-1-e25d68"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 0" src="https://img.shields.io/badge/L-0-lightgrey"/> <!-- unspecified: 0 --><strong>perl</strong> <code>5.36.0-7</code> (deb)</summary>

<small><code>pkg:deb/debian/perl@5.36.0-7?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2023-47038?s=debian&n=perl&ns=debian&t=deb&osn=debian&osv=12&vr=%3C5.36.0-7%2Bdeb12u1"><img alt="high : CVE--2023--47038" src="https://img.shields.io/badge/CVE--2023--47038-lightgrey?label=high%20&labelColor=e25d68"/></a> 

<table>
<tr><td>Affected range</td><td><code><5.36.0-7+deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><code>5.36.0-7+deb12u1</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.042%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>5th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A vulnerability was found in perl 5.30.0 through 5.38.0. This issue occurs when a crafted regular expression is compiled by perl, which can allow an attacker controlled byte buffer overflow in a heap allocated buffer.

---
- perl 5.36.0-10 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1056746)
[bookworm] - perl 5.36.0-7+deb12u1
[bullseye] - perl 5.32.1-4+deb11u3
[buster] - perl <not-affected> (Vulnerable code introduced later)
Fixed by: https://github.com/Perl/perl5/commit/12c313ce49b36160a7ca2e9b07ad5bd92ee4a010 (v5.34.2)
Fixed by: https://github.com/Perl/perl5/commit/7047915eef37fccd93e7cd985c29fe6be54650b6 (v5.36.2)
Fixed by: https://github.com/Perl/perl5/commit/92a9eb3d0d52ec7655c1beb29999a5a5219be664 (v5.38.1)
Fixed by: https://github.com/Perl/perl5/commit/ff1f9f59360afeebd6f75ca1502f5c3ebf077da3 (bleed)

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 1" src="https://img.shields.io/badge/H-1-e25d68"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 0" src="https://img.shields.io/badge/L-0-lightgrey"/> <!-- unspecified: 0 --><strong>gdk-pixbuf</strong> <code>2.42.10+dfsg-1</code> (deb)</summary>

<small><code>pkg:deb/debian/gdk-pixbuf@2.42.10%2Bdfsg-1?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2022-48622?s=debian&n=gdk-pixbuf&ns=debian&t=deb&osn=debian&osv=12&vr=%3C2.42.10%2Bdfsg-1%2Bdeb12u1"><img alt="high : CVE--2022--48622" src="https://img.shields.io/badge/CVE--2022--48622-lightgrey?label=high%20&labelColor=e25d68"/></a> 

<table>
<tr><td>Affected range</td><td><code><2.42.10+dfsg-1+deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><code>2.42.10+dfsg-1+deb12u1</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.097%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>42nd percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

In GNOME GdkPixbuf (aka gdk-pixbuf) through 2.42.10, the ANI (Windows animated cursor) decoder encounters heap memory corruption (in ani_load_chunk in io-ani.c) when parsing chunks in a crafted .ani file. A crafted file could allow an attacker to overwrite heap metadata, leading to a denial of service or code execution attack. This occurs in gdk_pixbuf_set_option() in gdk-pixbuf.c.

---
- gdk-pixbuf 2.42.12+dfsg-1 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1071265)
[bookworm] - gdk-pixbuf 2.42.10+dfsg-1+deb12u1
[bullseye] - gdk-pixbuf 2.42.2+dfsg-1+deb11u2
[buster] - gdk-pixbuf <postponed> (Minor issue, recheck when fixed upstream)
https://gitlab.gnome.org/GNOME/gdk-pixbuf/-/issues/202
Fixed by: https://gitlab.gnome.org/GNOME/gdk-pixbuf/-/commit/00c071dd11f723ca608608eef45cb1aa98da89cc (2.42.12)
Further improvements/hardenings:
https://gitlab.gnome.org/GNOME/gdk-pixbuf/-/commit/d52134373594ff76614fb415125b0d1c723ddd56 (2.42.12)
https://gitlab.gnome.org/GNOME/gdk-pixbuf/-/commit/91b8aa5cd8a0eea28acb51f0e121827ca2e7eb78 (2.42.12)

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 1" src="https://img.shields.io/badge/H-1-e25d68"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 0" src="https://img.shields.io/badge/L-0-lightgrey"/> <!-- unspecified: 0 --><strong>libxml2</strong> <code>2.9.14+dfsg-1.2</code> (deb)</summary>

<small><code>pkg:deb/debian/libxml2@2.9.14%2Bdfsg-1.2?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2022-2309?s=debian&n=libxml2&ns=debian&t=deb&osn=debian&osv=12&vr=%3C2.9.14%2Bdfsg-1.3%7Edeb12u1"><img alt="high : CVE--2022--2309" src="https://img.shields.io/badge/CVE--2022--2309-lightgrey?label=high%20&labelColor=e25d68"/></a> 

<table>
<tr><td>Affected range</td><td><code><2.9.14+dfsg-1.3~deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><code>2.9.14+dfsg-1.3~deb12u1</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.618%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>79th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

NULL Pointer Dereference allows attackers to cause a denial of service (or application crash). This only applies when lxml is used together with libxml2 2.9.10 through 2.9.14. libxml2 2.9.9 and earlier are not affected. It allows triggering crashes through forged input data, given a vulnerable code sequence in the application. The vulnerability is caused by the iterwalk function (also used by the canonicalize function). Such code shouldn't be in wide-spread use, given that parsing + iterwalk would usually be replaced with the more efficient iterparse function. However, an XML converter that serialises to C14N would also be vulnerable, for example, and there are legitimate use cases for this code sequence. If untrusted input is received (also remotely) and processed via iterwalk function, a crash can be triggered.

---
- lxml 4.9.1-1 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1014766)
[bullseye] - lxml <no-dsa> (Minor issue)
[buster] - lxml <no-dsa> (Minor issue)
- libxml2 2.9.14+dfsg-1.3 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1039991)
[bookworm] - libxml2 2.9.14+dfsg-1.3~deb12u1
[buster] - libxml2 <no-dsa> (Minor issue)
https://huntr.dev/bounties/8264e74f-edda-4c40-9956-49de635105ba/
https://github.com/lxml/lxml/commit/86368e9cf70a0ad23cccd5ee32de847149af0c6f (lxml-4.9.1)
https://gitlab.gnome.org/GNOME/libxml2/-/issues/378
Fixed by: https://gitlab.gnome.org/GNOME/libxml2/-/commit/5930fe01963136ab92125feec0c6204d9c9225dc (v2.10.0)
Fixed by: https://gitlab.gnome.org/GNOME/libxml2/-/commit/a82ea25fc83f563c574ddb863d6c17d9c5abdbd2 (v2.10.0)

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 1" src="https://img.shields.io/badge/H-1-e25d68"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 0" src="https://img.shields.io/badge/L-0-lightgrey"/> <!-- unspecified: 0 --><strong>semver</strong> <code>7.3.8</code> (npm)</summary>

<small><code>pkg:npm/semver@7.3.8</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2022-25883?s=github&n=semver&t=npm&vr=%3E%3D7.0.0%2C%3C7.5.2"><img alt="high 7.5: CVE--2022--25883" src="https://img.shields.io/badge/CVE--2022--25883-lightgrey?label=high%207.5&labelColor=e25d68"/></a> <i>Inefficient Regular Expression Complexity</i>

<table>
<tr><td>Affected range</td><td><code>>=7.0.0<br/><7.5.2</code></td></tr>
<tr><td>Fixed version</td><td><code>7.5.2</code></td></tr>
<tr><td>CVSS Score</td><td><code>7.5</code></td></tr>
<tr><td>CVSS Vector</td><td><code>CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.480%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>76th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

Versions of the package semver before 7.5.2 on the 7.x branch, before 6.3.1 on the 6.x branch, and all other versions before 5.7.2 are vulnerable to Regular Expression Denial of Service (ReDoS) via the function new Range, when untrusted user data is provided as a range.

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 2" src="https://img.shields.io/badge/M-2-fbb552"/> <img alt="low: 2" src="https://img.shields.io/badge/L-2-fce1a9"/> <!-- unspecified: 0 --><strong>libwmf</strong> <code>0.2.12-5.1</code> (deb)</summary>

<small><code>pkg:deb/debian/libwmf@0.2.12-5.1?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2009-3546?s=debian&n=libwmf&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D0.2.12-5.1"><img alt="medium : CVE--2009--3546" src="https://img.shields.io/badge/CVE--2009--3546-lightgrey?label=medium%20&labelColor=fbb552"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=0.2.12-5.1</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>1.805%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>88th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

The _gdGetColors function in gd_gd.c in PHP 5.2.11 and 5.3.x before 5.3.1, and the GD Graphics Library 2.x, does not properly verify a certain colorsTotal structure member, which might allow remote attackers to conduct buffer overflow or buffer over-read attacks via a crafted GD file, a different vulnerability than CVE-2009-3293. NOTE: some of these details are obtained from third party information.

---
- libwmf <unfixed> (unimportant)
- racket 5.0.2-1 (unimportant; bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=601525)
Only present in one of the sample pl-scheme packages (plot)
- libgd2 2.0.36~rc1~dfsg-3.1 (medium; bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=552534)
- php5 <not-affected> (the php packages use the system libgd2)
http://svn.php.net/viewvc?view=revision&revision=289557
<20091015173822.084de220@redhat.com> in OSS-sec

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2007-3996?s=debian&n=libwmf&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D0.2.12-5.1"><img alt="medium : CVE--2007--3996" src="https://img.shields.io/badge/CVE--2007--3996-lightgrey?label=medium%20&labelColor=fbb552"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=0.2.12-5.1</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>5.414%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>93rd percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

Multiple integer overflows in libgd in PHP before 5.2.4 allow remote attackers to cause a denial of service (application crash) and possibly execute arbitrary code via a large (1) srcW or (2) srcH value to the (a) gdImageCopyResized function, or a large (3) sy (height) or (4) sx (width) value to the (b) gdImageCreate or the (c) gdImageCreateTrueColor function.

---
- libgd2 2.0.35.dfsg-1 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=443456; medium)
- libwmf <unfixed> (unimportant)
- racket 5.0.2-1 (unimportant; bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=601525)
Only present in one of the sample pl-scheme packages (plot)
Debian's PHP packages are linked dynamically against libgd
see http://www.php.net/releases/5_2_4.php

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2007-3477?s=debian&n=libwmf&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D0.2.12-5.1"><img alt="low : CVE--2007--3477" src="https://img.shields.io/badge/CVE--2007--3477-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=0.2.12-5.1</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>2.882%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>91st percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

The (a) imagearc and (b) imagefilledarc functions in GD Graphics Library (libgd) before 2.0.35 allow attackers to cause a denial of service (CPU consumption) via a large (1) start or (2) end angle degree value.

---
- libgd2 2.0.35.dfsg-1 (low)
- libwmf <unfixed> (unimportant)
- racket 5.0.2-1 (unimportant; bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=601525)
Only present in one of the sample pl-scheme packages (plot)
CPU consumption DoS

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2007-3476?s=debian&n=libwmf&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D0.2.12-5.1"><img alt="low : CVE--2007--3476" src="https://img.shields.io/badge/CVE--2007--3476-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=0.2.12-5.1</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>3.867%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>92nd percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

Array index error in gd_gif_in.c in the GD Graphics Library (libgd) before 2.0.35 allows user-assisted remote attackers to cause a denial of service (crash and heap corruption) via large color index values in crafted image data, which results in a segmentation fault.

---
- libgd2 2.0.35.dfsg-1 (low)
- libwmf <unfixed> (unimportant)
- racket 5.0.2-1 (unimportant; bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=601525)
Only present in one of the sample pl-scheme packages (plot)
can write a 0 to a 4k window in heap, very unlikely to be controllable.

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 1" src="https://img.shields.io/badge/M-1-fbb552"/> <img alt="low: 1" src="https://img.shields.io/badge/L-1-fce1a9"/> <!-- unspecified: 0 --><strong>sqlite3</strong> <code>3.40.1-2</code> (deb)</summary>

<small><code>pkg:deb/debian/sqlite3@3.40.1-2?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2023-7104?s=debian&n=sqlite3&ns=debian&t=deb&osn=debian&osv=12&vr=%3C3.40.1-2%2Bdeb12u1"><img alt="medium : CVE--2023--7104" src="https://img.shields.io/badge/CVE--2023--7104-lightgrey?label=medium%20&labelColor=fbb552"/></a> 

<table>
<tr><td>Affected range</td><td><code><3.40.1-2+deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><code>3.40.1-2+deb12u1</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.203%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>59th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A vulnerability was found in SQLite SQLite3 up to 3.43.0 and classified as critical. This issue affects the function sessionReadRecord of the file ext/session/sqlite3session.c of the component make alltest Handler. The manipulation leads to heap-based buffer overflow. It is recommended to apply a patch to fix this issue. The associated identifier of this vulnerability is VDB-248999.

---
- sqlite3 3.43.1-1
[bookworm] - sqlite3 3.40.1-2+deb12u1
[buster] - sqlite3 <no-dsa> (Minor issue)
https://sqlite.org/forum/forumpost/5bcbf4571c
Fixed by: https://sqlite.org/src/info/0e4e7a05c4204b47

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2023-36191?s=debian&n=sqlite3&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D3.40.1-2"><img alt="low : CVE--2023--36191" src="https://img.shields.io/badge/CVE--2023--36191-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=3.40.1-2</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.044%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>15th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

sqlite3 v3.40.1 was discovered to contain a segmentation violation at /sqlite3_aflpp/shell.c.

---
REJECTED

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 1" src="https://img.shields.io/badge/M-1-fbb552"/> <img alt="low: 1" src="https://img.shields.io/badge/L-1-fce1a9"/> <!-- unspecified: 0 --><strong>nghttp2</strong> <code>1.52.0-1</code> (deb)</summary>

<small><code>pkg:deb/debian/nghttp2@1.52.0-1?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2024-28182?s=debian&n=nghttp2&ns=debian&t=deb&osn=debian&osv=12&vr=%3C1.52.0-1%2Bdeb12u2"><img alt="medium : CVE--2024--28182" src="https://img.shields.io/badge/CVE--2024--28182-lightgrey?label=medium%20&labelColor=fbb552"/></a> 

<table>
<tr><td>Affected range</td><td><code><1.52.0-1+deb12u2</code></td></tr>
<tr><td>Fixed version</td><td><code>1.52.0-1+deb12u2</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.044%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>16th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

nghttp2 is an implementation of the Hypertext Transfer Protocol version 2 in C. The nghttp2 library prior to version 1.61.0 keeps reading the unbounded number of HTTP/2 CONTINUATION frames even after a stream is reset to keep HPACK context in sync.  This causes excessive CPU usage to decode HPACK stream. nghttp2 v1.61.0 mitigates this vulnerability by limiting the number of CONTINUATION frames it accepts per stream. There is no workaround for this vulnerability.

---
- nghttp2 1.61.0-1 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1068415)
[bookworm] - nghttp2 1.52.0-1+deb12u2
https://github.com/nghttp2/nghttp2/security/advisories/GHSA-x6x3-gv8h-m57q
https://www.kb.cert.org/vuls/id/421644
https://github.com/nghttp2/nghttp2/commit/00201ecd8f982da3b67d4f6868af72a1b03b14e0 (v1.61.0)
https://github.com/nghttp2/nghttp2/commit/d71a4668c6bead55805d18810d633fbb98315af9 (v1.61.0)

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2023-44487?s=debian&n=nghttp2&ns=debian&t=deb&osn=debian&osv=12&vr=%3C1.52.0-1%2Bdeb12u1"><img alt="low : CVE--2023--44487" src="https://img.shields.io/badge/CVE--2023--44487-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code><1.52.0-1+deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><code>1.52.0-1+deb12u1</code></td></tr>
<tr><td>EPSS Score</td><td><code>85.557%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>99th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

The HTTP/2 protocol allows a denial of service (server resource consumption) because request cancellation can reset many streams quickly, as exploited in the wild in August through October 2023.

---
- tomcat9 9.0.70-2
- tomcat10 10.1.14-1
- trafficserver 9.2.3+ds-1 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1053801; bug #1054427)
- grpc <unfixed> (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1074421)
[bookworm] - grpc <no-dsa> (Minor issue)
[bullseye] - grpc <no-dsa> (Minor issue)
[buster] - grpc <no-dsa> (Minor issue)
- h2o 2.2.5+dfsg2-8 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1054232)
[bookworm] - h2o <no-dsa> (Minor issue)
[bullseye] - h2o <postponed> (Minor issue, DoS)
- haproxy 1.8.13-1
- nginx 1.24.0-2 (unimportant; bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1053770)
- nghttp2 1.57.0-1 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1053769)
- jetty9 9.4.53-1
- netty 1:4.1.48-8 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1054234)
- dnsdist 1.8.2-2
[bookworm] - dnsdist <no-dsa> (Minor issue)
[bullseye] - dnsdist <no-dsa> (Minor issue)
[buster] - dnsdist <not-affected> (HTTP/2 support was added later)
- varnish 7.5.0-1 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1056156)
[bookworm] - varnish <ignored> (Minor issue, too intrusive to backport)
[bullseye] - varnish <ignored> (Minor issue, too intrusive to backport)
Tomcat: https://github.com/apache/tomcat/commit/76bb4bfbfeae827dce896f650655bbf6e251ed49 (10.1.14)
Tomcat: https://github.com/apache/tomcat/commit/6d1a9fd6642387969e4410b9989c85856b74917a (9.0.81)
Starting with 9.0.70-2 Tomcat9 no longer ships the server stack, using that as the fixed version
ATS: https://lists.apache.org/thread/5py8h42mxfsn8l1wy6o41xwhsjlsd87q
ATS: https://github.com/apache/trafficserver/commit/b28ad74f117307e8de206f1de70c3fa716f90682 (9.2.3-rc0)
ATS: https://github.com/apache/trafficserver/commit/d742d74039aaa548dda0148ab4ba207906abc620 (8.1.9)
grpc: https://github.com/grpc/grpc/pull/34763
h2o: https://github.com/h2o/h2o/commit/28fe15117b909588bf14269a0e1c6ec4548579fe
dnsdist: h2o change breaks the ABI, hence dnsdist switched to a vendored fix in 1.8.2-2
haproxy: http://git.haproxy.org/?p=haproxy.git;a=commit;h=f210191dcdf32a2cb263c5bd22b7fc98698ce59a (v1.9-dev1)
haproxy: https://www.mail-archive.com/haproxy@formilux.org/msg44134.html
haproxy: https://www.mail-archive.com/haproxy@formilux.org/msg44136.html
nginx: https://mailman.nginx.org/pipermail/nginx-devel/2023-October/S36Q5HBXR7CAIMPLLPRSSSYR4PCMWILK.html
nginx: https://github.com/nginx/nginx/commit/6ceef192e7af1c507826ac38a2d43f08bf265fb9
nghttp2: https://github.com/nghttp2/nghttp2/pull/1961
nghttp2: https://github.com/nghttp2/nghttp2/security/advisories/GHSA-vx74-f528-fxqg
nghttp2: https://github.com/nghttp2/nghttp2/commit/72b4af6143681f528f1d237b21a9a7aee1738832 (v1.57.0)
jetty9: https://github.com/eclipse/jetty.project/issues/10679
jetty9: https://github.com/eclipse/jetty.project/releases/tag/jetty-9.4.53.v20231009
https://www.openwall.com/lists/oss-security/2023/10/10/6
https://blog.cloudflare.com/technical-breakdown-http2-rapid-reset-ddos-attack/
Go uses CVE-2023-39325 to track this
netty: https://github.com/netty/netty/security/advisories/GHSA-xpw8-rcwv-8f8p
netty: https://github.com/netty/netty/commit/58f75f665aa81a8cbcf6ffa74820042a285c5e61 (netty-4.1.100.Final)
varnish: https://varnish-cache.org/security/VSV00013.html
varnish: https://github.com/varnishcache/varnish-cache/issues/3996
https://varnish-cache.org/docs/7.5/whats-new/changes-7.5.html#cve-2023-44487
Unaffected implementations not requiring code changes:
- rust-hyper: https://seanmonstar.com/post/730794151136935936/hyper-http2-rapid-reset-unaffected
- apache2: https://chaos.social/@icing/111210915918780532
- lighttpd: https://www.openwall.com/lists/oss-security/2023/10/13/9

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 1" src="https://img.shields.io/badge/M-1-fbb552"/> <img alt="low: 1" src="https://img.shields.io/badge/L-1-fce1a9"/> <!-- unspecified: 0 --><strong>tar</strong> <code>1.34+dfsg-1.2</code> (deb)</summary>

<small><code>pkg:deb/debian/tar@1.34%2Bdfsg-1.2?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2023-39804?s=debian&n=tar&ns=debian&t=deb&osn=debian&osv=12&vr=%3C1.34%2Bdfsg-1.2%2Bdeb12u1"><img alt="medium : CVE--2023--39804" src="https://img.shields.io/badge/CVE--2023--39804-lightgrey?label=medium%20&labelColor=fbb552"/></a> 

<table>
<tr><td>Affected range</td><td><code><1.34+dfsg-1.2+deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><code>1.34+dfsg-1.2+deb12u1</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.045%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>18th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

In GNU tar before 1.35, mishandled extension attributes in a PAX archive can lead to an application crash in xheader.c.

---
- tar 1.34+dfsg-1.3 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1058079)
[bookworm] - tar 1.34+dfsg-1.2+deb12u1
[bullseye] - tar 1.34+dfsg-1+deb11u1
Fixed by: https://git.savannah.gnu.org/cgit/tar.git/commit/?id=a339f05cd269013fa133d2f148d73f6f7d4247e4 (v1.35)

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2022-48303?s=debian&n=tar&ns=debian&t=deb&osn=debian&osv=12&vr=%3C1.34%2Bdfsg-1.2%2Bdeb12u1"><img alt="low : CVE--2022--48303" src="https://img.shields.io/badge/CVE--2022--48303-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code><1.34+dfsg-1.2+deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><code>1.34+dfsg-1.2+deb12u1</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.067%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>32nd percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

GNU Tar through 1.34 has a one-byte out-of-bounds read that results in use of uninitialized memory for a conditional jump. Exploitation to change the flow of control has not been demonstrated. The issue occurs in from_header in list.c via a V7 archive in which mtime has approximately 11 whitespace characters.

---
- tar 1.34+dfsg-1.4 (unimportant)
[bookworm] - tar 1.34+dfsg-1.2+deb12u1
[bullseye] - tar 1.34+dfsg-1+deb11u1
Crash in CLI tool, no security impact
https://savannah.gnu.org/bugs/?62387
https://savannah.gnu.org/patch/?10307
Fixed by: https://git.savannah.gnu.org/cgit/tar.git/commit/?id=3da78400eafcccb97e2f2fd4b227ea40d794ede8 (v1.35)

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 1" src="https://img.shields.io/badge/M-1-fbb552"/> <img alt="low: 0" src="https://img.shields.io/badge/L-0-lightgrey"/> <!-- unspecified: 0 --><strong>dav1d</strong> <code>1.0.0-2</code> (deb)</summary>

<small><code>pkg:deb/debian/dav1d@1.0.0-2?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2024-1580?s=debian&n=dav1d&ns=debian&t=deb&osn=debian&osv=12&vr=%3C1.0.0-2%2Bdeb12u1"><img alt="medium : CVE--2024--1580" src="https://img.shields.io/badge/CVE--2024--1580-lightgrey?label=medium%20&labelColor=fbb552"/></a> 

<table>
<tr><td>Affected range</td><td><code><1.0.0-2+deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><code>1.0.0-2+deb12u1</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.288%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>69th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

An integer overflow in dav1d AV1 decoder that can occur when decoding videos with large frame size. This can lead to memory corruption within the AV1 decoder. We recommend upgrading past version 1.4.0 of dav1d.

---
- dav1d 1.4.0-1 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1064310)
https://code.videolan.org/videolan/dav1d/commit/2b475307dc11be9a1c3cc4358102c76a7f386a51 (1.4.0)
https://bugs.chromium.org/p/project-zero/issues/detail?id=2502

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 1" src="https://img.shields.io/badge/M-1-fbb552"/> <img alt="low: 0" src="https://img.shields.io/badge/L-0-lightgrey"/> <!-- unspecified: 0 --><strong>mariadb</strong> <code>1:10.11.3-1</code> (deb)</summary>

<small><code>pkg:deb/debian/mariadb@1:10.11.3-1?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2023-22084?s=debian&n=mariadb&ns=debian&t=deb&osn=debian&osv=12&vr=%3C1%3A10.11.6-0%2Bdeb12u1"><img alt="medium : CVE--2023--22084" src="https://img.shields.io/badge/CVE--2023--22084-lightgrey?label=medium%20&labelColor=fbb552"/></a> 

<table>
<tr><td>Affected range</td><td><code><1:10.11.6-0+deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><code>1:10.11.6-0+deb12u1</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.101%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>43rd percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

Vulnerability in the MySQL Server product of Oracle MySQL (component: InnoDB).  Supported versions that are affected are 5.7.43 and prior, 8.0.34 and prior and  8.1.0. Easily exploitable vulnerability allows high privileged attacker with network access via multiple protocols to compromise MySQL Server.  Successful attacks of this vulnerability can result in unauthorized ability to cause a hang or frequently repeatable crash (complete DOS) of MySQL Server. CVSS 3.1 Base Score 4.9 (Availability impacts).  CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:N/I:N/A:H).

---
- mariadb 1:10.11.6-1
[bookworm] - mariadb 1:10.11.6-0+deb12u1
- mariadb-10.5 <removed>
[bullseye] - mariadb-10.5 1:10.5.23-0+deb11u1
- mariadb-10.3 <removed>
- mysql-8.0 8.0.35-1 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1055034)
Fixed in MariaDB: 11.2.2, 11.1.3, 11.0.4, 10.11.6, 10.10.7, 10.6.16, 10.5.23, 10.4.32
https://github.com/MariaDB/server/commit/15ae97b1c2c14f1263cdc853673c4129625323de (mariadb-10.4.32)
MariaDB bug: https://jira.mariadb.org/browse/MDEV-32578
MySQL commit: https://github.com/mysql/mysql-server/commit/38e9a0779aeea2d197c727e306a910c56b26a47c (mysql-5.7.44)
Introduced by MySQL commit: https://github.com/mysql/mysql-server/commit/0c954c2289a75d90d1088356b1092437ebf45a1d (mysql-5.7.2-12)

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 1" src="https://img.shields.io/badge/M-1-fbb552"/> <img alt="low: 0" src="https://img.shields.io/badge/L-0-lightgrey"/> <!-- unspecified: 0 --><strong>apr</strong> <code>1.7.2-3</code> (deb)</summary>

<small><code>pkg:deb/debian/apr@1.7.2-3?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2023-49582?s=debian&n=apr&ns=debian&t=deb&osn=debian&osv=12&vr=%3C1.7.2-3%2Bdeb12u1"><img alt="medium : CVE--2023--49582" src="https://img.shields.io/badge/CVE--2023--49582-lightgrey?label=medium%20&labelColor=fbb552"/></a> 

<table>
<tr><td>Affected range</td><td><code><1.7.2-3+deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><code>1.7.2-3+deb12u1</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.042%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>5th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

Lax permissions set by the Apache Portable Runtime library on Unix platforms would allow local users read access to named shared memory segments, potentially revealing sensitive application data.   This issue does not affect non-Unix platforms, or builds with APR_USE_SHMEM_SHMGET=1 (apr.h)  Users are recommended to upgrade to APR version 1.7.5, which fixes this issue.

---
- apr 1.7.5-1 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1080375)
[bookworm] - apr 1.7.2-3+deb12u1
[bullseye] - apr <ignored> (binary packages not affected due to APR_USE_SHMEM_SHMGET=1)
https://www.openwall.com/lists/oss-security/2024/08/26/1
https://lists.apache.org/thread/h5f1c2dqm8bf5yfosw3rg85927p612l0
Exposed by: https://github.com/apache/apr/commit/dcdd7daaef7ee6c077a4769a5bec1fbc11e5611f (trunk)
Exposed by: https://github.com/apache/apr/commit/ebd6c401ccceea461a929122526caacf9c9e7b1d (1.7.1-rc1)
Fixed by: https://github.com/apache/apr/commit/501072062dfcbc459f5d1e576113d17c7de84d5a (trunk)
Fixed by: https://github.com/apache/apr/commit/36ea6d5a2bfc480dd8032cc8651e6793552bc2aa (1.7.5)

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 1" src="https://img.shields.io/badge/M-1-fbb552"/> <img alt="low: 0" src="https://img.shields.io/badge/L-0-lightgrey"/> <!-- unspecified: 0 --><strong>libtasn1-6</strong> <code>4.19.0-2</code> (deb)</summary>

<small><code>pkg:deb/debian/libtasn1-6@4.19.0-2?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2024-12133?s=debian&n=libtasn1-6&ns=debian&t=deb&osn=debian&osv=12&vr=%3C4.19.0-2%2Bdeb12u1"><img alt="medium : CVE--2024--12133" src="https://img.shields.io/badge/CVE--2024--12133-lightgrey?label=medium%20&labelColor=fbb552"/></a> 

<table>
<tr><td>Affected range</td><td><code><4.19.0-2+deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><code>4.19.0-2+deb12u1</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.045%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>18th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A flaw in libtasn1 causes inefficient handling of specific certificate data. When processing a large number of elements in a certificate, libtasn1 takes much longer than expected, which can slow down or even crash the system. This flaw allows an attacker to send a specially crafted certificate, causing a denial of service attack.

---
- libtasn1-6 4.20.0-1 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1095406)
https://www.openwall.com/lists/oss-security/2025/02/06/6
https://gitlab.com/gnutls/libtasn1/-/issues/52
https://gitlab.com/gnutls/libtasn1/-/commit/4082ca2220b5ba910b546afddf7780fc4a51f75a (v4.20.0)
https://gitlab.com/gnutls/libtasn1/-/commit/869a97aa259dffa2620dabcad84e1c22545ffc3d (v4.20.0)
https://lists.gnu.org/archive/html/help-libtasn1/2025-02/msg00001.html

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 1" src="https://img.shields.io/badge/M-1-fbb552"/> <img alt="low: 0" src="https://img.shields.io/badge/L-0-lightgrey"/> <!-- unspecified: 0 --><strong>librsvg</strong> <code>2.54.5+dfsg-1</code> (deb)</summary>

<small><code>pkg:deb/debian/librsvg@2.54.5%2Bdfsg-1?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2023-38633?s=debian&n=librsvg&ns=debian&t=deb&osn=debian&osv=12&vr=%3C2.54.7%2Bdfsg-1%7Edeb12u1"><img alt="medium : CVE--2023--38633" src="https://img.shields.io/badge/CVE--2023--38633-lightgrey?label=medium%20&labelColor=fbb552"/></a> 

<table>
<tr><td>Affected range</td><td><code><2.54.7+dfsg-1~deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><code>2.54.7+dfsg-1~deb12u1</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.225%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>61st percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A directory traversal problem in the URL decoder of librsvg before 2.56.3 could be used by local or remote attackers to disclose files (on the local filesystem outside of the expected area), as demonstrated by href=".?../../../../../../../../../../etc/passwd" in an xi:include element.

---
- librsvg 2.54.7+dfsg-1 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1041810)
[buster] - librsvg <not-affected> (The vulnerable code was introduced later)
https://bugzilla.suse.com/show_bug.cgi?id=1213502
https://gitlab.gnome.org/GNOME/librsvg/-/issues/996
https://gitlab.gnome.org/GNOME/librsvg/-/commit/15293f1243e1dd4756ffc1d13d5a8ea49167174f (2.54.6)
https://gitlab.gnome.org/GNOME/librsvg/-/commit/d1f066bf2198bd46c5ba80cb5123b768ec16e37d (2.50.8)
https://gitlab.gnome.org/GNOME/librsvg/-/commit/22bcb919c8b39133370c7fc0eb27176fb09aa4fb (2.46.6)
https://www.openwall.com/lists/oss-security/2023/07/27/1
https://www.canva.dev/blog/engineering/when-url-parsers-disagree-cve-2023-38633/

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 1" src="https://img.shields.io/badge/M-1-fbb552"/> <img alt="low: 0" src="https://img.shields.io/badge/L-0-lightgrey"/> <!-- unspecified: 0 --><strong>tar</strong> <code>6.1.13</code> (npm)</summary>

<small><code>pkg:npm/tar@6.1.13</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2024-28863?s=github&n=tar&t=npm&vr=%3C6.2.1"><img alt="medium 6.5: CVE--2024--28863" src="https://img.shields.io/badge/CVE--2024--28863-lightgrey?label=medium%206.5&labelColor=fbb552"/></a> <i>Uncontrolled Resource Consumption</i>

<table>
<tr><td>Affected range</td><td><code><6.2.1</code></td></tr>
<tr><td>Fixed version</td><td><code>6.2.1</code></td></tr>
<tr><td>CVSS Score</td><td><code>6.5</code></td></tr>
<tr><td>CVSS Vector</td><td><code>CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:N/I:N/A:H</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.045%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>18th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

## Description: 
During some analysis today on npm's `node-tar` package I came across the folder creation process, Basicly if you provide node-tar with a path like this `./a/b/c/foo.txt` it would create every folder and sub-folder here a, b and c until it reaches the last folder to create `foo.txt`, In-this case I noticed that there's no validation at all on the amount of folders being created, that said we're actually able to CPU and memory consume the system running node-tar and even crash the nodejs client within few seconds of running it using a path with too many sub-folders inside

## Steps To Reproduce:
You can reproduce this issue by downloading the tar file I provided in the resources and using node-tar to extract it, you should get the same behavior as the video

## Proof Of Concept:
Here's a [video](https://hackerone-us-west-2-production-attachments.s3.us-west-2.amazonaws.com/3i7uojw8s52psar6pg8zkdo4h9io?response-content-disposition=attachment%3B%20filename%3D%22tar-dos-poc.webm%22%3B%20filename%2A%3DUTF-8%27%27tar-dos-poc.webm&response-content-type=video%2Fwebm&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIAQGK6FURQSWWGDXHA%2F20240312%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20240312T080103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDcaCXVzLXdlc3QtMiJHMEUCID3xYDc6emXVPOg8iVR5dVk0u3gguTPIDJ0OIE%2BKxj17AiEAi%2BGiay1gGMWhH%2F031fvMYnSsa8U7CnpZpxvFAYqNRwgqsQUIQBADGgwwMTM2MTkyNzQ4NDkiDAaj6OgUL3gg4hhLLCqOBUUrOgWSqaK%2FmxN6nKRvB4Who3LIyzswFKm9LV94GiSVFP3zXYA480voCmAHTg7eBL7%2BrYgV2RtXbhF4aCFMCN3qu7GeXkIdH7xwVMi9zXHkekviSKZ%2FsZtVVjn7RFqOCKhJl%2FCoiLQJuDuju%2FtfdTGZbEbGsPgKHoILYbRp81K51zeRL21okjsOehmypkZzq%2BoGrXIX0ynPOKujxw27uqdF4T%2BF9ynodq01vGgwgVBEjHojc4OKOfr1oW5b%2FtGVV59%2BOBVI1hqIKHRG0Ed4SWmp%2BLd1hazGuZPvp52szmegnOj5qr3ubppnKL242bX%2FuAnQKzKK0HpwolqXjsuEeFeM85lxhqHV%2B1BJqaqSHHDa0HUMLZistMRshRlntuchcFQCR6HBa2c8PSnhpVC31zMzvYMfKsI12h4HB6l%2FudrmNrvmH4LmNpi4dZFcio21DzKj%2FRjWmxjH7l8egDyG%2FIgPMY6Ls4IiN7aR1jijYTrBCgPUUHets3BFvqLzHtPFnG3B7%2FYRPnhCLu%2FgzvKN3F8l38KqeTNMHJaxkuhCvEjpFB2SJbi2QZqZZbLj3xASqXoogzbsyPp0Tzp0tH7EKDhPA7H6wwiZukXfFhhlYzP8on9fO2Ajz%2F%2BTDkDjbfWw4KNJ0cFeDsGrUspqQZb5TAKlUge7iOZEc2TZ5uagatSy9Mg08E4nImBSE5QUHDc7Daya1gyqrETMDZBBUHH2RFkGA9qMpEtNrtJ9G%2BPedz%2FpPY1hh9OCp9Pg1BrX97l3SfVzlAMRfNibhywq6qnE35rVnZi%2BEQ1UgBjs9jD%2FQrW49%2FaD0oUDojVeuFFryzRnQxDbKtYgonRcItTvLT5Y0xaK9P0u6H1197%2FMk3XxmjD9%2Fb%2BvBjqxAQWWkKiIxpC1oHEWK9Jt8UdJ39xszDBGpBqjB6Tvt5ePAXSyX8np%2FrBi%2BAPx06O0%2Ba7pU4NmH800EVXxxhgfj9nMw3CeoUIdxorVKtU2Mxw%2FLaAiPgxPS4rqkt65NF7eQYfegcSYDTm2Z%2BHPbz9HfCaVZ28Zqeko6sR%2F29ML4bguqVvHAM4mWPLNDXH33mjG%2BuzLi8e1BF7tNveg2X9G%2FRdcMkojwKYbu6xN3M6aX2alQg%3D%3D&X-Amz-SignedHeaders=host&X-Amz-Signature=1e8235d885f1d61529b7d6b23ea3a0780c300c91d86e925dd8310d5b661ddbe2) show-casing the exploit: 

## Impact

Denial of service by crashing the nodejs client when attempting to parse a tar archive, make it run out of heap memory and consuming server CPU and memory resources

## Report resources
[payload.txt](https://hackerone-us-west-2-production-attachments.s3.us-west-2.amazonaws.com/1e83ayb5dd3350fvj3gst0mqixwk?response-content-disposition=attachment%3B%20filename%3D%22payload.txt%22%3B%20filename%2A%3DUTF-8%27%27payload.txt&response-content-type=text%2Fplain&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIAQGK6FURQSWWGDXHA%2F20240312%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20240312T080103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDcaCXVzLXdlc3QtMiJHMEUCID3xYDc6emXVPOg8iVR5dVk0u3gguTPIDJ0OIE%2BKxj17AiEAi%2BGiay1gGMWhH%2F031fvMYnSsa8U7CnpZpxvFAYqNRwgqsQUIQBADGgwwMTM2MTkyNzQ4NDkiDAaj6OgUL3gg4hhLLCqOBUUrOgWSqaK%2FmxN6nKRvB4Who3LIyzswFKm9LV94GiSVFP3zXYA480voCmAHTg7eBL7%2BrYgV2RtXbhF4aCFMCN3qu7GeXkIdH7xwVMi9zXHkekviSKZ%2FsZtVVjn7RFqOCKhJl%2FCoiLQJuDuju%2FtfdTGZbEbGsPgKHoILYbRp81K51zeRL21okjsOehmypkZzq%2BoGrXIX0ynPOKujxw27uqdF4T%2BF9ynodq01vGgwgVBEjHojc4OKOfr1oW5b%2FtGVV59%2BOBVI1hqIKHRG0Ed4SWmp%2BLd1hazGuZPvp52szmegnOj5qr3ubppnKL242bX%2FuAnQKzKK0HpwolqXjsuEeFeM85lxhqHV%2B1BJqaqSHHDa0HUMLZistMRshRlntuchcFQCR6HBa2c8PSnhpVC31zMzvYMfKsI12h4HB6l%2FudrmNrvmH4LmNpi4dZFcio21DzKj%2FRjWmxjH7l8egDyG%2FIgPMY6Ls4IiN7aR1jijYTrBCgPUUHets3BFvqLzHtPFnG3B7%2FYRPnhCLu%2FgzvKN3F8l38KqeTNMHJaxkuhCvEjpFB2SJbi2QZqZZbLj3xASqXoogzbsyPp0Tzp0tH7EKDhPA7H6wwiZukXfFhhlYzP8on9fO2Ajz%2F%2BTDkDjbfWw4KNJ0cFeDsGrUspqQZb5TAKlUge7iOZEc2TZ5uagatSy9Mg08E4nImBSE5QUHDc7Daya1gyqrETMDZBBUHH2RFkGA9qMpEtNrtJ9G%2BPedz%2FpPY1hh9OCp9Pg1BrX97l3SfVzlAMRfNibhywq6qnE35rVnZi%2BEQ1UgBjs9jD%2FQrW49%2FaD0oUDojVeuFFryzRnQxDbKtYgonRcItTvLT5Y0xaK9P0u6H1197%2FMk3XxmjD9%2Fb%2BvBjqxAQWWkKiIxpC1oHEWK9Jt8UdJ39xszDBGpBqjB6Tvt5ePAXSyX8np%2FrBi%2BAPx06O0%2Ba7pU4NmH800EVXxxhgfj9nMw3CeoUIdxorVKtU2Mxw%2FLaAiPgxPS4rqkt65NF7eQYfegcSYDTm2Z%2BHPbz9HfCaVZ28Zqeko6sR%2F29ML4bguqVvHAM4mWPLNDXH33mjG%2BuzLi8e1BF7tNveg2X9G%2FRdcMkojwKYbu6xN3M6aX2alQg%3D%3D&X-Amz-SignedHeaders=host&X-Amz-Signature=bad9fe731f05a63a950f99828125653a8c1254750fe0ca7be882e89ecdd449ae)
[archeive.tar.gz](https://hackerone-us-west-2-production-attachments.s3.us-west-2.amazonaws.com/ymkuh4xnfdcf1soeyi7jc2x4yt2i?response-content-disposition=attachment%3B%20filename%3D%22archive.tar.gz%22%3B%20filename%2A%3DUTF-8%27%27archive.tar.gz&response-content-type=application%2Fx-tar&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIAQGK6FURQSWWGDXHA%2F20240312%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20240312T080103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDcaCXVzLXdlc3QtMiJHMEUCID3xYDc6emXVPOg8iVR5dVk0u3gguTPIDJ0OIE%2BKxj17AiEAi%2BGiay1gGMWhH%2F031fvMYnSsa8U7CnpZpxvFAYqNRwgqsQUIQBADGgwwMTM2MTkyNzQ4NDkiDAaj6OgUL3gg4hhLLCqOBUUrOgWSqaK%2FmxN6nKRvB4Who3LIyzswFKm9LV94GiSVFP3zXYA480voCmAHTg7eBL7%2BrYgV2RtXbhF4aCFMCN3qu7GeXkIdH7xwVMi9zXHkekviSKZ%2FsZtVVjn7RFqOCKhJl%2FCoiLQJuDuju%2FtfdTGZbEbGsPgKHoILYbRp81K51zeRL21okjsOehmypkZzq%2BoGrXIX0ynPOKujxw27uqdF4T%2BF9ynodq01vGgwgVBEjHojc4OKOfr1oW5b%2FtGVV59%2BOBVI1hqIKHRG0Ed4SWmp%2BLd1hazGuZPvp52szmegnOj5qr3ubppnKL242bX%2FuAnQKzKK0HpwolqXjsuEeFeM85lxhqHV%2B1BJqaqSHHDa0HUMLZistMRshRlntuchcFQCR6HBa2c8PSnhpVC31zMzvYMfKsI12h4HB6l%2FudrmNrvmH4LmNpi4dZFcio21DzKj%2FRjWmxjH7l8egDyG%2FIgPMY6Ls4IiN7aR1jijYTrBCgPUUHets3BFvqLzHtPFnG3B7%2FYRPnhCLu%2FgzvKN3F8l38KqeTNMHJaxkuhCvEjpFB2SJbi2QZqZZbLj3xASqXoogzbsyPp0Tzp0tH7EKDhPA7H6wwiZukXfFhhlYzP8on9fO2Ajz%2F%2BTDkDjbfWw4KNJ0cFeDsGrUspqQZb5TAKlUge7iOZEc2TZ5uagatSy9Mg08E4nImBSE5QUHDc7Daya1gyqrETMDZBBUHH2RFkGA9qMpEtNrtJ9G%2BPedz%2FpPY1hh9OCp9Pg1BrX97l3SfVzlAMRfNibhywq6qnE35rVnZi%2BEQ1UgBjs9jD%2FQrW49%2FaD0oUDojVeuFFryzRnQxDbKtYgonRcItTvLT5Y0xaK9P0u6H1197%2FMk3XxmjD9%2Fb%2BvBjqxAQWWkKiIxpC1oHEWK9Jt8UdJ39xszDBGpBqjB6Tvt5ePAXSyX8np%2FrBi%2BAPx06O0%2Ba7pU4NmH800EVXxxhgfj9nMw3CeoUIdxorVKtU2Mxw%2FLaAiPgxPS4rqkt65NF7eQYfegcSYDTm2Z%2BHPbz9HfCaVZ28Zqeko6sR%2F29ML4bguqVvHAM4mWPLNDXH33mjG%2BuzLi8e1BF7tNveg2X9G%2FRdcMkojwKYbu6xN3M6aX2alQg%3D%3D&X-Amz-SignedHeaders=host&X-Amz-Signature=5e2c0d4b4de40373ac0fe91908c2659141a6dd4ab850271cc26042a3885c82ea)

## Note
This report was originally reported to GitHub bug bounty program, they asked me to report it to you a month ago

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 22" src="https://img.shields.io/badge/L-22-fce1a9"/> <!-- unspecified: 0 --><strong>binutils</strong> <code>2.40-2</code> (deb)</summary>

<small><code>pkg:deb/debian/binutils@2.40-2?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2025-1182?s=debian&n=binutils&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.40-2"><img alt="low : CVE--2025--1182" src="https://img.shields.io/badge/CVE--2025--1182-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.40-2</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.044%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>13th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A vulnerability, which was classified as critical, was found in GNU Binutils 2.43. Affected is the function bfd_elf_reloc_symbol_deleted_p of the file bfd/elflink.c of the component ld. The manipulation leads to memory corruption. It is possible to launch the attack remotely. The complexity of an attack is rather high. The exploitability is told to be difficult. The exploit has been disclosed to the public and may be used. The patch is identified as b425859021d17adf62f06fb904797cf8642986ad. It is recommended to apply a patch to fix this issue.

---
- binutils <unfixed> (unimportant)
https://sourceware.org/bugzilla/show_bug.cgi?id=32644
https://sourceware.org/git/gitweb.cgi?p=binutils-gdb.git;h=b425859021d17adf62f06fb904797cf8642986ad
binutils not covered by security support

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2025-1181?s=debian&n=binutils&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.40-2"><img alt="low : CVE--2025--1181" src="https://img.shields.io/badge/CVE--2025--1181-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.40-2</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.044%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>13th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A vulnerability classified as critical was found in GNU Binutils 2.43. This vulnerability affects the function _bfd_elf_gc_mark_rsec of the file bfd/elflink.c of the component ld. The manipulation leads to memory corruption. The attack can be initiated remotely. The complexity of an attack is rather high. The exploitation appears to be difficult. The exploit has been disclosed to the public and may be used. The name of the patch is 931494c9a89558acb36a03a340c01726545eef24. It is recommended to apply a patch to fix this issue.

---
- binutils <unfixed> (unimportant)
https://sourceware.org/bugzilla/show_bug.cgi?id=32643
https://sourceware.org/git/gitweb.cgi?p=binutils-gdb.git;h=931494c9a89558acb36a03a340c01726545eef24
binutils not covered by security support

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2025-1180?s=debian&n=binutils&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.40-2"><img alt="low : CVE--2025--1180" src="https://img.shields.io/badge/CVE--2025--1180-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.40-2</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.044%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>13th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A vulnerability classified as problematic has been found in GNU Binutils 2.43. This affects the function _bfd_elf_write_section_eh_frame of the file bfd/elf-eh-frame.c of the component ld. The manipulation leads to memory corruption. It is possible to initiate the attack remotely. The complexity of an attack is rather high. The exploitability is told to be difficult. The exploit has been disclosed to the public and may be used. It is recommended to apply a patch to fix this issue.

---
- binutils <unfixed> (unimportant)
https://sourceware.org/bugzilla/show_bug.cgi?id=32642
binutils not covered by security support

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2025-1179?s=debian&n=binutils&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.40-2"><img alt="low : CVE--2025--1179" src="https://img.shields.io/badge/CVE--2025--1179-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.40-2</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.073%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>35th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A vulnerability was found in GNU Binutils 2.43. It has been rated as critical. Affected by this issue is the function bfd_putl64 of the file bfd/libbfd.c of the component ld. The manipulation leads to memory corruption. The attack may be launched remotely. The complexity of an attack is rather high. The exploitation is known to be difficult. The exploit has been disclosed to the public and may be used. Upgrading to version 2.44 is able to address this issue. It is recommended to upgrade the affected component. The code maintainer explains, that "[t]his bug has been fixed at some point between the 2.43 and 2.44 releases".

---
- binutils 2.44-1 (unimportant)
https://sourceware.org/bugzilla/show_bug.cgi?id=32640
binutils not covered by security support
No exact commits pinpointed, but upstream confirms this fixed in 2.44

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2025-1178?s=debian&n=binutils&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.40-2"><img alt="low : CVE--2025--1178" src="https://img.shields.io/badge/CVE--2025--1178-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.40-2</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.044%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>13th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A vulnerability was found in GNU Binutils 2.43. It has been declared as problematic. Affected by this vulnerability is the function bfd_putl64 of the file libbfd.c of the component ld. The manipulation leads to memory corruption. The attack can be launched remotely. The complexity of an attack is rather high. The exploitation appears to be difficult. The exploit has been disclosed to the public and may be used. The identifier of the patch is 75086e9de1707281172cc77f178e7949a4414ed0. It is recommended to apply a patch to fix this issue.

---
- binutils <unfixed> (unimportant)
https://sourceware.org/bugzilla/show_bug.cgi?id=32638
https://sourceware.org/git/gitweb.cgi?p=binutils-gdb.git;h=75086e9de1707281172cc77f178e7949a4414ed0
binutils not covered by security support

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2025-1176?s=debian&n=binutils&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.40-2"><img alt="low : CVE--2025--1176" src="https://img.shields.io/badge/CVE--2025--1176-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.40-2</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.109%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>45th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A vulnerability was found in GNU Binutils 2.43 and classified as critical. This issue affects the function _bfd_elf_gc_mark_rsec of the file elflink.c of the component ld. The manipulation leads to heap-based buffer overflow. The attack may be initiated remotely. The complexity of an attack is rather high. The exploitation is known to be difficult. The exploit has been disclosed to the public and may be used. The patch is named f9978defb6fab0bd8583942d97c112b0932ac814. It is recommended to apply a patch to fix this issue.

---
- binutils <unfixed> (unimportant)
https://sourceware.org/bugzilla/show_bug.cgi?id=32636
https://sourceware.org/git/gitweb.cgi?p=binutils-gdb.git;h=f9978defb6fab0bd8583942d97c112b0932ac814
binutils not covered by security support

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2025-1153?s=debian&n=binutils&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.40-2"><img alt="low : CVE--2025--1153" src="https://img.shields.io/badge/CVE--2025--1153-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.40-2</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.060%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>28th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A vulnerability classified as problematic was found in GNU Binutils 2.43/2.44. Affected by this vulnerability is the function bfd_set_format of the file format.c. The manipulation leads to memory corruption. The attack can be launched remotely. The complexity of an attack is rather high. The exploitation appears to be difficult. Upgrading to version 2.45 is able to address this issue. The identifier of the patch is 8d97c1a53f3dc9fd8e1ccdb039b8a33d50133150. It is recommended to upgrade the affected component.

---
- binutils <unfixed> (unimportant)
https://sourceware.org/bugzilla/show_bug.cgi?id=32603
https://sourceware.org/git/gitweb.cgi?p=binutils-gdb.git;h=8d97c1a53f3dc9fd8e1ccdb039b8a33d50133150
binutils not covered by security support

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2025-1152?s=debian&n=binutils&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.40-2"><img alt="low : CVE--2025--1152" src="https://img.shields.io/badge/CVE--2025--1152-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.40-2</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.052%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>23rd percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A vulnerability classified as problematic has been found in GNU Binutils 2.43. Affected is the function xstrdup of the file xstrdup.c of the component ld. The manipulation leads to memory leak. It is possible to launch the attack remotely. The complexity of an attack is rather high. The exploitability is told to be difficult. The exploit has been disclosed to the public and may be used. It is recommended to apply a patch to fix this issue. The code maintainer explains: "I'm not going to commit some of the leak fixes I've been working on to the 2.44 branch due to concern that would destabilise ld. All of the reported leaks in this bugzilla have been fixed on binutils master."

---
- binutils <unfixed> (unimportant)
https://sourceware.org/bugzilla/show_bug.cgi?id=32576
binutils not covered by security support

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2025-1151?s=debian&n=binutils&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.40-2"><img alt="low : CVE--2025--1151" src="https://img.shields.io/badge/CVE--2025--1151-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.40-2</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.052%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>23rd percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A vulnerability was found in GNU Binutils 2.43. It has been rated as problematic. This issue affects the function xmemdup of the file xmemdup.c of the component ld. The manipulation leads to memory leak. The attack may be initiated remotely. The complexity of an attack is rather high. The exploitation is known to be difficult. The exploit has been disclosed to the public and may be used. It is recommended to apply a patch to fix this issue. The code maintainer explains: "I'm not going to commit some of the leak fixes I've been working on to the 2.44 branch due to concern that would destabilise ld. All of the reported leaks in this bugzilla have been fixed on binutils master."

---
- binutils <unfixed> (unimportant)
https://sourceware.org/bugzilla/show_bug.cgi?id=32576
binutils not covered by security support

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2025-1150?s=debian&n=binutils&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.40-2"><img alt="low : CVE--2025--1150" src="https://img.shields.io/badge/CVE--2025--1150-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.40-2</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.052%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>23rd percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A vulnerability was found in GNU Binutils 2.43. It has been declared as problematic. This vulnerability affects the function bfd_malloc of the file libbfd.c of the component ld. The manipulation leads to memory leak. The attack can be initiated remotely. The complexity of an attack is rather high. The exploitation appears to be difficult. The exploit has been disclosed to the public and may be used. It is recommended to apply a patch to fix this issue. The code maintainer explains: "I'm not going to commit some of the leak fixes I've been working on to the 2.44 branch due to concern that would destabilise ld. All of the reported leaks in this bugzilla have been fixed on binutils master."

---
- binutils <unfixed> (unimportant)
https://sourceware.org/bugzilla/show_bug.cgi?id=32576
binutils not covered by security support

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2025-1149?s=debian&n=binutils&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.40-2"><img alt="low : CVE--2025--1149" src="https://img.shields.io/badge/CVE--2025--1149-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.40-2</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.052%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>23rd percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A vulnerability was found in GNU Binutils 2.43. It has been classified as problematic. This affects the function xstrdup of the file libiberty/xmalloc.c of the component ld. The manipulation leads to memory leak. It is possible to initiate the attack remotely. The complexity of an attack is rather high. The exploitability is told to be difficult. The exploit has been disclosed to the public and may be used. It is recommended to apply a patch to fix this issue. The code maintainer explains: "I'm not going to commit some of the leak fixes I've been working on to the 2.44 branch due to concern that would destabilise ld. All of the reported leaks in this bugzilla have been fixed on binutils master."

---
- binutils <unfixed> (unimportant)
https://sourceware.org/bugzilla/show_bug.cgi?id=32576
binutils not covered by security support

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2025-1148?s=debian&n=binutils&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.40-2"><img alt="low : CVE--2025--1148" src="https://img.shields.io/badge/CVE--2025--1148-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.40-2</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.060%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>28th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A vulnerability was found in GNU Binutils 2.43 and classified as problematic. Affected by this issue is the function link_order_scan of the file ld/ldelfgen.c of the component ld. The manipulation leads to memory leak. The attack may be launched remotely. The complexity of an attack is rather high. The exploitation is known to be difficult. The exploit has been disclosed to the public and may be used. It is recommended to apply a patch to fix this issue. The code maintainer explains: "I'm not going to commit some of the leak fixes I've been working on to the 2.44 branch due to concern that would destabilise ld. All of the reported leaks in this bugzilla have been fixed on binutils master."

---
- binutils <unfixed> (unimportant)
https://sourceware.org/bugzilla/show_bug.cgi?id=32576
binutils not covered by security support

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2025-1147?s=debian&n=binutils&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.40-2"><img alt="low : CVE--2025--1147" src="https://img.shields.io/badge/CVE--2025--1147-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.40-2</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.060%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>28th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A vulnerability has been found in GNU Binutils 2.43 and classified as problematic. Affected by this vulnerability is the function __sanitizer::internal_strlen of the file binutils/nm.c of the component nm. The manipulation of the argument const leads to buffer overflow. The attack can be launched remotely. The complexity of an attack is rather high. The exploitation appears to be difficult. The exploit has been disclosed to the public and may be used.

---
- binutils <unfixed> (unimportant)
https://sourceware.org/bugzilla/show_bug.cgi?id=32556
binutils not covered by security support

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2025-0840?s=debian&n=binutils&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.40-2"><img alt="low : CVE--2025--0840" src="https://img.shields.io/badge/CVE--2025--0840-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.40-2</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.073%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>35th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A vulnerability, which was classified as problematic, was found in GNU Binutils up to 2.43. This affects the function disassemble_bytes of the file binutils/objdump.c. The manipulation of the argument buf leads to stack-based buffer overflow. It is possible to initiate the attack remotely. The complexity of an attack is rather high. The exploitability is told to be difficult. The exploit has been disclosed to the public and may be used. Upgrading to version 2.44 is able to address this issue. The identifier of the patch is baac6c221e9d69335bf41366a1c7d87d8ab2f893. It is recommended to upgrade the affected component.

---
- binutils 2.43.90.20250122-1 (unimportant)
https://sourceware.org/bugzilla/show_bug.cgi?id=32560
https://sourceware.org/git/gitweb.cgi?p=binutils-gdb.git;h=baac6c221e9d69335bf41366a1c7d87d8ab2f893
binutils not covered by security support

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2024-57360?s=debian&n=binutils&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.40-2"><img alt="low : CVE--2024--57360" src="https://img.shields.io/badge/CVE--2024--57360-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.40-2</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.043%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>12th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

https://www.gnu.org/software/binutils/ nm >=2.43 is affected by: Incorrect Access Control. The type of exploitation is: local. The component is: `nm --without-symbol-version` function.

---
- binutils 2.43.50.20241221-1 (unimportant)
https://sourceware.org/bugzilla/show_bug.cgi?id=32467
Fixed by: https://sourceware.org/git/gitweb.cgi?p=binutils-gdb.git;h=5f8987d3999edb26e757115fe87be55787d510b9
binutils not covered by security support

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2024-53589?s=debian&n=binutils&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.40-2"><img alt="low : CVE--2024--53589" src="https://img.shields.io/badge/CVE--2024--53589-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.40-2</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.043%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>12th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

GNU objdump 2.43 is vulnerable to Buffer Overflow in the BFD (Binary File Descriptor) library's handling of tekhex format files.

---
- binutils 2.44-1 (unimportant)
https://bushido-sec.com/index.php/2024/12/05/binutils-objdump-tekhex-buffer-overflow/
https://sourceware.org/git/gitweb.cgi?p=binutils-gdb.git;h=e0323071916878e0634a6e24d8250e4faff67e88 (binutils-2_44)
binutils not covered by security support

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2023-1972?s=debian&n=binutils&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.40-2"><img alt="low : CVE--2023--1972" src="https://img.shields.io/badge/CVE--2023--1972-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.40-2</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.121%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>48th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A potential heap based buffer overflow was found in _bfd_elf_slurp_version_tables() in bfd/elf.c. This may lead to loss of availability.

---
- binutils 2.41-1 (unimportant)
https://sourceware.org/git/?p=binutils-gdb.git;a=blobdiff;f=bfd/elf.c;h=185028cbd97ae0901c4276c8a4787b12bb75875a;hp=027d01437352555bc4ac0717cb0486c751a7775d;hb=c22d38baefc5a7a1e1f5cdc9dbb556b1f0ec5c57;hpb=f2f9bde5cde7ff34ed0a4c4682a211d402aa1086
https://sourceware.org/bugzilla/show_bug.cgi?id=30285
binutils not covered by security support

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2021-32256?s=debian&n=binutils&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.40-2"><img alt="low : CVE--2021--32256" src="https://img.shields.io/badge/CVE--2021--32256-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.40-2</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.110%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>46th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

An issue was discovered in GNU libiberty, as distributed in GNU Binutils 2.36. It is a stack-overflow issue in demangle_type in rust-demangle.c.

---
- binutils <unfixed> (unimportant)
https://bugs.launchpad.net/ubuntu/+source/binutils/+bug/1927070
binutils not covered by security support

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2018-9996?s=debian&n=binutils&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.40-2"><img alt="low : CVE--2018--9996" src="https://img.shields.io/badge/CVE--2018--9996-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.40-2</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.046%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>19th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

An issue was discovered in cplus-dem.c in GNU libiberty, as distributed in GNU Binutils 2.30. Stack Exhaustion occurs in the C++ demangling functions provided by libiberty, and there are recursive stack frames: demangle_template_value_parm, demangle_integral_value, and demangle_expression.

---
- binutils <unfixed> (unimportant)
https://gcc.gnu.org/bugzilla/show_bug.cgi?id=85304
binutils not covered by security support

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2018-20712?s=debian&n=binutils&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.40-2"><img alt="low : CVE--2018--20712" src="https://img.shields.io/badge/CVE--2018--20712-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.40-2</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.163%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>54th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A heap-based buffer over-read exists in the function d_expression_1 in cp-demangle.c in GNU libiberty, as distributed in GNU Binutils 2.31.1. A crafted input can cause segmentation faults, leading to denial-of-service, as demonstrated by c++filt.

---
- binutils <unfixed> (unimportant)
https://gcc.gnu.org/bugzilla/show_bug.cgi?id=88629
https://sourceware.org/bugzilla/show_bug.cgi?id=24043
binutils not covered by security support

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2018-20673?s=debian&n=binutils&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.40-2"><img alt="low : CVE--2018--20673" src="https://img.shields.io/badge/CVE--2018--20673-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.40-2</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.045%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>18th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

The demangle_template function in cplus-dem.c in GNU libiberty, as distributed in GNU Binutils 2.31.1, contains an integer overflow vulnerability (for "Create an array for saving the template argument values") that can trigger a heap-based buffer overflow, as demonstrated by nm.

---
- binutils <unfixed> (unimportant)
https://sourceware.org/bugzilla/show_bug.cgi?id=24039
binutils not covered by security support

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2017-13716?s=debian&n=binutils&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.40-2"><img alt="low : CVE--2017--13716" src="https://img.shields.io/badge/CVE--2017--13716-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.40-2</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.106%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>45th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

The C++ symbol demangler routine in cplus-dem.c in libiberty, as distributed in GNU Binutils 2.29, allows remote attackers to cause a denial of service (excessive memory allocation and application crash) via a crafted file, as demonstrated by a call from the Binary File Descriptor (BFD) library (aka libbfd).

---
- binutils <unfixed> (unimportant)
https://sourceware.org/bugzilla/show_bug.cgi?id=22009
Underlying bug is though in the C++ demangler part of libiberty, but MITRE
has assigned it specifically to the issue as raised within binutils.
binutils not covered by security support

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 7" src="https://img.shields.io/badge/L-7-fce1a9"/> <!-- unspecified: 0 --><strong>elfutils</strong> <code>0.188-2.1</code> (deb)</summary>

<small><code>pkg:deb/debian/elfutils@0.188-2.1?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2025-1377?s=debian&n=elfutils&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D0.188-2.1"><img alt="low : CVE--2025--1377" src="https://img.shields.io/badge/CVE--2025--1377-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=0.188-2.1</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.044%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>13th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A vulnerability, which was classified as problematic, has been found in GNU elfutils 0.192. This issue affects the function gelf_getsymshndx of the file strip.c of the component eu-strip. The manipulation leads to denial of service. The attack needs to be approached locally. The exploit has been disclosed to the public and may be used. The identifier of the patch is fbf1df9ca286de3323ae541973b08449f8d03aba. It is recommended to apply a patch to fix this issue.

---
- elfutils <unfixed> (unimportant)
https://sourceware.org/bugzilla/show_bug.cgi?id=32673
https://sourceware.org/git/?p=elfutils.git;a=fbf1df9ca286de3323ae541973b08449f8d03aba
Crash in CLI tool, considered only to be a normal bug by upstream

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2025-1376?s=debian&n=elfutils&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D0.188-2.1"><img alt="low : CVE--2025--1376" src="https://img.shields.io/badge/CVE--2025--1376-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=0.188-2.1</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.044%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>13th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A vulnerability classified as problematic was found in GNU elfutils 0.192. This vulnerability affects the function elf_strptr in the library /libelf/elf_strptr.c of the component eu-strip. The manipulation leads to denial of service. It is possible to launch the attack on the local host. The complexity of an attack is rather high. The exploitation appears to be difficult. The exploit has been disclosed to the public and may be used. The name of the patch is b16f441cca0a4841050e3215a9f120a6d8aea918. It is recommended to apply a patch to fix this issue.

---
- elfutils <unfixed> (unimportant)
https://sourceware.org/bugzilla/show_bug.cgi?id=32672
https://sourceware.org/git/?p=elfutils.git;a=commit;h=b16f441cca0a4841050e3215a9f120a6d8aea918
Crash in CLI tool, considered only to be a normal bug by upstream

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2025-1372?s=debian&n=elfutils&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D0.188-2.1"><img alt="low : CVE--2025--1372" src="https://img.shields.io/badge/CVE--2025--1372-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=0.188-2.1</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.044%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>16th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A vulnerability was found in GNU elfutils 0.192. It has been declared as critical. Affected by this vulnerability is the function dump_data_section/print_string_section of the file readelf.c of the component eu-readelf. The manipulation of the argument z/x leads to buffer overflow. An attack has to be approached locally. The exploit has been disclosed to the public and may be used. The identifier of the patch is 73db9d2021cab9e23fd734b0a76a612d52a6f1db. It is recommended to apply a patch to fix this issue.

---
- elfutils <unfixed> (unimportant)
https://sourceware.org/bugzilla/show_bug.cgi?id=32656
https://sourceware.org/bugzilla/show_bug.cgi?id=32657
https://sourceware.org/git/?p=elfutils.git;a=commit;h=73db9d2021cab9e23fd734b0a76a612d52a6f1db
Crash in CLI tool, considered only to be a normal bug by upstream

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2025-1371?s=debian&n=elfutils&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D0.188-2.1"><img alt="low : CVE--2025--1371" src="https://img.shields.io/badge/CVE--2025--1371-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=0.188-2.1</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.044%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>13th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A vulnerability has been found in GNU elfutils 0.192 and classified as problematic. This vulnerability affects the function handle_dynamic_symtab of the file readelf.c of the component eu-read. The manipulation leads to null pointer dereference. Attacking locally is a requirement. The exploit has been disclosed to the public and may be used. The patch is identified as b38e562a4c907e08171c76b8b2def8464d5a104a. It is recommended to apply a patch to fix this issue.

---
- elfutils <unfixed> (unimportant)
https://sourceware.org/bugzilla/show_bug.cgi?id=32655
https://sourceware.org/git/?p=elfutils.git;a=commit;h=b38e562a4c907e08171c76b8b2def8464d5a104a
Crash in CLI tool, considered only to be a normal bug by upstream

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2025-1365?s=debian&n=elfutils&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D0.188-2.1"><img alt="low : CVE--2025--1365" src="https://img.shields.io/badge/CVE--2025--1365-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=0.188-2.1</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.044%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>13th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A vulnerability, which was classified as critical, was found in GNU elfutils 0.192. This affects the function process_symtab of the file readelf.c of the component eu-readelf. The manipulation of the argument D/a leads to buffer overflow. Local access is required to approach this attack. The exploit has been disclosed to the public and may be used. The identifier of the patch is 5e5c0394d82c53e97750fe7b18023e6f84157b81. It is recommended to apply a patch to fix this issue.

---
- elfutils <unfixed> (unimportant)
https://sourceware.org/bugzilla/show_bug.cgi?id=32654
https://sourceware.org/git/?p=elfutils.git;a=commit;h=5e5c0394d82c53e97750fe7b18023e6f84157b81
Crash in CLI tool, considered only to be a normal bug by upstream

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2025-1352?s=debian&n=elfutils&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D0.188-2.1"><img alt="low : CVE--2025--1352" src="https://img.shields.io/badge/CVE--2025--1352-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=0.188-2.1</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.073%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>35th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A vulnerability has been found in GNU elfutils 0.192 and classified as critical. This vulnerability affects the function __libdw_thread_tail in the library libdw_alloc.c of the component eu-readelf. The manipulation of the argument w leads to memory corruption. The attack can be initiated remotely. The complexity of an attack is rather high. The exploitation appears to be difficult. The exploit has been disclosed to the public and may be used. The name of the patch is 2636426a091bd6c6f7f02e49ab20d4cdc6bfc753. It is recommended to apply a patch to fix this issue.

---
- elfutils <unfixed> (unimportant)
https://sourceware.org/bugzilla/show_bug.cgi?id=32650
Fixed by: https://sourceware.org/git/?p=elfutils.git;a=2636426a091bd6c6f7f02e49ab20d4cdc6bfc753
Crash in CLI tool, considered only to be a normal bug by upstream

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2024-25260?s=debian&n=elfutils&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D0.188-2.1"><img alt="low : CVE--2024--25260" src="https://img.shields.io/badge/CVE--2024--25260-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=0.188-2.1</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.045%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>18th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

elfutils v0.189 was discovered to contain a NULL pointer dereference via the handle_verdef() function at readelf.c.

---
- elfutils <unfixed> (unimportant)
https://sourceware.org/bugzilla/show_bug.cgi?id=31058
https://sourceware.org/git/?p=elfutils.git;a=commit;h=373f5212677235fc3ca6068b887111554790f944
Crash in CLI tool, considered only to be a normal bug by upstream

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 4" src="https://img.shields.io/badge/L-4-fce1a9"/> <!-- unspecified: 0 --><strong>openldap</strong> <code>2.5.13+dfsg-5</code> (deb)</summary>

<small><code>pkg:deb/debian/openldap@2.5.13%2Bdfsg-5?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2020-15719?s=debian&n=openldap&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.5.13%2Bdfsg-5"><img alt="low : CVE--2020--15719" src="https://img.shields.io/badge/CVE--2020--15719-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.5.13+dfsg-5</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.160%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>54th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

libldap in certain third-party OpenLDAP packages has a certificate-validation flaw when the third-party package is asserting RFC6125 support. It considers CN even when there is a non-matching subjectAltName (SAN). This is fixed in, for example, openldap-2.4.46-10.el8 in Red Hat Enterprise Linux.

---
- openldap <unfixed> (unimportant; bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=965184)
https://bugs.openldap.org/show_bug.cgi?id=9266
https://bugzilla.redhat.com/show_bug.cgi?id=1740070
RedHat/CentOS applied patch: https://git.centos.org/rpms/openldap/raw/67459960064be9d226d57c5f82aaba0929876813/f/SOURCES/openldap-tlso-dont-check-cn-when-bad-san.patch
OpenLDAP upstream did dispute the issue as beeing valid, as the current libldap
behaviour does conform with RFC4513. RFC6125 does not superseed the rules for
verifying service identity provided in specifications for existing application
protocols published prior to RFC6125, like RFC4513 for LDAP.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2017-17740?s=debian&n=openldap&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.5.13%2Bdfsg-5"><img alt="low : CVE--2017--17740" src="https://img.shields.io/badge/CVE--2017--17740-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.5.13+dfsg-5</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.492%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>76th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

contrib/slapd-modules/nops/nops.c in OpenLDAP through 2.4.45, when both the nops module and the memberof overlay are enabled, attempts to free a buffer that was allocated on the stack, which allows remote attackers to cause a denial of service (slapd crash) via a member MODDN operation.

---
- openldap <unfixed> (unimportant)
http://www.openldap.org/its/index.cgi/Incoming?id=8759
nops slapd-module not built

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2017-14159?s=debian&n=openldap&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.5.13%2Bdfsg-5"><img alt="low : CVE--2017--14159" src="https://img.shields.io/badge/CVE--2017--14159-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.5.13+dfsg-5</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.051%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>23rd percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

slapd in OpenLDAP 2.4.45 and earlier creates a PID file after dropping privileges to a non-root account, which might allow local users to kill arbitrary processes by leveraging access to this non-root account for PID file modification before a root script executes a "kill `cat /pathname`" command, as demonstrated by openldap-initscript.

---
- openldap <unfixed> (unimportant)
http://www.openldap.org/its/index.cgi?findid=8703
Negligible security impact, but filed #877512

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2015-3276?s=debian&n=openldap&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.5.13%2Bdfsg-5"><img alt="low : CVE--2015--3276" src="https://img.shields.io/badge/CVE--2015--3276-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.5.13+dfsg-5</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.299%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>69th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

The nss_parse_ciphers function in libraries/libldap/tls_m.c in OpenLDAP does not properly parse OpenSSL-style multi-keyword mode cipher strings, which might cause a weaker than intended cipher to be used and allow remote attackers to have unspecified impact via unknown vectors.

---
- openldap <unfixed> (unimportant)
Debian builds with GNUTLS, not NSS

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 4" src="https://img.shields.io/badge/L-4-fce1a9"/> <!-- unspecified: 0 --><strong>patch</strong> <code>2.7.6-7</code> (deb)</summary>

<small><code>pkg:deb/debian/patch@2.7.6-7?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2021-45261?s=debian&n=patch&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.7.6-7"><img alt="low : CVE--2021--45261" src="https://img.shields.io/badge/CVE--2021--45261-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.7.6-7</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.065%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>31st percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

An Invalid Pointer vulnerability exists in GNU patch 2.7 via the another_hunk function, which causes a Denial of Service.

---
- patch <unfixed> (unimportant)
https://savannah.gnu.org/bugs/?61685
Negligible security impact

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2018-6952?s=debian&n=patch&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.7.6-7"><img alt="low : CVE--2018--6952" src="https://img.shields.io/badge/CVE--2018--6952-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.7.6-7</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>1.737%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>88th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A double free exists in the another_hunk function in pch.c in GNU patch through 2.7.6.

---
- patch <unfixed> (unimportant)
https://savannah.gnu.org/bugs/index.php?53133
https://git.savannah.gnu.org/cgit/patch.git/commit/?id=9c986353e420ead6e706262bf204d6e03322c300
When fixing this issue make sure to not apply only the incomplete fix,
and opening CVE-2019-20633, cf. https://savannah.gnu.org/bugs/index.php?56683
Crash in CLI tool, no security impact

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2018-6951?s=debian&n=patch&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.7.6-7"><img alt="low : CVE--2018--6951" src="https://img.shields.io/badge/CVE--2018--6951-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.7.6-7</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.925%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>83rd percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

An issue was discovered in GNU patch through 2.7.6. There is a segmentation fault, associated with a NULL pointer dereference, leading to a denial of service in the intuit_diff_type function in pch.c, aka a "mangled rename" issue.

---
- patch <unfixed> (unimportant)
https://git.savannah.gnu.org/cgit/patch.git/commit/?id=f290f48a621867084884bfff87f8093c15195e6a
https://savannah.gnu.org/bugs/index.php?53132
Crash in CLI tool, no security impact

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2010-4651?s=debian&n=patch&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.7.6-7"><img alt="low : CVE--2010--4651" src="https://img.shields.io/badge/CVE--2010--4651-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.7.6-7</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.577%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>78th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

Directory traversal vulnerability in util.c in GNU patch 2.6.1 and earlier allows user-assisted remote attackers to create or overwrite arbitrary files via a filename that is specified with a .. (dot dot) or full pathname, a related issue to CVE-2010-1679.

---
- patch <unfixed> (unimportant)
Applying a patch blindly opens more severe security issues than only directory traversal...
openwall ships a fix
See https://bugzilla.redhat.com/show_bug.cgi?id=667529 for details

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 2" src="https://img.shields.io/badge/L-2-fce1a9"/> <!-- unspecified: 0 --><strong>gcc-12</strong> <code>12.2.0-14</code> (deb)</summary>

<small><code>pkg:deb/debian/gcc-12@12.2.0-14?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2023-4039?s=debian&n=gcc-12&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D12.2.0-14"><img alt="low : CVE--2023--4039" src="https://img.shields.io/badge/CVE--2023--4039-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=12.2.0-14</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.071%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>34th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

**DISPUTED**A failure in the -fstack-protector feature in GCC-based toolchains  that target AArch64 allows an attacker to exploit an existing buffer  overflow in dynamically-sized local variables in your application  without this being detected. This stack-protector failure only applies  to C99-style dynamically-sized local variables or those created using  alloca(). The stack-protector operates as intended for statically-sized  local variables.  The default behavior when the stack-protector  detects an overflow is to terminate your application, resulting in  controlled loss of availability. An attacker who can exploit a buffer  overflow without triggering the stack-protector might be able to change  program flow control to cause an uncontrolled loss of availability or to  go further and affect confidentiality or integrity. NOTE: The GCC project argues that this is a missed hardening bug and not a vulnerability by itself.

---
- gcc-13 13.2.0-4 (unimportant)
- gcc-12 12.3.0-9 (unimportant)
- gcc-11 11.4.0-4 (unimportant)
- gcc-10 10.5.0-3 (unimportant)
- gcc-9 9.5.0-6 (unimportant)
- gcc-8 <removed> (unimportant)
- gcc-7 <removed> (unimportant)
https://github.com/metaredteam/external-disclosures/security/advisories/GHSA-x7ch-h5rf-w2mf
Not considered a security issue by GCC upstream
https://developer.arm.com/Arm%20Security%20Center/GCC%20Stack%20Protector%20Vulnerability%20AArch64

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2022-27943?s=debian&n=gcc-12&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D12.2.0-14"><img alt="low : CVE--2022--27943" src="https://img.shields.io/badge/CVE--2022--27943-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=12.2.0-14</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.101%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>43rd percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

libiberty/rust-demangle.c in GNU GCC 11.2 allows stack consumption in demangle_const, as demonstrated by nm-new.

---
- gcc-12 <unfixed> (unimportant)
Negligible security impact
https://gcc.gnu.org/bugzilla/show_bug.cgi?id=105039

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 2" src="https://img.shields.io/badge/L-2-fce1a9"/> <!-- unspecified: 0 --><strong>m4</strong> <code>1.4.19-3</code> (deb)</summary>

<small><code>pkg:deb/debian/m4@1.4.19-3?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2008-1688?s=debian&n=m4&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D1.4.19-3"><img alt="low : CVE--2008--1688" src="https://img.shields.io/badge/CVE--2008--1688-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=1.4.19-3</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>1.582%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>87th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

Unspecified vulnerability in GNU m4 before 1.4.11 might allow context-dependent attackers to execute arbitrary code, related to improper handling of filenames specified with the -F option.  NOTE: it is not clear when this issue crosses privilege boundaries.

---
- m4 <unfixed> (unimportant)
The file name is passed through a cmdline argument and m4 doesn't run with
elevated privileges.

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2008-1687?s=debian&n=m4&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D1.4.19-3"><img alt="low : CVE--2008--1687" src="https://img.shields.io/badge/CVE--2008--1687-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=1.4.19-3</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>1.119%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>85th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

The (1) maketemp and (2) mkstemp builtin functions in GNU m4 before 1.4.11 do not quote their output when a file is created, which might allow context-dependent attackers to trigger a macro expansion, leading to unspecified use of an incorrect filename.

---
- m4 <unfixed> (unimportant)
This is more a generic bug and not a security issue: the random output would
need to match the name of an existing macro

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 1" src="https://img.shields.io/badge/L-1-fce1a9"/> <img alt="unspecified: 1" src="https://img.shields.io/badge/U-1-lightgrey"/><strong>libwebp</strong> <code>1.2.4-0.2</code> (deb)</summary>

<small><code>pkg:deb/debian/libwebp@1.2.4-0.2?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2023-4863?s=debian&n=libwebp&ns=debian&t=deb&osn=debian&osv=12&vr=%3C1.2.4-0.2%2Bdeb12u1"><img alt="low : CVE--2023--4863" src="https://img.shields.io/badge/CVE--2023--4863-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code><1.2.4-0.2+deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><code>1.2.4-0.2+deb12u1</code></td></tr>
<tr><td>EPSS Score</td><td><code>42.776%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>97th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

Heap buffer overflow in libwebp in Google Chrome prior to 116.0.5845.187 and libwebp 1.3.2 allowed a remote attacker to perform an out of bounds memory write via a crafted HTML page. (Chromium security severity: Critical)

---
- chromium 117.0.5938.62-1 (unimportant)
[buster] - chromium <end-of-life> (see DSA 5046)
- firefox 117.0.1-1
- firefox-esr 115.2.1esr-1
- thunderbird 1:115.2.2-1
- libwebp 1.2.4-0.3 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1051787)
https://chromereleases.googleblog.com/2023/09/stable-channel-update-for-desktop_11.html
src:chromium builds against the system libwebp library
Fixed by: https://chromium.googlesource.com/webm/libwebp.git/+/902bc9190331343b2017211debcec8d2ab87e17a%5E%21/
Followup: https://chromium.googlesource.com/webm/libwebp.git/+/95ea5226c870449522240ccff26f0b006037c520%5E%21/#F0
https://www.mozilla.org/en-US/security/advisories/mfsa2023-40/#CVE-2023-4863

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2023-5129?s=debian&n=libwebp&ns=debian&t=deb&osn=debian&osv=12&vr=%3C1.2.4-0.2%2Bdeb12u1"><img alt="unspecified : CVE--2023--5129" src="https://img.shields.io/badge/CVE--2023--5129-lightgrey?label=unspecified%20&labelColor=lightgrey"/></a> 

<table>
<tr><td>Affected range</td><td><code><1.2.4-0.2+deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><code>1.2.4-0.2+deb12u1</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.043%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>12th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

With a specially crafted WebP lossless file, libwebp may write data out of bounds to the heap.

The ReadHuffmanCodes() function allocates the HuffmanCode buffer with a size that comes from an array of precomputed sizes: kTableSize. The color_cache_bits value defines which size to use.

The kTableSize array only takes into account sizes for 8-bit first-level table lookups but not second-level table lookups. libwebp allows codes that are up to 15-bit (MAX_ALLOWED_CODE_LENGTH). When BuildHuffmanTable() attempts to fill the second-level tables it may write data out-of-bounds. The OOB write to the undersized array happens in ReplicateValue.



---
REJECTED

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 1" src="https://img.shields.io/badge/L-1-fce1a9"/> <!-- unspecified: 0 --><strong>jansson</strong> <code>2.14-2</code> (deb)</summary>

<small><code>pkg:deb/debian/jansson@2.14-2?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2020-36325?s=debian&n=jansson&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.14-2"><img alt="low : CVE--2020--36325" src="https://img.shields.io/badge/CVE--2020--36325-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.14-2</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.170%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>55th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

An issue was discovered in Jansson through 2.13.1. Due to a parsing error in json_loads, there's an out-of-bounds read-access bug. NOTE: the vendor reports that this only occurs when a programmer fails to follow the API specification

---
- jansson <unfixed> (unimportant)
https://github.com/akheron/jansson/issues/548
Disputed security impact (only if programmer fails to follow API specifications)

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 1" src="https://img.shields.io/badge/L-1-fce1a9"/> <!-- unspecified: 0 --><strong>jbigkit</strong> <code>2.1-6.1</code> (deb)</summary>

<small><code>pkg:deb/debian/jbigkit@2.1-6.1?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2017-9937?s=debian&n=jbigkit&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.1-6.1"><img alt="low : CVE--2017--9937" src="https://img.shields.io/badge/CVE--2017--9937-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.1-6.1</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.125%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>48th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

In LibTIFF 4.0.8, there is a memory malloc failure in tif_jbig.c. A crafted TIFF document can lead to an abort resulting in a remote denial of service attack.

---
- jbigkit <unfixed> (unimportant; bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=869708)
http://bugzilla.maptools.org/show_bug.cgi?id=2707
The CVE was assigned for src:tiff by MITRE, but the issue actually lies
in jbigkit itself.

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 1" src="https://img.shields.io/badge/L-1-fce1a9"/> <!-- unspecified: 0 --><strong>gnupg2</strong> <code>2.2.40-1.1</code> (deb)</summary>

<small><code>pkg:deb/debian/gnupg2@2.2.40-1.1?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2022-3219?s=debian&n=gnupg2&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.2.40-1.1"><img alt="low : CVE--2022--3219" src="https://img.shields.io/badge/CVE--2022--3219-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.2.40-1.1</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.046%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>20th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

GnuPG can be made to spin on a relatively small input by (for example) crafting a public key with thousands of signatures attached, compressed down to just a few KB.

---
- gnupg2 <unfixed> (unimportant)
https://bugzilla.redhat.com/show_bug.cgi?id=2127010
https://dev.gnupg.org/D556
https://dev.gnupg.org/T5993
https://www.openwall.com/lists/oss-security/2022/07/04/8
GnuPG upstream is not implementing this change.

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 1" src="https://img.shields.io/badge/L-1-fce1a9"/> <!-- unspecified: 0 --><strong>unzip</strong> <code>6.0-28</code> (deb)</summary>

<small><code>pkg:deb/debian/unzip@6.0-28?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2021-4217?s=debian&n=unzip&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D6.0-28"><img alt="low : CVE--2021--4217" src="https://img.shields.io/badge/CVE--2021--4217-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=6.0-28</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.112%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>46th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A flaw was found in unzip. The vulnerability occurs due to improper handling of Unicode strings, which can lead to a null pointer dereference. This flaw allows an attacker to input a specially crafted zip file, leading to a crash or code execution.

---
- unzip <unfixed> (unimportant)
https://bugzilla.redhat.com/show_bug.cgi?id=2044583
https://bugs.launchpad.net/ubuntu/+source/unzip/+bug/1957077
Crash in CLI tool, no security impact

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 1" src="https://img.shields.io/badge/L-1-fce1a9"/> <!-- unspecified: 0 --><strong>libgcrypt20</strong> <code>1.10.1-3</code> (deb)</summary>

<small><code>pkg:deb/debian/libgcrypt20@1.10.1-3?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2018-6829?s=debian&n=libgcrypt20&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D1.10.1-3"><img alt="low : CVE--2018--6829" src="https://img.shields.io/badge/CVE--2018--6829-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=1.10.1-3</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.329%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>71st percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

cipher/elgamal.c in Libgcrypt through 1.8.2, when used to encrypt messages directly, improperly encodes plaintexts, which allows attackers to obtain sensitive information by reading ciphertext data (i.e., it does not have semantic security in face of a ciphertext-only attack). The Decisional Diffie-Hellman (DDH) assumption does not hold for Libgcrypt's ElGamal implementation.

---
- libgcrypt20 <unfixed> (unimportant)
- libgcrypt11 <removed> (unimportant)
- gnupg1 <unfixed> (unimportant)
- gnupg <removed> (unimportant)
https://github.com/weikengchen/attack-on-libgcrypt-elgamal
https://github.com/weikengchen/attack-on-libgcrypt-elgamal/wiki
https://lists.gnupg.org/pipermail/gcrypt-devel/2018-February/004394.html
GnuPG uses ElGamal in hybrid mode only.
This is not a vulnerability in libgcrypt, but in an application using
it in an insecure manner, see also
https://lists.gnupg.org/pipermail/gcrypt-devel/2018-February/004401.html

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 1" src="https://img.shields.io/badge/L-1-fce1a9"/> <!-- unspecified: 0 --><strong>util-linux</strong> <code>2.38.1-5+b1</code> (deb)</summary>

<small><code>pkg:deb/debian/util-linux@2.38.1-5%2Bb1?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2024-28085?s=debian&n=util-linux&ns=debian&t=deb&osn=debian&osv=12&vr=%3C2.38.1-5%2Bdeb12u1"><img alt="low : CVE--2024--28085" src="https://img.shields.io/badge/CVE--2024--28085-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code><2.38.1-5+deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><code>2.38.1-5+deb12u1</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.046%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>20th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

wall in util-linux through 2.40, often installed with setgid tty permissions, allows escape sequences to be sent to other users' terminals through argv. (Specifically, escape sequences received from stdin are blocked, but escape sequences received from argv are not blocked.) There may be plausible scenarios where this leads to account takeover.

---
- util-linux 2.39.3-11 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1067849)
https://www.openwall.com/lists/oss-security/2024/03/27/5
https://github.com/util-linux/util-linux/commit/404b0781f52f7c045ca811b2dceec526408ac253 (v2.40)

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 1" src="https://img.shields.io/badge/L-1-fce1a9"/> <!-- unspecified: 0 --><strong>libxslt</strong> <code>1.1.35-1</code> (deb)</summary>

<small><code>pkg:deb/debian/libxslt@1.1.35-1?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2015-9019?s=debian&n=libxslt&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D1.1.35-1"><img alt="low : CVE--2015--9019" src="https://img.shields.io/badge/CVE--2015--9019-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=1.1.35-1</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.060%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>28th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

In libxslt 1.1.29 and earlier, the EXSLT math.random function was not initialized with a random seed during startup, which could cause usage of this function to produce predictable outputs.

---
- libxslt <unfixed> (unimportant; bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=859796)
https://bugzilla.gnome.org/show_bug.cgi?id=758400
https://bugzilla.suse.com/show_bug.cgi?id=934119
There's no indication that math.random() in intended to ensure cryptographic
randomness requirements. Proper seeding needs to happen in the application
using libxslt.

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 1" src="https://img.shields.io/badge/L-1-fce1a9"/> <!-- unspecified: 0 --><strong>apt</strong> <code>2.6.1</code> (deb)</summary>

<small><code>pkg:deb/debian/apt@2.6.1?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2011-3374?s=debian&n=apt&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D2.6.1"><img alt="low : CVE--2011--3374" src="https://img.shields.io/badge/CVE--2011--3374-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=2.6.1</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.307%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>70th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

It was found that apt-key in apt, all versions, do not correctly validate gpg keys with the master keyring, leading to a potential man-in-the-middle attack.

---
- apt <unfixed> (unimportant; bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=642480)
Not exploitable in Debian, since no keyring URI is defined

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 1" src="https://img.shields.io/badge/L-1-fce1a9"/> <!-- unspecified: 0 --><strong>coreutils</strong> <code>9.1-1</code> (deb)</summary>

<small><code>pkg:deb/debian/coreutils@9.1-1?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2017-18018?s=debian&n=coreutils&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D9.1-1"><img alt="low : CVE--2017--18018" src="https://img.shields.io/badge/CVE--2017--18018-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=9.1-1</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.042%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>5th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

In GNU Coreutils through 8.29, chown-core.c in chown and chgrp does not prevent replacement of a plain file with a symlink during use of the POSIX "-R -L" options, which allows local users to modify the ownership of arbitrary files by leveraging a race condition.

---
- coreutils <unfixed> (unimportant)
http://lists.gnu.org/archive/html/coreutils/2017-12/msg00045.html
https://www.openwall.com/lists/oss-security/2018/01/04/3
Documentation patches proposed:
https://lists.gnu.org/archive/html/coreutils/2017-12/msg00072.html
https://lists.gnu.org/archive/html/coreutils/2017-12/msg00073.html
Neutralised by kernel hardening

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 1" src="https://img.shields.io/badge/L-1-fce1a9"/> <!-- unspecified: 0 --><strong>util-linux</strong> <code>2.38.1-5</code> (deb)</summary>

<small><code>pkg:deb/debian/util-linux@2.38.1-5?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2024-28085?s=debian&n=util-linux&ns=debian&t=deb&osn=debian&osv=12&vr=%3C2.38.1-5%2Bdeb12u1"><img alt="low : CVE--2024--28085" src="https://img.shields.io/badge/CVE--2024--28085-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code><2.38.1-5+deb12u1</code></td></tr>
<tr><td>Fixed version</td><td><code>2.38.1-5+deb12u1</code></td></tr>
<tr><td>EPSS Score</td><td><code>0.046%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>20th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

wall in util-linux through 2.40, often installed with setgid tty permissions, allows escape sequences to be sent to other users' terminals through argv. (Specifically, escape sequences received from stdin are blocked, but escape sequences received from argv are not blocked.) There may be plausible scenarios where this leads to account takeover.

---
- util-linux 2.39.3-11 (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1067849)
https://www.openwall.com/lists/oss-security/2024/03/27/5
https://github.com/util-linux/util-linux/commit/404b0781f52f7c045ca811b2dceec526408ac253 (v2.40)

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 1" src="https://img.shields.io/badge/L-1-fce1a9"/> <!-- unspecified: 0 --><strong>libpng1.6</strong> <code>1.6.39-2</code> (deb)</summary>

<small><code>pkg:deb/debian/libpng1.6@1.6.39-2?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2021-4214?s=debian&n=libpng1.6&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D1.6.39-2"><img alt="low : CVE--2021--4214" src="https://img.shields.io/badge/CVE--2021--4214-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=1.6.39-2</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.056%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>26th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A heap overflow flaw was found in libpngs' pngimage.c program. This flaw allows an attacker with local network access to pass a specially crafted PNG file to the pngimage utility, causing an application to crash, leading to a denial of service.

---
- libpng1.6 <unfixed> (unimportant)
https://github.com/glennrp/libpng/issues/302
Crash in CLI package, not shipped in binary packages

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 1" src="https://img.shields.io/badge/L-1-fce1a9"/> <!-- unspecified: 0 --><strong>pixman</strong> <code>0.42.2-1</code> (deb)</summary>

<small><code>pkg:deb/debian/pixman@0.42.2-1?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2023-37769?s=debian&n=pixman&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D0.42.2-1"><img alt="low : CVE--2023--37769" src="https://img.shields.io/badge/CVE--2023--37769-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=0.42.2-1</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.068%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>33rd percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

stress-test master commit e4c878 was discovered to contain a FPE vulnerability via the component combine_inner at /pixman-combine-float.c.

---
- pixman <unfixed> (unimportant)
https://gitlab.freedesktop.org/pixman/pixman/-/issues/76
Crash in test tool, no security impact

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 1" src="https://img.shields.io/badge/L-1-fce1a9"/> <!-- unspecified: 0 --><strong>openexr</strong> <code>3.1.5-5</code> (deb)</summary>

<small><code>pkg:deb/debian/openexr@3.1.5-5?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2017-14988?s=debian&n=openexr&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D3.1.5-5"><img alt="low : CVE--2017--14988" src="https://img.shields.io/badge/CVE--2017--14988-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=3.1.5-5</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.167%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>54th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

Header::readfrom in IlmImf/ImfHeader.cpp in OpenEXR 2.2.0 allows remote attackers to cause a denial of service (excessive memory allocation) via a crafted file that is accessed with the ImfOpenInputFile function in IlmImf/ImfCRgbaFile.cpp. NOTE: The maintainer and multiple third parties believe that this vulnerability isn't valid

---
- openexr <unfixed> (bug https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=878551; unimportant)
https://github.com/openexr/openexr/issues/248
Issue in the use of openexr via ImageMagick, no real security impact

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 1" src="https://img.shields.io/badge/L-1-fce1a9"/> <!-- unspecified: 0 --><strong>shadow</strong> <code>1:4.13+dfsg1-1</code> (deb)</summary>

<small><code>pkg:deb/debian/shadow@1:4.13%2Bdfsg1-1?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2007-5686?s=debian&n=shadow&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D1%3A4.13%2Bdfsg1-1"><img alt="low : CVE--2007--5686" src="https://img.shields.io/badge/CVE--2007--5686-lightgrey?label=low%20&labelColor=fce1a9"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=1:4.13+dfsg1-1</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.172%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>55th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

initscripts in rPath Linux 1 sets insecure permissions for the /var/log/btmp file, which allows local users to obtain sensitive information regarding authentication attempts.  NOTE: because sshd detects the insecure permissions and does not log certain events, this also prevents sshd from logging failed authentication attempts by remote attackers.

---
- shadow <unfixed> (unimportant)
See #290803, on Debian LOG_UNKFAIL_ENAB in login.defs is set to no so
unknown usernames are not recorded on login failures

</blockquote>
</details>
</details></td></tr>

<tr><td valign="top">
<details><summary><img alt="critical: 0" src="https://img.shields.io/badge/C-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/H-0-lightgrey"/> <img alt="medium: 0" src="https://img.shields.io/badge/M-0-lightgrey"/> <img alt="low: 0" src="https://img.shields.io/badge/L-0-lightgrey"/> <img alt="unspecified: 2" src="https://img.shields.io/badge/U-2-lightgrey"/><strong>libyaml</strong> <code>0.2.5-1</code> (deb)</summary>

<small><code>pkg:deb/debian/libyaml@0.2.5-1?os_distro=bookworm&os_name=debian&os_version=12</code></small><br/>
<a href="https://scout.docker.com/v/CVE-2024-35329?s=debian&n=libyaml&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D0.2.5-1"><img alt="unspecified : CVE--2024--35329" src="https://img.shields.io/badge/CVE--2024--35329-lightgrey?label=unspecified%20&labelColor=lightgrey"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=0.2.5-1</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.043%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>12th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

libyaml 0.2.5 is vulnerable to a heap-based Buffer Overflow in yaml_document_add_sequence in api.c.

---
REJECTED

</blockquote>
</details>

<a href="https://scout.docker.com/v/CVE-2024-3205?s=debian&n=libyaml&ns=debian&t=deb&osn=debian&osv=12&vr=%3E%3D0.2.5-1"><img alt="unspecified : CVE--2024--3205" src="https://img.shields.io/badge/CVE--2024--3205-lightgrey?label=unspecified%20&labelColor=lightgrey"/></a> 

<table>
<tr><td>Affected range</td><td><code>>=0.2.5-1</code></td></tr>
<tr><td>Fixed version</td><td><strong>Not Fixed</strong></td></tr>
<tr><td>EPSS Score</td><td><code>0.043%</code></td></tr>
<tr><td>EPSS Percentile</td><td><code>12th percentile</code></td></tr>
</table>

<details><summary>Description</summary>
<blockquote>

A vulnerability was found in yaml libyaml up to 0.2.5 and classified as critical. Affected by this issue is the function yaml_emitter_emit_flow_sequence_item of the file /src/libyaml/src/emitter.c. The manipulation leads to heap-based buffer overflow. The attack may be launched remotely. The exploit has been disclosed to the public and may be used. The identifier of this vulnerability is VDB-259052. NOTE: The vendor was contacted early about this disclosure but did not respond in any way.

---
REJECTED

</blockquote>
</details>
</details></td></tr>
</table>

