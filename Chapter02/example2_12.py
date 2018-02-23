class ThreadPoolExecutor(_base.Executor):
    def submit(self, fn, *args, **kwargs):
        [...]
        self._adjust_thread_count()

def _adjust_thread_count(self):
    [...]
    # TODO(bquinlan): Should avoid creating new threads if there are more
    # idle threads than items in the work queue.
    if len(self._threads) < self._max_workers:
        t = threading.Thread(target=_worker,
                            args=(weakref.ref(self, weakref_cb),
                                 self._work_queue))
    t.daemon = True
    t.start()
    self._threads.add(t)
    _threads_queues[t] = self._work_queue